from tkinter import *
import customtkinter
import openai
import os
import pickle

_api_window_hide = '600x500'
_api_window_show = '600x650'

# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry(_api_window_hide)
root.iconbitmap('ai_lt.ico')  # https://tkinter.com/ai_lt.ico

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Submit to ChatGPT
def speak():
    pass

# Clear The Screens
def clear():
    pass

# Do API stuff
def key():
    # Resize App Larger
    root.geometry(_api_window_show)
    # Reshow API Frame
    api_frame.pack(pady=30)

# Save API Key
def save_key():
    # Hide API Frame
    api_frame.pack_forget()
    # Resize App Smaller
    root.geometry(_api_window_hide)

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

# Create Scrollbar from text widget
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")


# Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

# Entry Widget To Type Stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(root, placeholder_text="Type Something To ChatGPT...",
                                    width=535, height=50, border_width=1)
chat_entry.pack(pady=10)

# Create Buttom Frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Create Submit Button
submit_button = customtkinter.CTkButton(button_frame, text="Speak To ChatGPT", command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create Clear Button
clear_button = customtkinter.CTkButton(button_frame, text="Clear Response", command=clear)
clear_button.grid(row=0, column=1, padx=35)

# Create API Button
api_button = customtkinter.CTkButton(button_frame, text="Update API Key", command=key)
api_button.grid(row=0, column=2, padx=25)

# Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
# api_frame.pack(pady=30)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame, placeholder_text="Enter Your API Key...", width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

# Add API Button
api_save_button = customtkinter.CTkButton(api_frame, text="Save Key", command=save_key)
api_save_button.grid(row=0, column=1, padx=10)



root.mainloop()
