import re

PARAMETERS = [
    "glucose",
    "cholesterol",
    "hdl",
    "ldl",
    "triglycerides",
    "hemoglobin",
    "wbc",
    "rbc",
    "platelets",
    "creatinine",
    "urea",
    "bilirubin",
    "alt",
    "ast",
    "sodium",
    "potassium",
    "calcium",
    "bmi",
    "heart rate",
    "blood pressure"
]

def extract_values(text):

    results = {}

    text = text.lower()

    for param in PARAMETERS:

        pattern = rf"{param}\s*[:\-]?\s*([0-9.]+)"

        match = re.search(pattern, text)

        if match:
            results[param] = float(match.group(1))

    return results