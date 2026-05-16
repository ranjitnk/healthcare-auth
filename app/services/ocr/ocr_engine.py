def extract_text(file_path: str):

    try:
        with open(file_path, "r") as f:
            text = f.read()

        return text

    except FileNotFoundError:
        return "File not found"