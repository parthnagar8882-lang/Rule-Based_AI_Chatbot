# Rule-Based AI Chatbot

## Project Overview

This is Artificial Intelligence Internship Project 1: a simple web chatbot that answers common questions using predefined rules and decision-making logic.

## Internship Project 1 Objective

Demonstrate control flow, dictionaries, string processing, input sanitization, keyword matching, and continuous chatbot interaction with Python and Flask.

## Features

- Rule-based responses for greetings, help, thanks, and exit messages.
- Answers to basic AI, programming, and project questions.
- Input sanitization for capitalization, punctuation, and extra spaces.
- Friendly fallback response for unknown messages.
- JSON communication between Flask and JavaScript.
- Send button, Enter-key support, quick questions, and Clear Chat.
- Responsive student-level interface.

## How the Rule-Based Chatbot Works

1. JavaScript sends the user's message to Flask at `/chat`.
2. Flask calls `get_response()` in `chatbot.py`.
3. The chatbot sanitizes the text and checks exact commands first.
4. It then checks safe phrases for predefined topics.
5. Flask returns the selected response as JSON for display in the chat window.

## Rule-Based AI Explanation

This chatbot does not use machine learning, external AI APIs, or large language models. It uses explicit rules, dictionaries, if-elif conditions, and basic phrase matching. Its responses are therefore limited to the topics defined in `chatbot.py`.

## Project Workflow

User message → Input sanitization → Rule/phrase matching → Predefined response → JSON response → Chat display

## Project Structure

```text
rule-based-ai-chatbot/
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── templates/index.html
└── static/
    ├── css/style.css
    └── js/script.js
```

## Technologies Used

Python, Flask, HTML5, CSS3, and JavaScript.

## Installation Instructions and How to Run (Windows)

```powershell
cd rule-based-ai-chatbot
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open the address printed in the terminal, usually `http://127.0.0.1:5000`.

## Example Conversations

- `Hello` → A greeting response.
- `What is your name?` → The chatbot introduces itself.
- `What is AI?` → A basic AI explanation.
- `What is Python?` → A Python explanation.
- `Help` → Lists supported topics.
- `Tell me about quantum gravity` → Friendly fallback response.
- `Bye` → Goodbye response without stopping the server.
- `   HELLO!` → Correctly returns a greeting after sanitization.

## Limitations

The chatbot understands only its predefined topics. It cannot learn from users, remember conversations, or answer open-ended questions outside its rules.

## Future Improvements

- Store chatbot rules in a JSON file.
- Add more predefined technical topics.
- Save chat history locally in the browser.
- Add automated unit tests for more response rules.
