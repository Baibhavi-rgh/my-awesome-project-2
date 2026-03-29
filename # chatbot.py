# chatbot.py

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I am your Digital Help Assistant. How can I help you?"

    # Email help
    elif "email" in user_input:
        return "To send an email: Open Gmail → Click Compose → Enter receiver email → Write message → Click Send."

    # Password help
    elif "password" in user_input:
        return "A strong password includes uppercase, lowercase, numbers, and symbols. Example: Abc@1234"

    # OTP safety
    elif "otp" in user_input:
        return "⚠️ Never share your OTP with anyone."

    # Internet basics
    elif "internet" in user_input:
        return "The internet is a global network connecting millions of computers."

    # Phishing / scam
    elif "phishing" in user_input or "scam" in user_input:
        return "Phishing is a fraud attempt to steal your data. Avoid unknown links and emails."

    # Browser help
    elif "browser" in user_input:
        return "A browser is used to access websites. Examples: Chrome, Edge, Firefox."

    # Digital payment safety
    elif "upi" in user_input or "payment" in user_input:
        return "Always verify receiver details before payment. Never share OTP or PIN."

    # Default response
    else:
        return "Sorry 😔 I didn't understand. Try asking about email, password, internet, or safety."