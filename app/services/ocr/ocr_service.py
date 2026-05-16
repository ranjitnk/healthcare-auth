def run_ocr(filename: str):

    try:
        with open(filename, "r") as f:
            text = f.read()

        return text

    except FileNotFoundError:
        return "File not found"