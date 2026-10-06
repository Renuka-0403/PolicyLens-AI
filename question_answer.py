import re

def find_sentences(text, keywords):
    sentences = re.split(r'(?<=[.!?])\s+|\n+', text)

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

    if "premium" in question or "pay" in question or "payment" in question:
        return f"The premium amount is {policy.get('Premium', 'Not detected')}."

    if "maturity date" in question or "when does" in question and "mature" in question:
        return f"The maturity date is {policy.get('Maturity Date', 'Not detected')}."

    if "maturity benefit" in question:
        return f"The maturity benefit is {policy.get('Maturity Benefit', 'Not detected')}."

    if "maturity" in question:
        return (
            f"The maturity date is {policy.get('Maturity Date', 'Not detected')} "
            f"and the maturity benefit is {policy.get('Maturity Benefit', 'Not detected')}."
        )

    if "sum assured" in question or "sum insured" in question or "coverage" in question:
        return f"The coverage amount is {policy.get('Sum Assured', 'Not detected')}."

    if "policy term" in question or "how long" in question:
        return f"The policy term is {policy.get('Policy Term', 'Not detected')}."

    if "nominee" in question:
        nominee = policy.get("Nominee", "Not detected")
        death_benefit = policy.get("Death Benefit", "Not detected")

        return (
            f"The nominee is {nominee}. "
            f"The death benefit information is: {death_benefit}"
        )

    if "waiting period" in question or "wait" in question:
        return f"The waiting period is {policy.get('Waiting Period', 'Not detected')}."

    if "grace period" in question or "grace" in question:
        return f"The grace period is {policy.get('Grace Period', 'Not detected')}."

    if "benefit" in question or "benefits" in question:
        return find_sentences(text, ["benefit", "bonus", "coverage"])

    if "exclusion" in question or "excluded" in question or "not covered" in question:
        return find_sentences(text, ["exclusion", "excluded", "not covered"])

    if "claim" in question:
        return find_sentences(text, ["claim", "claim process", "claim settlement"])

    if "document" in question or "documents" in question:
        return find_sentences(text, ["document", "documents", "proof"])

    if "bonus" in question:
        return find_sentences(text, ["bonus", "additional bonus"])

    return "I could not find a matching answer in the extracted policy text."