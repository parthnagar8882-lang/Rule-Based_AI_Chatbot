"""Predefined response rules for the Rule-Based AI Chatbot."""

import re


EXACT_RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I help you with?",
    "hey": "Hey! How can I assist you?",
    "good morning": "Good morning! How can I help you today?",
    "good afternoon": "Good afternoon! What would you like to know?",
    "good evening": "Good evening! How can I assist you?",
    "help": "You can ask me about my purpose, how I work, AI, programming, this project, or say hello to start a conversation.",
    "thanks": "You're welcome! Happy to help.",
    "thank you": "You're welcome! Happy to help.",
    "thank you so much": "You're very welcome! Happy to help.",
    "bye": "Goodbye! Have a great day.",
    "goodbye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Have a great day.",
    "quit": "Goodbye! Have a great day.",
    "see you": "See you later! Have a great day.",
}

EXIT_COMMANDS = {"bye", "goodbye", "exit", "quit", "see you"}
FALLBACK_RESPONSE = (
    "Sorry, I don't understand that yet. Try asking about AI, programming, "
    "this project, or type 'help' to see what I can answer."
)


def sanitize_input(message):
    """Normalize user text so capitalization, punctuation, and extra spaces do not affect rules."""
    if not isinstance(message, str):
        return ""
    cleaned_message = message.strip().lower()
    cleaned_message = re.sub(r"[^a-z0-9\s]", " ", cleaned_message)
    return re.sub(r"\s+", " ", cleaned_message).strip()


def has_phrase(message, phrase):
    """Check complete words/phrases without unsafe substring matching."""
    return re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", message) is not None


def get_response(message):
    """Return a predefined chatbot response and whether the message was an exit command."""
    cleaned_message = sanitize_input(message)

    if not cleaned_message:
        return "Please type a message before sending.", False

    # Exact matches have priority because they are the clearest user commands.
    if cleaned_message in EXACT_RESPONSES:
        return EXACT_RESPONSES[cleaned_message], cleaned_message in EXIT_COMMANDS

    # Bot information and project information.
    if any(has_phrase(cleaned_message, phrase) for phrase in ["what is your name", "who are you", "your name"]):
        return "I'm a Rule-Based AI Chatbot created as part of an Artificial Intelligence internship project.", False
    if any(has_phrase(cleaned_message, phrase) for phrase in ["what can you do", "your purpose", "what is your purpose"]):
        return "I can answer predefined questions about AI, programming, and this internship project using rule-based logic.", False
    if any(has_phrase(cleaned_message, phrase) for phrase in ["how do you work", "how you work"]):
        return "I use predefined rules, keyword matching, and decision-making logic to provide a suitable response.", False
    if any(has_phrase(cleaned_message, phrase) for phrase in ["what is this project", "rule based chatbot", "internship project 1"]):
        return "This is Internship Project 1: a Rule-Based AI Chatbot built with Python and Flask.", False

    # AI concepts.
    if has_phrase(cleaned_message, "artificial intelligence") or has_phrase(cleaned_message, "what is ai"):
        return "Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks that normally require human intelligence.", False
    if has_phrase(cleaned_message, "machine learning"):
        return "Machine Learning is a part of AI where computers learn patterns from data to make predictions or decisions.", False
    if has_phrase(cleaned_message, "deep learning"):
        return "Deep Learning is a type of Machine Learning that uses layered neural networks to learn complex patterns.", False
    if has_phrase(cleaned_message, "what is chatbot") or has_phrase(cleaned_message, "what is a chatbot"):
        return "A chatbot is a program that communicates with users through text or voice to answer questions or provide assistance.", False

    # Programming and web technologies.
    technology_responses = {
        "what is python": "Python is a beginner-friendly programming language used for web development, automation, data analysis, and AI projects.",
        "what is flask": "Flask is a lightweight Python web framework used to build web applications and APIs.",
        "what is html": "HTML is the standard markup language used to structure content on web pages.",
        "what is css": "CSS is used to style HTML pages by controlling colors, spacing, fonts, and layout.",
        "what is javascript": "JavaScript is a programming language used to add interactivity and dynamic behavior to web pages.",
    }
    for phrase, response in technology_responses.items():
        if has_phrase(cleaned_message, phrase):
            return response, False

    if any(has_phrase(cleaned_message, phrase) for phrase in ["what can i ask", "commands", "can you help"]):
        return "Try asking: What is AI?, What is Python?, How do you work?, What is this project?, or type goodbye.", False

    return FALLBACK_RESPONSE, False
