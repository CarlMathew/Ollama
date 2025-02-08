import ollama

def chat_with_bot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": user_input}])
        print("Chatbot:", response["message"]["content"])

if __name__ == "__main__":
    chat_with_bot()
