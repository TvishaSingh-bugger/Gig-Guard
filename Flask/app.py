from flask import Flask, render_template, request, redirect, session
import random
import uuid
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

users = {}
user_store = {}

# -----------------------------
# DATA
# -----------------------------
def get_data(city="Meerut"):
    api_key = "73b28d4bb97c4abbb0f53318260404"

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"

    try:
        res = requests.get(url)
        data = res.json()

        temp = data["current"]["temp_c"]
        rain = data["current"]["precip_mm"]
        condition = data["current"]["condition"]["text"]

        # AQI (PM2.5 used as approximation)
        aqi = data["current"].get("air_quality", {}).get("pm2_5", 150)

        return {
            "temp": int(temp),
            "rain": int(rain),
            "aqi": int(aqi),
            "condition": condition
        }

    except Exception as e:
        print("API Error:", e)

        # fallback safety (VERY IMPORTANT)
        return {
            "temp": 30,
            "rain": 0,
            "aqi": 150,
            "condition": "Unknown"
        }
# -----------------------------
# AGE
# -----------------------------
def calculate_age(dob):
    birth = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birth.year

def calculate_risk(user, data):
    score = 0

    # Category risk
    if user["category"] == "Quick Commerce":
        score += 25
    elif user["category"] == "Food Delivery":
        score += 15
    elif user["category"] == "Logistics":
        score += 18
    else:
        score += 10

    # Age risk
    if user["age"] < 21:
        score += 10
    elif user["age"] > 40:
        score += 5

    # Environmental risk
    if data["aqi"] > 300:
        score += 25
    elif data["aqi"] > 200:
        score += 15

    if data["rain"] > 60:
        score += 20
    elif data["rain"] > 30:
        score += 10

    if data["temp"] > 40:
        score += 15

    # Past claims risk
    score += user["claims"] * 5

    return min(score, 100)

# -----------------------------
# PREMIUM
# -----------------------------
def calculate_premium(user, risk_score):
    base = 20
    premium = base + int(risk_score * 0.6)
    return premium

def get_risk_level(score):
    if score < 30:
        return "LOW"
    elif score < 70:
        return "MEDIUM"
    else:
        return "HIGH"
# -----------------------------
# TRIGGER
# -----------------------------
def check_trigger(data):
    if data["aqi"] > 300:
        return "High Pollution"

    if data["rain"] > 20 or "rain" in data["condition"].lower():
        return "Heavy Rain"

    if data["temp"] > 40:
        return "Extreme Heat"

    return None

# -----------------------------
# PAYOUT
# -----------------------------
def calculate_payout(user):
    return 800 if user["plan"] == "Premium" else 400

# -----------------------------
# ROUTES
# -----------------------------

@app.route("/")
def home():
    return redirect("/login")

# -----------------------------
# REGISTER
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        dob = request.form["dob"]

        category = request.form["category"]
        custom_category = request.form.get("custom_category")

        company = request.form["company"]
        other_company = request.form.get("other_company")

        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            error = "Passwords do not match"
        elif username in users:
            error = "User already exists"
        else:
            age = calculate_age(dob)

            final_category = custom_category if category == "Other" else category
            final_company = other_company if company == "Other" else company

            users[username] = password

            user_store[username] = {
                "age": age,
                "category": final_category,
                "company": final_company,
                "policy_id": "POL" + str(uuid.uuid4())[:6],
                "plan": "Basic",
                "claims": 0,
                "history": []
            }

            return redirect("/login")

    return render_template("register.html", error=error)

# -----------------------------
# LOGIN
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        if u in users and users[u] == p:
            session["user"] = u
            return redirect("/dashboard")
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)

# -----------------------------
# DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    user = user_store[session["user"]]
    data = get_data()

    risk_score = calculate_risk(user, data)
    risk_level = get_risk_level(risk_score)
    premium = calculate_premium(user, risk_score)

    return render_template(
        "dashboard.html",
        user=user,
        data=data,
        premium=premium,
        risk=risk_score,
        risk_level=risk_level
    )

# -----------------------------
# PLAN
# -----------------------------
@app.route("/select-plan", methods=["POST"])
def select_plan():
    user_store[session["user"]]["plan"] = request.form["plan"]
    return redirect("/dashboard")

# -----------------------------
# CLAIM
# -----------------------------
@app.route("/simulate")
def simulate():
    user = user_store[session["user"]]
    data = get_data()

    trigger = check_trigger(data)

    if trigger:
        amount = calculate_payout(user)
        result = f"{trigger} → ₹{amount}"
        user["claims"] += 1
    else:
        result = "No disruption"

    user["history"].append(result)
    return redirect("/dashboard")

# -----------------------------
# LOGOUT
# -----------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)