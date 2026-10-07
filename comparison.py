def compare_policies(policy1, policy2, policy3=None):
    fields = [
        "Insurance Company",
        "Product Name",
        "Policy Number",
        "Insurance Type",
        "Premium",
        "GST",
        "Total Premium",
        "Base Sum Insured",
        "Policy Period",
        "Minimum Entry Age",
        "Maximum Entry Age",
        "Child Entry Age",
        "Family Adults",
        "Dependent Children",
        "Secure Benefit",
        "Plus Benefit",
        "Automatic Restore Benefit",
        "Protect Benefit",
        "Global Cover",
        "Bonus"
    ]
    comparison = []
    for field in fields:
        row = {
            "Feature": field,
            "Policy 1": policy1.get(
                field,
                "Not detected"
            ),
            "Policy 2": policy2.get(
                field,
                "Not detected"
            )
        }
        if policy3:
            row["Policy 3"] = policy3.get(
                field,
                "Not detected"
            )
        comparison.append(row)
    return comparison