def run_ocr(filename):

    with open(filename, "r") as f:
        text = f.read()

    return text