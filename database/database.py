import sqlite3

def create_database():

    conn = sqlite3.connect("database/users.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        age INTEGER,
        state TEXT,
        occupation TEXT,
        income INTEGER

    )
    """)

    conn.commit()
    conn.close()


def save_profile(name, age, state, occupation, income):

    conn = sqlite3.connect("database/users.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO profiles
    (name, age, state, occupation, income)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, state, occupation, income))

    conn.commit()
    conn.close()

# ==========================================
# AI Scheme Recommendation Function
# ==========================================

def get_recommended_schemes(age, occupation, income, state):

    recommendations = []

    occupation = occupation.lower()
    state = state.lower()

    if occupation == "student":
        recommendations.append("PM Vidyalaxmi Scheme")
        recommendations.append("National Scholarship Portal")
        recommendations.append("PM YASASVI Scholarship")
        recommendations.append("Central Sector Scholarship")

    elif occupation in ["business", "entrepreneur"]:
        recommendations.append("PM Mudra Loan")
        recommendations.append("Startup India")
        recommendations.append("Stand-Up India")

    elif occupation == "farmer":
        recommendations.append("PM Kisan")
        recommendations.append("Kisan Credit Card")
        recommendations.append("Crop Insurance Scheme")

    if income < 300000:
        recommendations.append("Ayushman Bharat")
        recommendations.append("PM Awas Yojana")
        recommendations.append("EWS Benefits")

    if age < 25:
        recommendations.append("Skill India")
        recommendations.append("Digital India Training")

    # State Specific Recommendations

    if state == "maharashtra":
        recommendations.append("Maharashtra Farmer Welfare Scheme")
        recommendations.append("MahaDBT Scholarship")

    elif state == "karnataka":
        recommendations.append("Raitha Siri Scheme")
        recommendations.append("Karnataka Scholarship Portal")

    elif state == "gujarat":
        recommendations.append("Mukhyamantri Yuva Swavalamban Yojana")

    elif state == "uttar pradesh":
        recommendations.append("UP Scholarship Scheme")

    elif state == "jharkhand":
        recommendations.append("Jharkhand State Scholarship")

    elif state == "madhya pradesh":
        recommendations.append("Mukhyamantri Medhavi Vidyarthi Yojana")

    elif state == "rajasthan":
        recommendations.append("Rajasthan Scholarship Portal")

    return list(set(recommendations))


def get_latest_profile():

    conn = sqlite3.connect("database/users.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM profiles
    ORDER BY id DESC
    LIMIT 1
    """)

    profile = cursor.fetchone()

    conn.close()

    return profile

def search_opportunities(keyword):

    data = [

    {
    "name": "PM Kisan",
    "type": "Scheme",
    "description": "Financial support for farmers"
    },

    {
    "name": "Kisan Credit Card",
    "type": "Loan",
    "description": "Agricultural credit support for farmers"
    },

    {
    "name": "Crop Insurance Scheme",
    "type": "Scheme",
    "description": "Protection against crop losses"
    },

    {
    "name": "PM Vidyalaxmi Scheme",
    "type": "Education",
    "description": "Education loan support for students"
    },

    {
    "name": "National Scholarship Portal",
    "type": "Scholarship",
    "description": "Central government scholarships"
    },

    {
    "name": "PM Mudra Loan",
    "type": "Loan",
    "description": "Business loan support for entrepreneurs"
    },

    {
    "name": "Startup India",
    "type": "Startup",
    "description": "Funding and support for startups"
    },

    {
    "name": "Ayushman Bharat",
    "type": "Health Scheme",
    "description": "Health insurance support"
    },

    {
    "name": "Skill India",
    "type": "Training",
    "description": "Skill development programs for youth"
    },

    {
    "name": "MahaDBT Scholarship",
    "type": "Scholarship",
    "description": "Maharashtra student financial support"
    }

    ]

    results = []

    keyword = keyword.lower()

    for item in data:

        if (
            keyword in item["name"].lower()
            or keyword in item["type"].lower()
            or keyword in item["description"].lower()
        ):
            results.append(item)

    return results

def get_scheme_details(name):

    schemes = {

        "PM Kisan": {
            "benefit": "₹6000 per year financial support",
            "eligibility": "All eligible farmers",
            "website": "https://pmkisan.gov.in"
        },

        "Kisan Credit Card": {
            "benefit": "Low-interest agricultural loans",
            "eligibility": "Farmers",
            "website": "https://www.myscheme.gov.in"
        },

        "Crop Insurance Scheme": {
            "benefit": "Crop loss protection",
            "eligibility": "Farmers",
            "website": "https://pmfby.gov.in"
        },

        "Skill India": {
            "benefit": "Free skill training",
            "eligibility": "Youth",
            "website": "https://www.skillindia.gov.in"
        },

        "Digital India Training": {
            "benefit": "Digital skills and computer training",
            "eligibility": "Students and Youth",
            "website": "https://www.skillindia.gov.in"
        },

        "MahaDBT Scholarship": {
            "benefit": "Financial support for higher education",
            "eligibility": "Eligible Maharashtra students",
            "website": "https://mahadbt.maharashtra.gov.in"
        },

        "Maharashtra Farmer Welfare Scheme": {
            "benefit": "Financial assistance and welfare support",
            "eligibility": "Farmers of Maharashtra",
            "website": "https://www.maharashtra.gov.in"
        },

        "PM Vidyalaxmi Scheme": {
            "benefit": "Education loan assistance",
            "eligibility": "Students",
            "website": "https://www.vidyalakshmi.co.in"
        },

        "National Scholarship Portal": {
            "benefit": "Government scholarships",
            "eligibility": "Eligible students",
            "website": "https://scholarships.gov.in"
        }

    }

    return schemes.get(name)
