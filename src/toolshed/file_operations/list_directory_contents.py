import os

def list_directory_contents(directory_path: str) -> list:
    try:
        # Get the list of contents in the directory
        contents = os.listdir(directory_path)
        return contents
    except Exception as e:
        return f"Error: {str(e)}"

