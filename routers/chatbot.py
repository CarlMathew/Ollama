import ollama
import csv
import os
class OllamaChat:
    def __init__(self, model="llama3.2"):
        self.model = model
        self.filename = "conversation.csv"
        self.file_exists = os.path.isfile(self.filename)
        self.fields = ["role", "content"]
        self._conversation = [
            {
                "role": "system",
                "content": "Now you will act as a Carl. and you will be name as Carl So basically that's me. I'm going to introduce you myself."
            },
            {
                "role":"system",
                "content": "I'm Carl and I'm 24 years old. I live in Cabuyao Laguna. I don't have any siblings and I already have a bachelor degree in Computer Engineering"
            }
        ]
    def message(self, user_input):
        mode = ""

        if self.file_exists:
            mode = "a"
            converstaion = self.read_message()
            new_data = []
            input_data = {
                "role": "user",
                "content": user_input
            }
            converstaion.append(input_data)
            new_data.append(input_data)
            response = ollama.chat(model = self.model, messages=converstaion)
            bot_reply = response["message"]["content"]
            output_data = {
                "role": "assistant",
                "content": bot_reply
            }
            new_data.append(output_data)
            self.write_message(mode, new_data)


        elif not self.file_exists:
            mode = "w"
            new_data = [i for i in self._conversation] 
            input_data = {
                "role": "user",
                "content": user_input
            }

            new_data.append(input_data)
            response = ollama.chat(model = self.model, messages=new_data)
            bot_reply = response["message"]["content"]
            output_data = {
                "role": "assistant",
                "content": bot_reply
            }
            new_data.append(output_data)
            self.write_message(mode, new_data)

        return bot_reply, new_data, output_data



    def read_message(self):
        conversation = []
        if self.file_exists:
            with open(self.filename, "r") as file:
                csvFile = csv.reader(file)
                
                for index, lines in enumerate(csvFile):
                    if lines and index != 0:
                        conversation.append(dict(zip(self.fields, lines)))
            return conversation
        
    def write_message(self, mode, data):
        with open(self.filename, mode) as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.fields)

            if not self.file_exists:
                writer.writeheader()
            
            writer.writerows(data)

    def removeFile(self):
        os.remove(self.filename)

    def chat_with_both(self):
        while True:
            user_input = input("You: ")
            self._conversation.append({"role": "user", "content": user_input})
            response = ollama.chat(model = self.model, messages=self._conversation)
            bot_reply = response["message"]["content"]
            self._conversation.append({"role":"assistant", "content": bot_reply})
            print(f"AI:{bot_reply}")




    