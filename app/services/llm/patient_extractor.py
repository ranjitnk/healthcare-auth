import re

def extract_patient_data(text: str):
    # Added re.IGNORECASE to handle different naming conventions
    # The (.*?) is a non-greedy match which is safer for structured data
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