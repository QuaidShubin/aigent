import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            print(f"Error: {e}")
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a specified file. Given a file path, it will create the file if file is not yet created, or overwrite existing file. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write / overwrite into the file.",
            ),
        },
    ),
)
