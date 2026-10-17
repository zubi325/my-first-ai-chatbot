
print("================================")
print("     MY FIRST AI CHATBOT")
print("================================")
print("Hello! I am your chatbot.")
print("Type 'exit' to stop chatting.")
print()

while True:
    user_message = input("You: ").strip().lower()

    if user_message == "exit":
        print("Bot: Goodbye! See you again.")
        break

    elif "hello" in user_message or "hi" in user_message:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_message:
        print("Bot: My name is Zubi AI.")

    elif "how are you" in user_message:
        print("Bot: I am fine! Thanks for asking.")

    elif "help" in user_message:
        print("Bot: Sure! Tell me what you need help with.")

    else:
        print("Bot: I am still learning. Please ask me something simple.")
