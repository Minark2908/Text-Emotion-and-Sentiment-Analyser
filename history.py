import os
import pandas as pd
import datetime

HISTORY_FILE = "history.csv"

def init_history():
    if not os.path.exists(HISTORY_FILE):
        df = pd.DataFrame(columns=["Timestamp", "User", "Text", "Prediction", "Confidence", "Mode"])
        df.to_csv(HISTORY_FILE, index=False)

def save_to_history(user_name, text, prediction, confidence, analysis_type):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([{
        "Timestamp": timestamp,
        "User": user_name,
        "Text": text,
        "Prediction": prediction,
        "Confidence": round(confidence, 2),
        "Mode": analysis_type
    }])
    if os.path.exists(HISTORY_FILE) and os.path.getsize(HISTORY_FILE) > 0:
        df = pd.read_csv(HISTORY_FILE)
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry
    df.to_csv(HISTORY_FILE, index=False)

def load_user_history(user_name):
    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        return df[df["User"] == user_name]
    return pd.DataFrame()
