def get_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content.strip()
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred: {e}"