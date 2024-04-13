# Azure-Bulk-Containers-Download

To Download All the containers from Azure Storage I use the given script.

## Automatic Steps

To Download all the files and folders from the storage account you have to follow this step:

1. Enter the asked values in the script.sh file, which are:
    - account_name: Storage Account name
    - account_key: Storage Account Access Key
    - local_directory: Device where all data from storage will be Download
2. Then run the bash file using: "bash script.sh"

## Mannual Steps

1. Run this to select the env and the library:
    - python3 -m venv path/to/venv
    - source path/to/venv/bin/activate
2. Add the values in.py files
    - account_name
    - account_key
    - local_directory
3. Now run the file and download the data
    - Run the File
    - python3 azure_storage.py

### NOTE: You can view the progress and make sure to keep the window open untill its done
