import os
import json

def register_tool(file_path:str, module:str, name:str, description:str) -> str:
    """
    Adds a new registration entry to the function_registrations.py file.
    
    Args:
        file_path (str): Path to the function_registrations.py file.
        module (str): The module name to add.
        name (str): The name of the function to add.
        description (str): The description of the function.
    
    Behavior:
        - Creates the file if it doesn't exist.
        - Ensures 'function_registrations' is present and updates it.
        - Appends the new entry if it doesn't already exist.
    """
    # Ensure the file exists; create it if missing
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("function_registrations = {\n    \"registrations\": []\n}\n")

    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()

    # Safely extract or initialize the `function_registrations` object
    exec_globals = {}
    try:
        exec(content, exec_globals)
        function_registrations = exec_globals.get("function_registrations", {"registrations": []})
    except Exception as e:
        raise ValueError(f"Error parsing the file: {e}")

    # Check for duplicates
    for registration in function_registrations["registrations"]:
        if registration["name"] == name:
            raise ValueError(f"A registration with the name '{name}' already exists.")

    # Add the new registration
    new_registration = {
        "module": module,
        "name": name,
        "description": description
    }
    function_registrations["registrations"].append(new_registration)

    # Write the updated content back to the file
    updated_content = f"function_registrations = {json.dumps(function_registrations, indent=4)}\n"
    with open(file_path, 'w') as file:
        file.write(updated_content)
