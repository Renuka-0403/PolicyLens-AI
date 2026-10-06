def compare_policies(policy1, policy2, policy3=None):
    fields = [
        "Policy Number",
        "Premium",
        "Sum Assured",
        "Policy Term",
        "Maturity Date",
        "Premium Frequency",
        "Grace Period",
        "Waiting Period",
        "Nominee",
        "Maturity Benefit",
        "Death Benefit"
    ]

    comparison = []

    for field in fields:
        row = {
            "Feature": field,
            "Policy 1": policy1.get(field, "Not detected"),
            "Policy 2": policy2.get(field, "Not detected")
        }

        if policy3:
            row["Policy 3"] = policy3.get(field, "Not detected")

        comparison.append(row)

    return comparison