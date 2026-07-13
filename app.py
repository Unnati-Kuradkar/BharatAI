from flask import Flask, render_template, request, redirect 
from database.database import (
    create_database,
    save_profile,
    get_latest_profile,
    get_recommended_schemes,
    search_opportunities,
    get_scheme_details
)
app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    profile = get_latest_profile()

    recommendations = []

    if profile:

        recommendations = get_recommended_schemes(
            profile[2],  # age
            profile[4],  # occupation
            profile[5],  # income
            profile[3]   # state
        )

    return render_template(
        "dashboard.html",
        profile=profile,
        recommendations=recommendations
    )

@app.route("/assistant")
def assistant():

    profile = get_latest_profile()

    return render_template(
        "assistant.html",
        profile=profile
    )

@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question", "").lower()

    profile = get_latest_profile()
    if not profile:
        return redirect("/profile")

    name = profile[1]
    age = profile[2]
    state = profile[3]
    occupation = profile[4]
    income = profile[5]

    response = f"""

    Hello {name},

    I analyzed your profile and found suitable information based on:

    👤 Age: {age}
    🌍 State: {state}
    💼 Occupation: {occupation}
    💰 Income: Rs. {income}

    """

    # Smart Question Responses

    if "pm kisan" in question:

        response += """

PM Kisan Scheme

Benefit:
Rs. 6000 yearly support to eligible farmers.

Apply:
https://pmkisan.gov.in/

"""

    elif "scholarship" in question:

        response += """

Top Scholarship Programs

- National Scholarship Portal
- PM YASASVI Scholarship
- Central Sector Scholarship

Apply:
https://scholarships.gov.in

"""

    elif "loan" in question:

        response += """

Popular Government Loan Programs

- PM Mudra Loan
- Kisan Credit Card
- Startup India Funding

"""

    else:

        if occupation.lower() == "student":

            schemes = [
                ("PM Vidyalaxmi Scheme", "#"),
                ("National Scholarship Programs", "#"),
                ("Skill India", "#")
            ]

        elif occupation.lower() == "farmer":

            schemes = [
                ("PM Kisan", "https://pmkisan.gov.in/"),
                ("Kisan Credit Card", "https://www.myscheme.gov.in/"),
                ("Crop Insurance Scheme", "https://pmfby.gov.in/")
            ]

        elif occupation.lower() == "business":

            schemes = [
                ("PM Mudra Loan", "https://www.mudra.org.in/"),
                ("Startup India", "https://www.startupindia.gov.in/"),
                ("MSME Support Schemes", "https://msme.gov.in/")
            ]

        else:

            schemes = [
                ("Ayushman Bharat", "https://pmjay.gov.in/"),
                ("PM Awas Yojana", "https://pmaymis.gov.in/"),
                ("State Government Schemes", "https://www.myscheme.gov.in/")
            ]

        response += "\n\nRecommended:\n\n"

        for scheme, link in schemes:
            response += f'• <a href="{link}" target="_blank">{scheme}</a>\n'

    return render_template(
        "assistant.html",
        answer=response,
        profile=profile
    )

@app.route("/eligibility")
def eligibility():

    profile = get_latest_profile()

    if not profile:
        return redirect("/profile")

    recommendations = get_recommended_schemes(
        profile[2],
        profile[4],
        profile[5],
        profile[3]
    )

    return render_template(
        "eligibility.html",
        recommendations=recommendations
    )

@app.route("/profile", methods=["GET", "POST"])
def profile():

    if request.method == "POST":

        name = request.form["name"]

        age = int(request.form["age"])

        state = request.form["state"]

        occupation = request.form["occupation"]

        income = int(request.form.get("income") or 0)

        print("Name:", name)
        print("Age:", age)
        print("State:", state)
        print("Occupation:", occupation)
        print("Income:", income)

        save_profile(
        name,
        age,
        state,
        occupation,
        income
        )

        recommendations = get_recommended_schemes(
        age,
        occupation,
        income,
        state
        )

        return render_template(
            "success.html",
            recommendations=recommendations
        )

    return render_template("profile.html")


@app.route("/logout")
def logout():

    return redirect("/")

@app.route("/search")
def search():

    keyword = request.args.get("query", "")

    results = search_opportunities(keyword)

    return render_template(
        "search_results.html",
        keyword=keyword,
        results=results
    )

@app.route("/scheme/<name>")
def scheme_detail(name):

    scheme = get_scheme_details(name)

    return render_template(
        "scheme_detail.html",
        scheme=scheme,
        name=name
    )

@app.route("/schemes")
def schemes():
    return render_template("schemes.html")


@app.route("/scholarships")
def scholarships():
    return render_template("scholarships.html")


@app.route("/tenders")
def tenders():
    return render_template("tenders.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501, debug=False)
