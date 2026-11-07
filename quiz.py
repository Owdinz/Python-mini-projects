from logging import root
import tkinter as tk
from tkinter import messagebox, simpledialog

#create main window
root = tk.Tk()
root.withdraw()  # Hide the main window

#consent for this quiz
def open_popup():
    pop_up = tk.Toplevel(root)
    popup.title("Consent Form")
    popup.geometry("400x200")
    tk.Label(popup, text="Please read the following consent form:", wraplength=380).pack(pady=10)
    consent_text = "Consent Form: By participating in this quiz, you agree to receive or to get trashtalked by the AI. You also agree to not hold the developers responsible for any emotional distress caused by the quiz. Do you agree to these terms?"
    tk.label(popup, text=consent_text, wraplength=380).pack(pady=10)
    #if AGREE
    def on_agree():
        popup.destroy()
        messagebox.showinfo("Consent", "Thank you for agreeing to the terms. You may proceed with the quiz.")


#message
messagebox.showinfo("Notification", "Welcome to the Quiz Application!")
#enter user name
user_input = simpledialog.askstring("Name", "Please enter your name: ")
print(f"Hello, {user_input}! Let's get started with the quiz.")
print("What topic do you want to take the quiz on?")
print("1. Math")
print("2. Science")
print("3. History")

#user prompt
user_input = messagebox.askquestion("Question", "Are you ready to start the quiz?")
if user_input == 'yes':
    # Start the quiz
    messagebox.showinfo("Quiz", "Great! Let's begin the quiz.")
else:
    messagebox.showinfo("Quiz", "No worries! You can start the quiz anytime.")
