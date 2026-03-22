# app.py (COLORFUL + STYLED STREAMLIT UI)

import streamlit as st
from similarity import compute_similarity


# 🔹 Page config
st.set_page_config(page_title="Document Similarity Checker", page_icon="📄", layout="centered")


# 🔹 Custom CSS (COLORS ADDED)
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to right, #eef2f3, #dfe9f3);
        }

        .title {
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            color: #2c3e50;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 25px;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        .result-high {
            background: #e8f8f5;
            border-left: 6px solid #1abc9c;
        }

        .result-medium {
            background: #fff8e1;
            border-left: 6px solid #f39c12;
        }

        .result-low {
            background: #fdecea;
            border-left: 6px solid #e74c3c;
        }

        .score {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #4A90E2;
        }

        .stButton>button {
            background: linear-gradient(to right, #4A90E2, #6dd5fa);
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            border: none;
        }

        .stButton>button:hover {
            background: linear-gradient(to right, #357ABD, #4facfe);
        }
    </style>
""", unsafe_allow_html=True)


# 🔹 Title
st.markdown('<div class="title">📄 Document Similarity Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Compare documents using TF-IDF & Cosine Similarity</div>', unsafe_allow_html=True)


# 🔹 Upload Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📂 Document 1")
    file1 = st.file_uploader("Upload File", type=["txt"], key="file1")

with col2:
    st.markdown("### 📂 Document 2")
    file2 = st.file_uploader("Upload File", type=["txt"], key="file2")


# 🔹 Compare Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Compare Documents", use_container_width=True):

    if file1 and file2:

        doc1 = file1.read().decode("utf-8")
        doc2 = file2.read().decode("utf-8")

        with st.spinner("Analyzing documents..."):
            score = compute_similarity(doc1, doc2)

        percentage = round(score * 100, 2)

        # 🔹 Choose color class
        if score > 0.7:
            result_class = "result-high"
            message = "📌 Documents are Highly Similar"
            st.success(message)
        elif score > 0.4:
            result_class = "result-medium"
            message = "📌 Documents are Moderately Similar"
            st.warning(message)
        else:
            result_class = "result-low"
            message = "📌 Documents are Not Similar"
            st.error(message)

        # 🔹 Result Card
        st.markdown(f"""
            <div class="card {result_class}">
                <h2 style="text-align:center;">🔍 Similarity Score</h2>
                <div class="score">{percentage}%</div>
            </div>
        """, unsafe_allow_html=True)

        # 🔹 Preview Section
        st.markdown("### 📄 Document Preview")

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Document 1**")
            st.markdown(f'<div class="card">{doc1[:300]}</div>', unsafe_allow_html=True)

        with col4:
            st.markdown("**Document 2**")
            st.markdown(f'<div class="card">{doc2[:300]}</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please upload both files.")

# streamlit run "c:\Users\agarw\OneDrive\Desktop\IRT\app.py"