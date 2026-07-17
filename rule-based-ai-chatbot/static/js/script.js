const chatMessages = document.getElementById("chat-messages");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const clearChatButton = document.getElementById("clear-chat");
const typingIndicator = document.getElementById("typing-indicator");
const welcomeMessage = "Hello! I'm a Rule-Based AI Chatbot. Type 'help' to see what you can ask me.";

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}-message`;
    message.textContent = text;
    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessage(text) {
    const message = text.trim();
    if (!message) {
        return;
    }

    addMessage(message, "user");
    messageInput.value = "";
    typingIndicator.hidden = false;
    messageInput.focus();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
        const data = await response.json();
        addMessage(data.response || "Sorry, something went wrong. Please try again.", "bot");
    } catch (error) {
        addMessage("Sorry, something went wrong. Please try again.", "bot");
    } finally {
        typingIndicator.hidden = true;
    }
}

chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    sendMessage(messageInput.value);
});

document.querySelectorAll(".quick-question").forEach((button) => {
    button.addEventListener("click", () => sendMessage(button.textContent));
});

clearChatButton.addEventListener("click", () => {
    chatMessages.innerHTML = "";
    addMessage(welcomeMessage, "bot");
    typingIndicator.hidden = true;
    messageInput.value = "";
    messageInput.focus();
});
