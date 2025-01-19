import os

def delete_file(file_path: str) -> str:
    try:
        os.remove(file_path)
        return 'File deleted successfully'
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return f'An error occurred: {str(e)}'
