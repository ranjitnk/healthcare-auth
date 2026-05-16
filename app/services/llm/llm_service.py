import re

def extract_entities(text: str):

    patterns = {
        "patient_name": r"Patient Name:\s*(.*)",
        "insurance_id": r"Insurance ID:\s*(.*)",
        "procedure": r"Procedure:\s*(.*)"
    }

    extracted = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        extracted[key] = match.group(1).strip() if match else "Not Found"

    return extracted