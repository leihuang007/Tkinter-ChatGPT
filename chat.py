from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
root.iconbitmap('ai_lt.ico')  # https://tkinter.com/ai_lt.ico

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add Text Widget To Get ChatGPT Responses
my_text = Text(text_frame,
               bg="#343638",
               width=65,
               bd=1,
               fg="#d6d6d6",
               relief="flat",
               wrap=WORD,
               selectbackground="#1f538d")
my_text.grid(row=0, column=0)
root.mainloop()
