import os

def create_file(file_path: str) -> str:
    try:
        with open(file_path, 'w') as file:
            file.write('')
        return f"File '{file_path}' created successfully."
    except Exception as e:
        return f"Error creating file: {str(e)}"