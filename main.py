import respones
import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("500x500")

ctk.set_appearance_mode("dark")
def ask():
    respones.Res()

# Title = ctk.CTkLabel(master=app, text="pybot", width=100, height=30, compound="top")
# Title.place()

AskBtn = ctk.CTkButton(master=app, text="Ask", width=100, height=30, command=ask)
AskBtn.place(relx=0.5, rely=0.5, anchor="center")
app.mainloop()

