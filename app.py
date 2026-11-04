
import os
from flask import render_template, request, redirect, url_for
from app_1 import app
from screening import QUESTIONS, calculate_score, get_result, validate_answers
import ml_analyzer

# Application settings
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "mindcare-development-key-change-before-deployment"
)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# QUESTIONNAIRE PAGE
@app.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()

        if not name or not age:
            return render_template(
                "index.html",
                error="Please enter your name and age."
            )

        try:
            age_value = int(age)
            if age_value < 18 or age_value > 120:
                raise ValueError
        except ValueError:
            return render_template(
                "index.html",
                error="Please enter a valid age (18–120)."
            )

        return render_template(
            "questionnaire.html",
            name=name,
            age=age_value,
            questions=QUESTIONS
        )

    return render_template(
        "questionnaire.html",
        questions=QUESTIONS
    )


# SUBMIT SCREENING ANSWERS
@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name", "User").strip() or "User"

    # Check safety questions first
    crisis = request.form.get("crisis")
    immediate_danger = request.form.get("immediate_danger")

    if crisis == "yes" or immediate_danger == "yes":
        return redirect(url_for("support"))

    if crisis not in ("yes", "no") or immediate_danger not in ("yes", "no"):
        return render_template(
            "questionnaire.html",
            questions=QUESTIONS,
            error="Please answer both safety questions."
        )

    # Read questionnaire answers
    try:
        answers = [
            int(request.form.get(f"q{i}", ""))
            for i in range(len(QUESTIONS))
        ]
    except ValueError:
        return render_template(
            "questionnaire.html",
            questions=QUESTIONS,
            error="Please answer all screening questions."
        )

    # Validate answers
    if not validate_answers(answers):
        return render_template(
            "questionnaire.html",
            questions=QUESTIONS,
            error="Invalid answers. Please try again."
        )

    # Calculate screening score
    score = calculate_score(answers)

    # Get result
    result = get_result(score)

    return render_template(
        "results.html",
        name=name,
        score=score,
        result=result
    )


# CRISIS SUPPORT PAGE
@app.route("/support")
def support():
    return render_template("support.html")


# AI TEXT ANALYSIS PAGE
@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    result = None
    error = None

    if request.method == "POST":

        user_text = request.form.get("user_text", "").strip()

        try:
            result = ml_analyzer.analyze_text(user_text)

        except (ValueError, FileNotFoundError) as e:
            error = str(e)

        except Exception:
            app.logger.exception("Text analysis failed")
            error = "Analysis is temporarily unavailable. Please try again."

    return render_template(
        "ml_analysis.html",
        result=result,
        error=error
    )


# ABOUT / HEALTH INFORMATION
@app.route("/about")
def about():
    return render_template("about.html")


# RUN APPLICATION
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
