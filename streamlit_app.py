import streamlit as st
from database import (
    create_database,
    save_profile,
    get_latest_profile,
    get_recommended_schemes
)

st.set_page_config(
    page_title="BharatAI",
    layout="wide"
)

create_database()

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

elif menu == "Profile":

    st.header("Create Your Profile")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100
    )

    state = st.text_input("State")

    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Farmer",
            "Business",
            "Other"
        ]
    )

    income = st.number_input(
        "Income",
        min_value=0
    )

    if st.button("Save Profile"):

        st.success("Profile Saved Successfully!")

        st.write("### Your Details")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("State:", state)
        st.write("Occupation:", occupation)
        st.write("Income:", income)
