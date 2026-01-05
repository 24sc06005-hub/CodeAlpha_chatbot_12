import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

class SmartChatbot:
    def __init__(self):
        self.user_name = None
        self.last_intent = None
    
    def detect_intent(self, user_input):
        keywords = {
            "greeting": ["hello", "hi", "hey", "hii"],
            "farewell": ["bye", "goodbye", "exit", "quit"],
            "name": ["my name is", "i am", "call me"],
            "ask_name": ["what is your name", "who are you"],
            "how_are_you": ["how are you", "how's it going"],
            "thanks": ["thanks", "thank you"],
            "joke": ["joke", "funny", "laugh"],
            "time": ["time", "clock", "hour"],
            "help": ["help", "assist", "guide"],
            "weather": ["weather", "temperature", "sunny", "rain"],
            "love": ["love", "like", "affection"],
            "hobby": ["hobby", "like to do", "interests"]
        }
        for intent, words in keywords.items():
            if any(word in user_input for word in words):
                return intent
        return "unknown"

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        intent = self.detect_intent(user_input)
        self.last_intent = intent

        
        if intent == "greeting":
            if self.user_name:
                return f"Hello {self.user_name}! How's your day going?"
            else:
                return random.choice(["Hi there!", "Hello!", "Hey! What's your name?"])
        
        
        if intent == "name":
            name = user_input.split("my name is")[-1].strip().title() or \
                   user_input.split("i am")[-1].strip().title() or \
                   user_input.split("call me")[-1].strip().title()
            self.user_name = name
            return f"Nice to meet you, {self.user_name}!"
        
        
        if intent == "ask_name":
            return "I am SmartChatbot, your virtual assistant!"
        
        
        if intent == "how_are_you":
            return random.choice([
                "I'm good, thanks! How about you?",
                "Feeling great! And you?",
                "I am fine. How's your day?"
            ])
        
        
        if intent == "thanks":
            return random.choice(["You're welcome!", "No problem!", "Anytime!"])
        
        
        if intent == "joke":
            jokes = [
                "Why did the computer show up late? It had a hard drive!",
                "Why did the math book look sad? Too many problems!",
                "I would tell you a joke about UDP… but you might not get it."
            ]
            return random.choice(jokes)
        
        
        if intent == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {now}."
        
        
        if intent == "weather":
            return "I can't check real weather yet, but I hope it's nice outside!"
        
        
        if intent == "love":
            return "Love is amazing! Spread positivity."
        if intent == "hobby":
            return "I enjoy chatting! What hobbies do you like?"
        
        
        if intent == "help":
            return "I can greet you, remember your name, tell jokes, give time, and chat about small talk."

        
        if intent == "farewell":
            if self.user_name:
                return f"Goodbye {self.user_name}! It was nice talking to you!"
            else:
                return "Goodbye! Have a great day!"

        
        if intent == "unknown":
            if self.last_intent == "how_are_you":
                return "I didn't catch that. How are you feeling today?"
            elif self.last_intent == "hobby":
                return "Interesting! Can you tell me more about your hobbies?"
            else:
                return random.choice([
                    "I'm not sure I understand. Can you rephrase?",
                    "Tell me more!",
                    "That's interesting! What else?"
                ])


class ChatGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("SmartChatbot")
        self.master.geometry("600x500")
        self.master.configure(bg="#0f0f0f") 

        
        self.bot = SmartChatbot()

        
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=("Consolas", 12))
        self.chat_area.config(state=tk.DISABLED, bg="#1e1e1e", fg="#00ffea")
        self.chat_area.place(x=10, y=10, width=580, height=400)

        
        self.entry = tk.Entry(master, font=("Consolas", 14), bg="#2e2e2e", fg="#ffffff", insertbackground="white")
        self.entry.place(x=10, y=420, width=480, height=40)
        self.entry.bind("<Return>", self.send_message)

        
        self.send_btn = tk.Button(master, text="Send", command=self.send_message, bg="#00ffea", fg="#000", font=("Consolas", 12))
        self.send_btn.place(x=500, y=420, width=90, height=40)

        
        self.display_message("SmartChatbot: Hello! Type 'bye' to exit.", "bot")

    def display_message(self, message, sender):
        self.chat_area.config(state=tk.NORMAL)
        if sender == "user":
            self.chat_area.insert(tk.END, f"You: {message}\n")
        else:
            self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if user_input == "":
            return
        self.display_message(user_input, "user")
        self.entry.delete(0, tk.END)

        
        response = self.bot.get_response(user_input)
        self.display_message(f"SmartChatbot: {response}", "bot")

        
        if self.bot.detect_intent(user_input) == "farewell":
            self.master.after(2000, self.master.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatGUI(root)
    root.mainloop()