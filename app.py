import streamlit as st

import pandas as pd
import numpy as np
import altair as alt

import joblib

pipe_lr = joblib.load(open("text_emotion.pkl", "rb"))
sentiment_pipe = joblib.load(open("text_sentiment.pkl", "rb"))


emotions_emoji_dict = {"anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗", "joy": "😂", "neutral": "😐", "sad": "😔",
                       "sadness": "😔", "shame": "😳", "surprise": "😮"}

sentiment_emoji_dict = {
    "Positive": "😊", "Negative": "😞", "Neutral": "😐"
}

def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]


def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

# Sentiment Prediction
def predict_sentiment(docx):
    results = sentiment_pipe.predict([docx])
    return results[0]

def get_sentiment_proba(docx):
    results = sentiment_pipe.predict_proba([docx])
    return results

def main():
    st.title("Text Emotion & Sentiment Analyser")
    st.subheader("Detect Emotions & Sentiments In Text")

    analysis_mode = st.selectbox("Choose Analysis Type", ["Emotion Detection", "Sentiment Analysis"])

    with st.form(key='my_form'):
        raw_text = st.text_area("Enter text here")
        submit_text = st.form_submit_button(label='Analyze')

    if submit_text:
        col1, col2 = st.columns(2)

        if analysis_mode == "Emotion Detection":
            prediction = predict_emotions(raw_text)
            probability = get_prediction_proba(raw_text)
            emoji_icon = emotions_emoji_dict.get(prediction, "")

            with col1:
                st.success("Original Text")
                st.write(raw_text)
                st.success("Predicted Emotion")
                st.write(f"{prediction} {emoji_icon}")
                st.write(f"Confidence: {np.max(probability):.2f}")

            with col2:
                st.success("Prediction Probabilities")
                proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["emotion", "probability"]
                fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotion', y='probability', color='emotion')
                st.altair_chart(fig, use_container_width=True)

        else:  # Sentiment Analysis
            prediction = predict_sentiment(raw_text)
            probability = get_sentiment_proba(raw_text)
            emoji_icon = sentiment_emoji_dict.get(prediction, "")

            with col1:
                st.success("Original Text")
                st.write(raw_text)
                st.success("Predicted Sentiment")
                st.write(f"{prediction} {emoji_icon}")

                # 🎉 Trigger confetti if positive sentiment
                if prediction.lower() == "positive":
                    st.balloons()
                elif prediction.lower() == "negative":
                    st.snow()

                st.write(f"Confidence: {np.max(probability):.2f}")

            with col2:
                st.success("Prediction Probabilities")
                proba_df = pd.DataFrame(probability, columns=sentiment_pipe.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["sentiment", "probability"]
                fig = alt.Chart(proba_df_clean).mark_bar().encode(x='sentiment', y='probability', color='sentiment')
                st.altair_chart(fig, use_container_width=True)
  

if __name__ == '__main__':
    main()