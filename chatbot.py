"""
Ultra AI Chatbot Assistant
Author: Your Name
Date: 2026-03-26
Description: Modern AI Chatbot GUI with dark theme, clickable suggestions,
             and expandable responses.
"""

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# ------------------- Responses and Suggestions -------------------
responses = {
    "hello": "Hi there! 😊",
    "hi": "Hello! How can I help you today? 😎",
    "how are you": "I'm fine, thanks! How about you? 🤖",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus! 😂",
    "what time is it": lambda: f"Current time is {datetime.now().strftime('%H:%M:%S')}",
    "bye": "Goodbye! Have a great day! 👋",
}

suggestions = ["hello", "tell me a joke", "what time is it", "how are you", "bye"]

# ------------------- Chatbot Logic -------------------
def get_response(msg):
    """Return bot response and exit flag for 'bye'."""
    msg = msg.lower().strip()
    if msg in responses:
        reply = responses[msg]
        if callable(reply):
            reply = reply()
        return reply, msg == "bye"
    return "Sorry, I didn’t understand that. 😅", False

# ------------------- GUI Logic -------------------
def send(msg=None):
    """Send user message and display bot reply."""
    user_msg = msg or user_entry.get()
    if not user_msg.strip(): return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_msg}\n", "user")

    reply, exit_flag = get_response(user_msg)
    chat_area.insert(tk.END, f"Bot: {reply}\n\n", "bot")
    chat_area.see(tk.END)
    chat_area.config(state='disabled')
    user_entry.delete(0, tk.END)

    if exit_flag:
        root.after(500, root.destroy)

# ------------------- GUI Setup -------------------
root = tk.Tk()
root.title("🌌 Ultra AI Chatbot Assistant")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Dark background

# Chat Display Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled',
                                      font=("Helvetica",12), bg="#2b2b2b", fg="#ffffff", insertbackground="#ffffff")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_config("user", foreground="#00ff00")
chat_area.tag_config("bot", foreground="#00ffff")

# User Input
user_entry = tk.Entry(root, font=("Helvetica",12), bg="#2b2b2b", fg="#ffffff", insertbackground="#ffffff")
user_entry.pack(padx=10, pady=5, fill=tk.X)
user_entry.bind("<Return>", lambda e: send())

# Send Button
tk.Button(root, text="Send", font=("Helvetica",12,"bold"), bg="#4CAF50", fg="#fff", command=send)\
    .pack(padx=10, pady=5)

# Suggestion Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=5)
for s in suggestions:
    tk.Button(btn_frame, text=s.capitalize(), font=("Helvetica",10,"bold"),
              bg="#3a3a3a", fg="#fff", command=lambda x=s: send(x))\
        .pack(side=tk.LEFT, padx=3, pady=3)

# Welcome message
chat_area.config(state='normal')
chat_area.insert(tk.END, "Bot: Hello! Click a suggestion or type your message below.\n\n", "bot")
chat_area.config(state='disabled')

root.mainloop()