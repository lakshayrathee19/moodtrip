import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    /* Page Styling */
    body {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    .custom-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }

    .custom-header {
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 2s infinite alternate;
    }

    .custom-sub {
        font-size: 1.2rem;
        color: #aaa;
        margin-top: -0.5rem;
        margin-bottom: 2rem;
        text-align: center;
    }

    @keyframes glow {
        0% { text-shadow: 0 0 10px #00c6ff; }
        100% { text-shadow: 0 0 20px #0072ff; }
    }

    .playlist ul {
        padding-left: 1.2rem;
    }

    .playlist li {
        margin-bottom: 0.5rem;
    }

    </style>
    """, unsafe_allow_html=True)
