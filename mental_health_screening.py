
# Mental Health Screening & Crisis Detection System
# Educational prototype - Not a medical diagnosis tool

def get_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def crisis_support():
    print("\n" + "=" * 50)
    print("          IMMEDIATE SUPPORT REQUIRED")
    print("=" * 50)

    print("Your response indicates a possible immediate safety concern.")
    print("\nPlease take these steps:")
    print("1. Contact a trusted friend or family member now.")
    print("2. Do not stay alone if you may hurt yourself.")
    print("3. Move away from anything you could use to hurt yourself.")
    print("4. If you are in immediate danger, call emergency services.")

    print("\nINDIA SUPPORT RESOURCES")
    print("Emergency: 112")
    print("Tele-MANAS: 14416")
    print("Please seek help from a qualified mental health professional.")
    print("=" * 50)


def screening_questions():
    questions = [
        "Have you been feeling stressed recently?",
        "Have you experienced difficulty sleeping?",
        "Have you been feeling anxious or worried?",
        "Have you lost interest in activities you enjoy?",
        "Have you been feeling tired or lacking energy?",
        "Have you experienced difficulty concentrating?",
        "Have you been feeling lonely or isolated?",
        "Have you been feeling overwhelmed by daily activities?"
    ]

    score = 0

    print("\nMENTAL WELLBEING QUESTIONNAIRE")
    print("Answer based on your experiences over the last 2 weeks.")
    print("\n0 = Never")
    print("1 = Occasionally")
    print("2 = Often")
    print("3 = Almost every day")

    for question in questions:
        while True:
            try:
                answer = int(input("\n" + question + "\nEnter 0-3: "))
                if 0 <= answer <= 3:
                    score += answer
                    break
                else:
                    print("Enter a number between 0 and 3.")
            except ValueError:
                print("Please enter a valid number.")

    return score


def show_results(name, age, score):
    print("\n" + "=" * 50)
    print("             SCREENING REPORT")
    print("=" * 50)

    print("Name:", name)
    print("Age:", age)
    print("Screening Score:", score, "/ 24")

    # Illustrative thresholds for this demo only
    if score <= 8:
        print("Result: Lower reported symptom burden")
        print("Suggestion: Maintain healthy daily routines.")
    elif score <= 16:
        print("Result: Moderate reported symptom burden")
        print("Suggestion: Consider talking to a counsellor.")
    else:
        print("Result: Higher reported symptom burden")
        print("Suggestion: Consider professional mental health support.")

    print("\nIMPORTANT:")
    print("This score is not a diagnosis.")
    print("It does not measure your complete mental health.")
    print("A qualified professional can provide an assessment.")
    print("=" * 50)


def main():
    print("=" * 50)
    print("    MENTAL HEALTH SCREENING SYSTEM")
    print("=" * 50)

    name = input("\nEnter your name: ").strip()

    while not name:
        name = input("Name cannot be empty. Enter your name: ").strip()

    while True:
        try:
            age = int(input("Enter your age: "))
            if 1 <= age <= 120:
                break
            print("Enter a valid age.")
        except ValueError:
            print("Please enter a valid number.")

    print("\nSAFETY CHECK")
    crisis = get_yes_no(
        "Are you thinking about hurting yourself or ending your life?"
    )

    immediate_danger = False

    if crisis:
        immediate_danger = get_yes_no(
            "Do you feel you might act on these thoughts or are you in immediate danger?"
        )

    if immediate_danger:
        crisis_support()
        return

    if crisis:
        print("\nThank you for sharing.")
        print("Please contact someone you trust and seek professional support.")
        print("India Tele-MANAS: 14416 | Emergency: 112")

    score = screening_questions()
    show_results(name, age, score)

    print("\nThank you for using the system.")


if __name__ == "__main__":
    main()
