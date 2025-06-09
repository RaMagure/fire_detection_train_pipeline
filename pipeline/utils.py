import os
import gdown
import py7zr

def is_data_yaml_present_and_extract_7z(archive_path):
    """
    Extracts the given .7z file and searches for 'data.yaml' inside.

    Parameters:
        archive_path (str): Full path to the .7z archive.

    Returns:
        str: Full path to 'data.yaml' if found.

    Raises:
        FileNotFoundError: If no 'data.yaml' is found after extraction.
    """
    if not archive_path.endswith('.7z'):
        raise ValueError(f"❌ Not a valid .7z file: {archive_path}")
    
    extract_dir = os.path.splitext(archive_path)[0]
    os.makedirs(extract_dir, exist_ok=True)

    with py7zr.SevenZipFile(archive_path, mode='r') as archive:
        archive.extractall(path=extract_dir)

    # Search for data.yaml in extracted folder
    for root, _, files in os.walk(extract_dir):
        if 'data.yaml' in files:
            data_yaml_path = os.path.join(root, 'data.yaml')
            print(f"✅ Found data.yaml at: {data_yaml_path}")
            return data_yaml_path

    raise FileNotFoundError("❌ 'data.yaml' not found in extracted contents.")


def download_to_data_folder(gdrive_url, filename=None):
    """
    Download a file from Google Drive and save it to the 'data/' folder with an optional filename.

    Parameters:
        gdrive_url (str): Shareable Google Drive link.
        filename (str): Optional custom filename (e.g., 'my_file.7z').

    Returns:
        str: Path to the downloaded file.
    """
    # Make sure the 'data' folder exists
    data_folder = 'data'
    os.makedirs(data_folder, exist_ok=True)

    output_path = os.path.join(data_folder, filename) if filename else None

    # Use fuzzy=True to auto-handle view links
    downloaded_path = gdown.download(url=gdrive_url, output=output_path, quiet=False, fuzzy=True)

    if downloaded_path:
        print(f"✅ Downloaded to: {downloaded_path}")
        return downloaded_path
    else:
        raise Exception("❌ Failed to download file. Check the link or permissions.")


# Example usage:
# zip_path = download_to_data_folder('https://drive.google.com/your-share-link', filename='fireDetection.7z')
# print(is_data_yaml_present_and_extract_7z(zip_path))
