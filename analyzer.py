import re
def clean_value(value):
    value = value.strip()
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" :-;,")
    return value
def find_value(text, patterns):
    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )
        if match:
            value = clean_value(match.group(1))
            if value and value not in [",", ".", ":", "-"]:
                return value
    return "Not detected"
def analyze_policy(text):
    policy = {}
    text = text.replace("\r", "")
    policy["Insurance Company"] = find_value(
        text,
        [
            r"(HDFC\s*ERGO\s*General\s*Insurance\s*Company\s*Limited)",
            r"(STAR\s*HEALTH\s*AND\s*ALLIED\s*INSURANCE\s*COMPANY\s*LIMITED)"
        ]
    )
    policy["Product Name"] = find_value(
        text,
        [
            r"(Optima\s*Secure)",
            r"(FAMILY\s*HEALTH\s*OPTIMA\s*INSURANCE\s*POLICY)"
        ]
    )
    policy["Policy Number"] = find_value(
        text,
        [
            r"Policy\s*(?:No\.?|Number|Ho\.?)\s*[:\-]?\s*([A-Z0-9][A-Z0-9\s\/\-]{5,})"
        ]
    )
    policy["Insurance Type"] = find_value(
        text,
        [
            r"(indemnity\s+health\s+insurance)",
            r"(health\s+insurance\s+product)",
            r"(health\s+insurance\s+policy)",
            r"(health\s+insurance)"
        ]
    )
    policy["Premium"] = find_value(
        text,
        [
            r"Premium\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9A-Za-z,\.]+)",
            r"Premium\s*[:\-]?\s*([0-9][0-9,\.]+)"
        ]
    )
    policy["GST"] = find_value(
        text,
        [
            r"GST\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9,\.]+)",
            r"GST\s*(?:Rs?|Re|₹)\s*([0-9,\.]+)"
        ]
    )
    policy["Total Premium"] = find_value(
        text,
        [
            r"Total\s+Premium\s*[:\-]?\s*(?:Rs?|Re|₹)\s*([0-9,\.]+)",
            r"Tota[l]?\s+Premium\s*(?:Rs?|Re|₹)\s*([0-9,\.]+)"
        ]
    )
    policy["Base Sum Insured"] = find_value(
        text,
        [
            r"SUM\s*INSURED\s*[:\-]?\s*[₹Rs\.]*\s*([0-9][0-9,]*)\s*/-",
            r"SUMINSURED\s*[:\-]?\s*[₹Rs\.]*\s*([0-9][0-9,]*)\s*/-",
            r"SUM\s+INSURED.*?([0-9][0-9,]*)\s*/-"
        ]
    )
    policy["Policy Period"] = find_value(
        text,
        [
            r"PERIOD\s+OF\s+(?:INSURANCE|WSURANCE)\s+FROM\s*[:;]?\s*(.{10,120}?)(?:\n|$)",
            r"period\s+of\s+insurance\s+from\s*[:;]?\s*(.{10,120}?)(?:\n|$)",
            r"issued\s+for\s+a\s+period\s+of\s+(\d+)\s*years?"
        ]
    )
    policy["Secure Benefit"] = find_value(
        text,
        [
            r"Secure\s+Benefit.*?additional\s+coverage.*?equivalent\s+to\s*([0-9%\/]+)"
        ]
    )
    policy["Plus Benefit"] = find_value(
        text,
        [
            r"Plus\s+Benefit.*?additional\s+coverage.*?([0-9%]+)"
        ]
    )
    policy["Automatic Restore Benefit"] = find_value(
        text,
        [
            r"Automatic\s+Restore\s+Benefits?.*?restores\s*([0-9%]+)"
        ]
    )
    policy["Protect Benefit"] = find_value(
        text,
        [
            r"Protect\s+Benefit.*?pays.*?towards\s+the\s+(.{10,120}?)(?:during|hospitalization|\n)"
        ]
    )
    policy["Global Cover"] = find_value(
        text,
        [
            r"Global\s+cover.*?provides\s+coverage\s+for\s+(.{10,150}?)(?:\n\n|\.)"
        ]
    )
    policy["Minimum Entry Age"] = find_value(
        text,
        [
            r"minimum\s+entry\s+age\s+for\s+an\s+adult\s+is\s+(\d+\s*years?)",
            r"minimum\s+entry\s+age.*?(\d+\s*years?)",
            r"age\s+group\s+(\d+\s+days?)"
        ]
    )
    policy["Maximum Entry Age"] = find_value(
        text,
        [
            r"maximum\s+entry\s+age\s+(?:is|of)?\s*(\d+\s*years?)",
            r"maximum\s+entry\s+age.*?(\d+\s*years?)"
        ]
    )
    policy["Child Entry Age"] = find_value(
        text,
        [
            r"minimum\s+entry\s+age\s+for\s+a\s+dependent\s+child.*?(\d+\s+days?)",
            r"dependent\s+child.*?(\d+\s+days?)"
        ]
    )
    family_match = re.search(
        r"(\d+)\s*ADULTS?\s*\+\s*(\d+)\s*CHILD",
        text,
        re.IGNORECASE
    )
    if family_match:
        policy["Family Adults"] = family_match.group(1)
        policy["Dependent Children"] = family_match.group(2)
    else:
        policy["Family Adults"] = find_value(
            text,
            [
                r"maximum\s+of\s+(\d+)\s+adults",
                r"(\d+)\s*ADULTS"
            ]
        )
        policy["Dependent Children"] = find_value(
            text,
            [
                r"maximum\s+of\s+(\d+)\s+dependent\s+children",
                r"(\d+)\s*CHILD"
            ]
        )
    policy["Bonus"] = find_value(
        text,
        [
            r"LIMIT\s+OF\s+COVERAGE\s*[:\-]?\s*(?:Rs?|Re|₹)?\s*([0-9,]+)\s*Bonus",
            r"Bonus\s*[:\-]?\s*(?:Rs?|Re|₹)?\s*([0-9,]+)"
        ]
    )
    return policy