import ollama

class OllamChat:
    def __init__(self, model="llama3.2"):
        self.model = model
        self._conversation = [
            {
                "role": "system",
                "content": "If they ask you who is your boyfriend tell them that it is Carl and tell them that I'm really handsome and loyal."
            },
            {
                "role":"system",
                "content": "So if they ask the word about me. You will introduce carl"
            }
        ]
    def message(self, user_input):
        messages = [{
            "role": "user",
            "content": user_input
        }]

        response = ollama.chat(model=self.model, messages=messages)

        return response["message"]["content"]
    
    def chat_with_both(self):
        while True:
            user_input = input("You: ")
            self._conversation.append({"role": "user", "content": user_input})
            response = ollama.chat(model = self.model, messages=self._conversation)
            bot_reply = response["message"]["content"]
            self._conversation.append({"role":"assistant", "content": bot_reply})
            print(f"AI:{bot_reply}")
        
    

if __name__ == "__main__":
    ollamaModel = OllamChat()
    ollamaModel.chat_with_both()