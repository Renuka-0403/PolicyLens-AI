import re

def find_value(text, patterns):
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

        if match:
            value = match.group(1).strip()

            if value and value not in [",", ".", ":", "-", "/"]:
                return value

    return "Not detected"


def analyze_policy(text):

    policy = {}

    policy["Insurance Company"] = find_value(text, [
        r"(HDFC\s*ERGO\s*General\s*Insurance\s*Company\s*Limited)",
        r"(STAR\s*HEALTH\s*AND\s*ALLIED\s*INSURANCE\s*COMPANY\s*LIMITED)"
    ])

    policy["Product Name"] = find_value(text, [
        r"(Optima\s*Secure)",
        r"(FAMILY\s*HEALTH\s*OPTIMA\s*INSURANCE\s*POLICY)"
    ])

    policy["Policy Number"] = find_value(text, [
        r"Policy\s*(?:No\.?|Number|Ho\.?)\s*[:\-]?\s*([A-Z0-9][A-Z0-9\s\/\-]{5,})"
    ])

    policy["Insurance Type"] = find_value(text, [
        r"(indemnity\s+health\s+insurance)",
        r"(health\s+insurance\s+product)",
        r"(health\s+insurance\s+policy)",
        r"(health\s+insurance)"
    ])

    policy["Premium"] = find_value(text, [
        r"Premium\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9A-Za-z,\.]+)",
        r"Premium\s*[:\-]?\s*([0-9][0-9A-Za-z,\.]*)"
    ])

    policy["GST"] = find_value(text, [
        r"GST\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9A-Za-z,\.]+)",
        r"GST\s*[:\-]?\s*([0-9][0-9A-Za-z,\.]*)"
    ])

    policy["Total Premium"] = find_value(text, [
        r"Total\s*Premium\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9A-Za-z,\.]+)",
        r"Tota[l]?\s*Premium\s*(?:Rs?|Re|₹)\s*([0-9A-Za-z,\.]+)"
    ])

    policy["Base Sum Insured"] = find_value(text, [
        r"SUM\s*INSURED.*?(\d[\d,]*)\s*/-",
        r"SUMINSURED.*?(\d[\d,]*)\s*/-",
        r"BASE\s*SUM\s*INSURED.*?(\d[\d,]*)",
        r"SUM\s*INSURED\s*[:\-]?\s*[₹Rs\.]*\s*([\d,]+)"
    ])

    policy["Policy Period"] = find_value(text, [
        r"PERIOD\s+OF\s+(?:INSURANCE|WSURANCE)\s+FROM\s*[:;]?\s*(.{10,120}?)(?:\n|$)",
        r"period\s+of\s+insurance\s+from\s*[:;]?\s*(.{10,120}?)(?:\n|$)",
        r"issued\s+for\s+a\s+period\s+of\s+(\d+\s*years?)"
    ])

    policy["Secure Benefit"] = find_value(text, [
        r"Secure\s+Benefit.*?(?:equivalent\s+to|of)\s*([\d%\/]+)"
    ])

    policy["Plus Benefit"] = find_value(text, [
        r"Plus\s+Benefit.*?(?:equivalent\s+to|of)\s*([\d%]+)"
    ])

    policy["Automatic Restore Benefit"] = find_value(text, [
        r"Automatic\s+Restore\s+Benefits?.*?restores\s*([\d%]+)"
    ])

    policy["Protect Benefit"] = find_value(text, [
        r"Protect\s+Benefit.*?pays\s+towards\s+(.*?)(?:\n|$)"
    ])

    policy["Global Cover"] = find_value(text, [
        r"Global\s+cover.*?provides\s+coverage\s+for\s+(.*?)(?:\n|$)"
    ])

    policy["Minimum Entry Age"] = find_value(text, [
        r"minimum\s+entry\s+age\s+for\s+an\s+adult\s+is\s+(\d+\s*years?)",
        r"age\s+group\s+(\d+\s*days?)"
    ])

    policy["Maximum Entry Age"] = find_value(text, [
        r"maximum\s+entry\s+age\s+(?:is|of)\s+(\d+\s*years?)",
        r"maximum\s+entry\s+age.*?(\d+\s*years?)"
    ])

    policy["Child Entry Age"] = find_value(text, [
        r"minimum\s+entry\s+age\s+for\s+a\s+dependent\s+child.*?(\d+\s*days?)",
        r"dependent\s+child.*?(\d+\s*days?)"
    ])

    policy["Family Adults"] = find_value(text, [
        r"(\d+)\s*ADULTS"
    ])

    policy["Dependent Children"] = find_value(text, [
        r"(\d+)\s*CHILD"
    ])

    policy["Bonus"] = find_value(text, [
        r"LIMIT\s+OF\s+COVERAGE\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([\d,]+)\s*Bonus",
        r"([\d,]+)\s*Bonus"
    ])

    return policy