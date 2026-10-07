import re
def find_sentences(text, keywords):
    sentences = re.split(
        r"(?<=[.!?])\s+|\n+",
        text
    )
    results = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        for keyword in keywords:
            if keyword in sentence_lower:
                sentence = sentence.strip()
                if sentence and sentence not in results:
                    results.append(sentence)
                break
    if results:
        return " ".join(results[:3])
    return "No relevant information was found in the policy."
def answer_question(question, text, policy):
    question = question.lower().strip()
    if (
        "premium" in question
        or "pay" in question
        or "payment" in question
    ):
        return (
            f"The premium amount is "
            f"{policy.get('Premium', 'Not detected')}."
        )
    if "gst" in question:
        return (
            f"The GST amount is "
            f"{policy.get('GST', 'Not detected')}."
        )
    if "total premium" in question:
        return (
            f"The total premium is "
            f"{policy.get('Total Premium', 'Not detected')}."
        )
    if (
        "sum insured" in question
        or "sum assured" in question
        or "coverage amount" in question
        or "coverage" in question
    ):
        return (
            f"The base sum insured or coverage amount is "
            f"{policy.get('Base Sum Insured', 'Not detected')}."
        )
    if (
        "policy period" in question
        or "period of insurance" in question
        or "how long" in question
    ):
        return (
            f"The policy period is "
            f"{policy.get('Policy Period', 'Not detected')}."
        )
    if (
        "company" in question
        or "insurer" in question
        or "insurance company" in question
    ):
        return (
            f"The insurance company is "
            f"{policy.get('Insurance Company', 'Not detected')}."
        )
    if "product" in question:

        return (
            f"The insurance product is "
            f"{policy.get('Product Name', 'Not detected')}."
        )
    if (
        "policy number" in question
        or "policy no" in question
    ):
        return (
            f"The policy number is "
            f"{policy.get('Policy Number', 'Not detected')}."
        )
    if "minimum age" in question:
        return (
            f"The minimum entry age is "
            f"{policy.get('Minimum Entry Age', 'Not detected')}."
        )
    if "maximum age" in question:
        return (
            f"The maximum entry age is "
            f"{policy.get('Maximum Entry Age', 'Not detected')}."
        )
    if (
        "child age" in question
        or "children age" in question
    ):
        return (
            f"The child entry age is "
            f"{policy.get('Child Entry Age', 'Not detected')}."
        )
    if "family" in question:
        adults = policy.get(
            "Family Adults",
            "Not detected"
        )
        children = policy.get(
            "Dependent Children",
            "Not detected"
        )
        return (
            f"The policy allows {adults} adult(s) "
            f"and {children} dependent child(ren), "
            f"based on the detected policy information."
        )
    if "secure benefit" in question:
        return (
            f"The Secure Benefit is "
            f"{policy.get('Secure Benefit', 'Not detected')}."
        )
    if "plus benefit" in question:
        return (
            f"The Plus Benefit is "
            f"{policy.get('Plus Benefit', 'Not detected')}."
        )
    if "restore" in question:
        return (
            f"The Automatic Restore Benefit is "
            f"{policy.get('Automatic Restore Benefit', 'Not detected')}."
        )
    if "protect benefit" in question:
        return (
            f"The Protect Benefit information is "
            f"{policy.get('Protect Benefit', 'Not detected')}."
        )
    if "global" in question:
        return (
            f"The Global Cover information is "
            f"{policy.get('Global Cover', 'Not detected')}."
        )
    if (
        "benefit" in question
        or "benefits" in question
    ):
        return find_sentences(
            text,
            [
                "benefit",
                "coverage",
                "bonus",
                "restore"
            ]
        )
    if (
        "exclusion" in question
        or "excluded" in question
        or "not covered" in question
    ):
        return find_sentences(
            text,
            [
                "exclusion",
                "excluded",
                "not covered"
            ]
        )
    if "claim" in question:
        return find_sentences(
            text,
            [
                "claim",
                "claim process",
                "claim settlement"
            ]
        )
    if (
        "document" in question
        or "documents" in question
    ):
        return find_sentences(
            text,
            [
                "document",
                "documents",
                "proof"
            ]
        )
    if "bonus" in question:
        return (
            f"The detected bonus information is "
            f"{policy.get('Bonus', 'Not detected')}."
        )
    return (
        "I could not find a matching answer in the "
        "extracted policy text."
    )