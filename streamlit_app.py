import streamlit as st

from database.database import (
    create_database,
    save_profile,
    get_latest_profile,
    get_recommended_schemes
)

# Create database and table
create_database()

# Page Config
st.set_page_config(
    page_title="BharatAI",
    layout="wide"
)

# Header
st.title("🇮🇳 BharatAI")
st.subheader("AI Government Opportunities Assistant")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Profile",
        "Dashboard"
    ]
)

# ==========================
# HOME PAGE
# ==========================

if menu == "Home":

    st.markdown("""
    ## Welcome to BharatAI

    Discover:
    - Government Schemes
    - Scholarships
    - Loans
    - Personalized Recommendations
    """)

# ==========================
# PROFILE PAGE
# ==========================

elif menu == "Profile":

    st.header("👤 Create Your Profile")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=18
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
        min_value=0,
        value=0
    )

    if st.button("Save Profile"):

        save_profile(
            name,
            age,
            state,
            occupation,
            income
        )

        st.success("✅ Profile Saved Successfully!")

# ==========================
# DASHBOARD PAGE
# ==========================

elif menu == "Dashboard":

    st.header("📊 Dashboard")

    profile = get_latest_profile()

    if profile:

        st.subheader("Profile Summary")

        st.write(f"**Name:** {profile[1]}")
        st.write(f"**Age:** {profile[2]}")
        st.write(f"**State:** {profile[3]}")
        st.write(f"**Occupation:** {profile[4]}")
        st.write(f"**Income:** ₹{profile[5]}")

        recommendations = get_recommended_schemes(
            profile[2],  # age
            profile[4],  # occupation
            profile[5],  # income
            profile[3]   # state
        )

        st.subheader("🎯 Recommended Schemes")

        for scheme in recommendations:
            st.success(scheme)

    else:
        st.warning("No profile found. Please create a profile first.")
