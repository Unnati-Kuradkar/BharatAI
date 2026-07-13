import streamlit as st

st.set_page_config(
    page_title="BharatAI",
    layout="wide"
)

st.title("🇮🇳 BharatAI")
st.subheader("AI Government Opportunities Assistant")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Profile",
        "Dashboard"
    ]
)

if menu == "Home":
    st.write("""
    Welcome to BharatAI!

    Discover:
    - Government Schemes
    - Scholarships
    - Loans
    - Personalized Recommendations
    """)
