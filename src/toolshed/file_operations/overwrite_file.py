def overwrite_file(file_path: str, content: str) -> str:
    try:
        with open(file_path, 'w') as file:
            file.write(content + '\n')
        return "Content written to the file successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"