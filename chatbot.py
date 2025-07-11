# chatbot.py

def get_chatbot_response(emotion: str, user_message: str) -> str:
    """
    Generate an empathetic chatbot response based on emotion.

    Parameters:
        emotion (str): Detected emotion (e.g., 'joy', 'sadness', etc.)
        user_message (str): User's message input

    Returns:
        str: Bot's emotionally relevant reply
    """
    emotion = emotion.lower().strip()

    responses = {
        "joy": [
            "That's amazing! 😊 Tell me what made you so happy!",
            "I love seeing joy like this! 💫 Keep spreading smiles!"
        ],
        "sadness": [
            "I'm really sorry you're feeling this way. 😔 I'm here for you.",
            "It's okay to feel sad sometimes. Want to talk about it?"
        ],
        "anger": [
            "Take a deep breath. Let's cool down together. 😤",
            "Anger is powerful — let's channel it into something positive!"
        ],
        "fear": [
            "You're not alone. It's okay to be scared sometimes. 🧸",
            "Fear means you're facing something important. I'm proud of you!"
        ],
        "love": [
            "That's beautiful. 💖 Tell me more about what you're feeling.",
            "Love is what makes the world go round. 😊"
        ],
        "surprise": [
            "Whoa! That sounds unexpected! 😲",
            "Surprises keep life exciting. What happened?"
        ]
    }

    fallback_response = "I'm here for you, anytime you want to talk. 😊"

    emotion_responses = responses.get(emotion, [fallback_response])
    
    # Pick a response based on user input length (just for variation)
    index = len(user_message) % len(emotion_responses)
    return emotion_responses[index]
