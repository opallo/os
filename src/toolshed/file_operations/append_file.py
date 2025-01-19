def append_file(file_path: str, content: str) -> str:
    try:
        with open(file_path, 'a') as file:
            file.write('\n' + content + '\n')
        return "Content appended to the file successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"