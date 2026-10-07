import streamlit as st
from ocr import extract_text
from analyzer import analyze_policy
from question_answer import answer_question
from comparison import compare_policies
st.set_page_config(
    page_title="PolicyLens AI",
    page_icon="📋",
    layout="wide"
)
st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #eef8ff 0%, #f7fbff 50%, #eaf5ff 100%);
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #075985;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #475569;
        margin-bottom: 25px;
    }

    .hero-box {
        background: linear-gradient(135deg, #0284c7, #0369a1);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(3, 105, 161, 0.18);
    }

    .hero-title {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .hero-text {
        font-size: 16px;
        line-height: 1.6;
    }

    .metric-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #dbeafe;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
        margin-bottom: 15px;
    }

    .metric-label {
        font-size: 13px;
        color: #64748b;
        margin-bottom: 5px;
    }

    .metric-value {
        font-size: 20px;
        font-weight: 700;
        color: #075985;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #075985;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .info-box {
        background: white;
        padding: 20px;
        border-radius: 14px;
        border-left: 5px solid #0284c7;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
        margin-bottom: 15px;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    [data-testid="stFileUploader"] {
        background: white;
        padding: 15px;
        border-radius: 14px;
        border: 1px solid #dbeafe;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<div class="main-title">PolicyLens AI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">OCR-Powered Insurance Policy Analyzer & Comparison Assistant</div>',
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">Understand Your Insurance Policy Faster</div>
        <div class="hero-text">
            Upload an insurance policy document and PolicyLens AI extracts
            important information such as premium, coverage, policy period,
            benefits, eligibility and other key details using Optical Character Recognition.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
uploaded_files = st.file_uploader(
    "Upload Insurance Policy Documents",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True,
    help="You can upload one policy for analysis or multiple policies for comparison."
)
if not uploaded_files:
    st.markdown(
        '<div class="section-title">How PolicyLens AI Works</div>',
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="info-box">
                <h4>1. Upload</h4>
                <p>Upload an insurance policy PDF or image.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="info-box">
                <h4>2. Extract</h4>
                <p>OCR reads the document and extracts important text.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div class="info-box">
                <h4>3. Understand</h4>
                <p>View key information, ask questions and compare policies.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("---")
    st.info(
        "Supported documents: Health Insurance, Life Insurance and other insurance policy documents."
    )
    st.stop()
policies = []
for file in uploaded_files:
    with st.spinner(f"Analyzing {file.name}..."):
        text = extract_text(file)
        policy = analyze_policy(text)
        policies.append(
            {
                "name": file.name,
                "text": text,
                "data": policy
            }
        )
st.success(f"{len(policies)} policy document(s) processed successfully.")
tabs = st.tabs(
    [
        "Dashboard",
        "Policy Details",
        "Ask Your Policy",
        "Compare Policies",
        "OCR Text"
    ]
)
with tabs[0]:
    st.markdown(
        '<div class="section-title">Policy Dashboard</div>',
        unsafe_allow_html=True
    )
    for item in policies:
        data = item["data"]
        st.subheader(item["name"])
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Insurance Company</div>
                    <div class="metric-value">{data.get("Insurance Company", "Not detected")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Product</div>
                    <div class="metric-value">{data.get("Product Name", "Not detected")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Premium</div>
                    <div class="metric-value">{data.get("Premium", "Not detected")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col4:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Base Sum Insured</div>
                    <div class="metric-value">{data.get("Base Sum Insured", "Not detected")}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.divider()
with tabs[1]:
    st.markdown(
        '<div class="section-title">Important Policy Information</div>',
        unsafe_allow_html=True
    )
    for item in policies:
        data = item["data"]
        st.subheader(item["name"])
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Insurance Company**")
            st.info(data.get("Insurance Company", "Not detected"))
            st.write("**Product Name**")
            st.info(data.get("Product Name", "Not detected"))
            st.write("**Policy Number**")
            st.info(data.get("Policy Number", "Not detected"))
            st.write("**Insurance Type**")
            st.info(data.get("Insurance Type", "Not detected"))
            st.write("**Premium**")
            st.info(data.get("Premium", "Not detected"))
            st.write("**GST**")
            st.info(data.get("GST", "Not detected"))
            st.write("**Total Premium**")
            st.info(data.get("Total Premium", "Not detected"))
            st.write("**Base Sum Insured**")
            st.info(data.get("Base Sum Insured", "Not detected"))
        with col2:
            st.write("**Policy Period**")
            st.info(data.get("Policy Period", "Not detected"))
            st.write("**Minimum Entry Age**")
            st.info(data.get("Minimum Entry Age", "Not detected"))
            st.write("**Maximum Entry Age**")
            st.info(data.get("Maximum Entry Age", "Not detected"))
            st.write("**Child Entry Age**")
            st.info(data.get("Child Entry Age", "Not detected"))
            st.write("**Family Adults**")
            st.info(data.get("Family Adults", "Not detected"))
            st.write("**Dependent Children**")
            st.info(data.get("Dependent Children", "Not detected"))
            st.write("**Bonus**")
            st.info(data.get("Bonus", "Not detected"))

        st.divider()
with tabs[2]:
    st.markdown(
        '<div class="section-title">Ask Your Policy</div>',
        unsafe_allow_html=True
    )
    policy_names = [item["name"] for item in policies]
    selected_policy = st.selectbox(
        "Select a policy",
        policy_names
    )
    selected_item = next(
        item for item in policies
        if item["name"] == selected_policy
    )
    question = st.text_input(
        "Ask a question",
        placeholder="Example: What is the premium amount?"
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Premium"):
            question = "What is the premium?"
    with col2:
        if st.button("Coverage"):
            question = "What is the coverage amount?"
    with col3:
        if st.button("Policy Period"):
            question = "What is the policy period?"
    with col4:
        if st.button("Benefits"):
            question = "What are the benefits?"
    if st.button("Get Answer", type="primary"):
        if question.strip():
            answer = answer_question(
                question,
                selected_item["text"],
                selected_item["data"]
            )
            st.markdown(
                f"""
                <div class="info-box">
                    <h4>PolicyLens Answer</h4>
                    <p>{answer}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter a question.")
with tabs[3]:
    st.markdown(
        '<div class="section-title">Compare Insurance Policies</div>',
        unsafe_allow_html=True
    )
    if len(policies) < 2:
        st.info(
            "Upload at least two insurance policies to use the comparison feature."
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
        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True
        )
with tabs[4]:
    st.markdown(
        '<div class="section-title">Extracted OCR Text</div>',
        unsafe_allow_html=True
    )
    for item in policies:
        with st.expander(item["name"]):
            st.text_area(
                "OCR Output",
                item["text"],
                height=400,
                key=f"ocr_{item['name']}"
            )
st.markdown("---")
st.caption(
    "PolicyLens AI | OCR-Based Insurance Policy Analysis | Extract → Analyze → Understand"
)