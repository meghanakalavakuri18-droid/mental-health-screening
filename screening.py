
# Mental Health Screening & Crisis Detection
# Screening questions and score calculation

QUESTIONS = [
    "Have you been feeling stressed recently?",
    "Have you experienced difficulty sleeping?",
    "Have you been feeling anxious or worried?",
    "Have you lost interest in activities you enjoy?",
    "Have you been feeling tired or lacking energy?",
    "Have you experienced difficulty concentrating?",
    "Have you been feeling lonely or isolated?",
    "Have you been feeling overwhelmed by daily activities?"
]


# Calculate total screening score
def calculate_score(answers):
    return sum(answers)


# Generate screening result
def get_result(score):

    if score <= 8:
        return {
            "level": "Lower reported symptom burden",
            "message": (
                "Continue healthy daily routines, "
                "sleep well and practice self-care."
            )
        }

    elif score <= 16:
        return {
            "level": "Moderate reported symptom burden",
            "message": (
                "Consider talking to a counsellor "
                "or qualified mental health professional."
            )
        }

    else:
        return {
            "level": "Higher reported symptom burden",
            "message": (
                "Consider seeking support from a "
                "qualified mental health professional."
            )
        }


# Validate user answers
def validate_answers(answers):

    if len(answers) != len(QUESTIONS):
        return False

    return all(
        isinstance(answer, int) and 0 <= answer <= 3
        for answer in answers
    )
