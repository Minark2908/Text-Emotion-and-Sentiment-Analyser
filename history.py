import os
import pandas as pd

HISTORY_FILE = "history.csv"

def init_history():
    if not os.path.exists(HISTORY_FILE):
        df = pd.DataFrame(columns=["user_name", "text", "prediction", "confidence", "analysis_type"])
        df.to_csv(HISTORY_FILE, index=False)

def save_to_history(user_name, text, prediction, confidence, analysis_type):
    new_entry = pd.DataFrame([{
        "user_name": user_name,
        "text": text,
        "prediction": prediction,
        "confidence": confidence,
        "analysis_type": analysis_type
    }])
    df = pd.read_csv(HISTORY_FILE)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)

def load_user_history(user_name):
    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        return df[df["user_name"] == user_name]
    return pd.DataFrame()
