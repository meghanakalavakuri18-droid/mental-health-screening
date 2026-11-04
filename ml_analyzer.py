
import os
import joblib

MODEL_FILE = os.path.join(
    "models",
    "mindcare_model.pkl"
)


def analyze_text(user_text):

    if not user_text or len(user_text.strip()) < 10:
        raise ValueError(
            "Please enter at least 10 characters."
        )

    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(
            "AI model not found. Please train the model first."
        )

    model = joblib.load(MODEL_FILE)

    prediction = model.predict([user_text])[0]

    probabilities = model.predict_proba([user_text])[0]
    confidence = max(probabilities) * 100

    descriptions = {
        "everyday": "Your text contains everyday wellbeing language.",
        "stress": "Your text contains language associated with stress.",
        "worry": "Your text contains language associated with worry.",
        "low_mood": "Your text contains language associated with low mood."
    }

    return {
        "category": prediction.replace("_", " ").title(),
        "description": descriptions.get(prediction, "Text analysis completed."),
        "confidence": round(float(confidence), 1)
    }
