import os
from .file_operations.create_file import create_file
from .file_operations.append_file import append_file
from .toolgen.register_tool import register_tool

def create_tool(tool_name: str, tool_directory: str, function_code: str, module: str, description: str) -> str:
    """
    Creates a new tool file, writes the provided function code, and registers the tool.

    Args:
        tool_name (str): The name of the tool (function) to create.
        tool_directory (str): The directory where the tool file will be created.
        function_code (str): The Python code for the function to be written to the file.
        module (str): The module name for registering the tool.
        description (str): The description of the tool for registration.

    Returns:
        str: A message indicating success or failure.
    """
    # Define the file path for the new tool
    tool_file_path = os.path.join(tool_directory, f"{tool_name}.py")
    
    # Create the tool file
    create_result = create_file(tool_file_path)
    if "Error" in create_result:
        return create_result

    # Append the function code to the tool file
    append_result = append_file(tool_file_path, function_code)
    if "Error" in append_result:
        return append_result

    # Register the tool
    registration_file_path = os.path.join(os.path.dirname(tool_directory), "function_registrations.py")
    try:
        register_tool(registration_file_path, module, tool_name, description)
    except ValueError as e:
        return f"Error during registration: {str(e)}"
    except Exception as e:
        return f"Unexpected error during registration: {str(e)}"

    return f"Tool '{tool_name}' created and registered successfully."