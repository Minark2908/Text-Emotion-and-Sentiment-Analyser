# music_suggester.py

def get_music_suggestion(emotion_or_sentiment: str) -> dict:
    """
    Returns music suggestion based on emotion or sentiment.

    Parameters:
        emotion_or_sentiment (str): Either emotion (e.g., joy, anger) or sentiment (positive, negative, neutral)

    Returns:
        dict: {'title': ..., 'url': ..., 'description': ...}
    """
    emotion_or_sentiment = emotion_or_sentiment.lower().strip()

    suggestions = {
        "joy": {
            "title": "Happy Vibes - Pharrell Williams",
            "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "description": "An upbeat track to keep your joyful energy flowing!"
        },
        "love": {
            "title": "Perfect - Ed Sheeran",
            "url": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
            "description": "A heartfelt song when you're in love. ❤️"
        },
        "sadness": {
            "title": "Choo Lo - The Local Train",
            "url": "https://open.spotify.com/track/0rlLBWFFTQiOWi963SH9bb?si=7f2aa306ae084eea",
            "description": "A soulful tune to help you feel and heal. 💔"
        },
        "anger": {
            "title": "Lose Yourself - Eminem",
            "url": "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
            "description": "Channel your anger into energy with this powerful track."
        },
        "fear": {
            "title": "Demons - Imagine Dragons",
            "url": "https://www.youtube.com/watch?v=mWRsgZuwf_8",
            "description": "You're not alone. This track gets you."
        },
        "surprise": {
            "title": "Viva La Vida - Coldplay",
            "url": "https://www.youtube.com/watch?v=dvgZkm1xWPE",
            "description": "An unexpected melody for an unexpected feeling."
        },
        "positive": {
            "title": "Illahi - Pritam, Arijit Singh",
            "url": "https://open.spotify.com/track/5cgKosPPj5Cs9a2JQufUc1?si=edce1907cff64432",
            "description": "Keep that positive vibe going strong!"
        },
        "negative": {
            "title": "Agar Tum Saath Ho - Alka Yagnik, Arijit Singh",
            "url": "https://open.spotify.com/track/3hkC9EHFZNQPXrtl8WPHnX?si=a941f19e8ee1481c",
            "description": "Gentle encouragement to lift your spirits."
        },
        "neutral": {
            "title": "Let Her Go - Passenger",
            "url": "https://www.youtube.com/watch?v=RBumgq5yVrA",
            "description": "Relax and reflect with this calm song."
        }
    }

    return suggestions.get(emotion_or_sentiment, {
        "title": "Peaceful Piano Playlist",
        "url": "https://www.youtube.com/watch?v=1ZYbU82GVz4",
        "description": "Relax and reset your mind."
    })
