import gspread
import streamlit as st
import datetime
from oauth2client.service_account import ServiceAccountCredentials

# Define scope for Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from Streamlit secrets
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"], scope
)

# Authorize gspread client
client = gspread.authorize(creds)

# Open the Google Sheet
SHEET_NAME = "TonoSense_History"  # Your sheet name
worksheet = client.open(SHEET_NAME).sheet1

# Function to save history to Google Sheet
def save_to_google_sheet(user_name, text, prediction, confidence, analysis_type):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [timestamp, user_name, text, prediction, round(confidence, 2), analysis_type]
    worksheet.append_row(data)
