import sys
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Retrieve command-line arguments
account_name = sys.argv[1]
account_key = sys.argv[2]
local_directory = sys.argv[3]

# Function to track download progress
def progress_callback(current, total, container_number):
    print(f"Container {container_number}: Downloaded {current} of {total} bytes ({(current/total) * 100:.2f}%)")

# Create a BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# List containers in the storage account
containers = list(blob_service_client.list_containers())

# Count of containers
total_containers = len(containers)
containers_processed = 0

# Print initial message
print(f"\033[1m\nAll Containers of {account_name} is going to start download.\033[0m")
print(f"\033[1mWe have {total_containers} containers.\033[0m\n")

# Iterate through each container
for container_number, container in enumerate(containers, start=1):
    containers_processed += 1
    print(f"\033[1mProcessing container {containers_processed}/{total_containers}.\033[0m")
    
    container_client = blob_service_client.get_container_client(container.name)
    
    # Create a directory with the container name to store the downloaded blobs
    os.makedirs(os.path.join(local_directory, container.name), exist_ok=True)
    
    # List blobs in the container
    blobs = container_client.list_blobs()
    
    # Download each blob in the container
    for blob in blobs:
        blob_client = container_client.get_blob_client(blob)
        
        # Determine the local file path
        local_file_path = os.path.join(local_directory, container.name, blob.name)
        
        # Skip download if file already exists locally
        if os.path.exists(local_file_path):
            print(f"Container {container_number}: \033[3mSkipped '{blob.name}' as it already exists locally.\033[0m")
            continue
        
        # Get blob properties to calculate total size for progress tracking
        blob_properties = blob_client.get_blob_properties()
        total_size = blob_properties.size
        
        # Download the blob to the local directory with progress tracking
        with open(local_file_path, "wb") as f:
            download_stream = blob_client.download_blob()
            bytes_downloaded = 0
            for chunk in download_stream.chunks():
                f.write(chunk)
                bytes_downloaded += len(chunk)
                progress_callback(bytes_downloaded, total_size, container_number)

print("\033[1m\nAll files downloaded successfully!\033[0m")
