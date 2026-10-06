import streamlit as st
from ocr import extract_text
from analyzer import analyze_policy
from question_answer import answer_question
from comparison import compare_policies
st.set_page_config(
    page_title="PolicyLens AI",
    page_icon="📄",
    layout="wide"
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #eaf6ff;
    }

    h1 {
        color: #1565c0;
    }

    h2, h3 {
        color: #1976d2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("PolicyLens AI")
st.subheader("OCR-Powered Insurance Policy Analyzer")
st.write(
    "Upload an insurance policy PDF or image to extract "
    "important information, ask questions, and compare policies."
)
uploaded_files = st.file_uploader(
    "Upload Insurance Policy",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)
if uploaded_files:
    policies = []
    for file in uploaded_files:
        with st.spinner("Processing " + file.name + "..."):
            text = extract_text(file)
            policy = analyze_policy(text)
            policies.append(
                {
                    "name": file.name,
                    "text": text,
                    "data": policy
                }
            )
    st.success("Policy processing completed.")
    tabs = st.tabs(
        [
            "Policy Summary",
            "Important Information",
            "Ask Your Policy",
            "Compare Policies"
        ]
    )
    with tabs[0]:
        st.header("Policy Summary")
        for item in policies:
            st.subheader(item["name"])
            data = item["data"]
            col1, col2 = st.columns(2)
            with col1:
                st.write(
                    "**Insurance Company:**",
                    data.get("Insurance Company", "Not detected")
                )
                st.write(
                    "**Product Name:**",
                    data.get("Product Name", "Not detected")
                )
                st.write(
                    "**Policy Number:**",
                    data.get("Policy Number", "Not detected")
                )
                st.write(
                    "**Insurance Type:**",
                    data.get("Insurance Type", "Not detected")
                )
                st.write(
                    "**Premium:**",
                    data.get("Premium", "Not detected")
                )
                st.write(
                    "**Total Premium:**",
                    data.get("Total Premium", "Not detected")
                )
                st.write(
                    "**Base Sum Insured:**",
                    data.get("Base Sum Insured", "Not detected")
                )
            with col2:
                st.write(
                    "**Policy Period:**",
                    data.get("Policy Period", "Not detected")
                )
                st.write(
                    "**GST:**",
                    data.get("GST", "Not detected")
                )
                st.write(
                    "**Bonus:**",
                    data.get("Bonus", "Not detected")
                )
                st.write(
                    "**Minimum Entry Age:**",
                    data.get("Minimum Entry Age", "Not detected")
                )
                st.write(
                    "**Maximum Entry Age:**",
                    data.get("Maximum Entry Age", "Not detected")
                )
                st.write(
                    "**Family Adults:**",
                    data.get("Family Adults", "Not detected")
                )
                st.write(
                    "**Dependent Children:**",
                    data.get("Dependent Children", "Not detected")
                )
            st.divider()
    with tabs[1]:
        st.header("Important Information")
        for item in policies:
            st.subheader(item["name"])
            data = item["data"]
            st.write(
                "**Secure Benefit:**",
                data.get("Secure Benefit", "Not detected")
            )
            st.write(
                "**Plus Benefit:**",
                data.get("Plus Benefit", "Not detected")
            )
            st.write(
                "**Automatic Restore Benefit:**",
                data.get("Automatic Restore Benefit", "Not detected")
            )
            st.write(
                "**Protect Benefit:**",
                data.get("Protect Benefit", "Not detected")
            )
            st.write(
                "**Global Cover:**",
                data.get("Global Cover", "Not detected")
            )
            st.divider()
    with tabs[2]:
        st.header("Ask Your Policy")
        policy_names = [
            item["name"]
            for item in policies
        ]
        selected_policy = st.selectbox(
            "Select a policy",
            policy_names
        )
        selected_item = next(
            item for item in policies
            if item["name"] == selected_policy
        )
        question = st.text_input(
            "Ask a question about your policy",
            placeholder="Example: What is the premium?"
        )
        if st.button("Get Answer"):
            if question.strip():
                answer = answer_question(
                    question,
                    selected_item["text"],
                    selected_item["data"]
                )
                st.info(answer)
            else:
                st.warning(
                    "Please enter a question."
                )
    with tabs[3]:
        st.header("Compare Policies")
        if len(policies) < 2:
            st.info(
                "Upload at least two policies to compare them."
            )
        else:
            policy1 = policies[0]["data"]
            policy2 = policies[1]["data"]
            policy3 = None
            if len(policies) >= 3:
                policy3 = policies[2]["data"]
            comparison = compare_policies(
                policy1,
                policy2,
                policy3
            )
            st.table(comparison)
    st.divider()
    with st.expander("View Extracted OCR Text"):
        for item in policies:
            st.subheader(item["name"])
            st.text_area(
                "OCR Text",
                item["text"],
                height=300,
                key="ocr_" + item["name"]
            )
else:
    st.info(
        "Upload an insurance policy PDF or image to begin."
    )
st.caption(
    "PolicyLens AI | OCR-Based Insurance Policy Analysis"
)