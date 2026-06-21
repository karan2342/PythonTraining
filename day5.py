import re

responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm not sure I understand. Could you please rephrase?"
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]

    return responses["default"]
  

def chatbot():
    print("Chatbot: Hello! I'm here to assist you. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!!")
            break

        response = chatbot_response(user_input)

        print(f"Chatbot: {response}")

chatbot()