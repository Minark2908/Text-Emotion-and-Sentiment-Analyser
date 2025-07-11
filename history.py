# utils/history_google.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google Sheets auth
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("tonosense-11aba885f112.json", scope)
client = gspread.authorize(creds)

# Open the sheet (change to your sheet name)
SHEET_NAME = "TonoSense_History"
sheet = client.open(SHEET_NAME).sheet1

def save_to_google_sheet(user_name, text, prediction, confidence, analysis_type):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [now, user_name, text, prediction, round(confidence, 2), analysis_type]
    sheet.append_row(row)
