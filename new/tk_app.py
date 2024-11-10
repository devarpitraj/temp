import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_+%-]+@[a-zA-Z.-]+\.[a-zA-z]{2,}$"
    return re.match(pattern, email)

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    
    if not name or not email or not age or gender == "":
        messagebox.showerror("Please, Fill all the fields")
        return
    
    if not validate_email(email):
        messagebox.showerror("Error", "Please, Enter a valid email address")
        return
    
    age = int(age)
    if age <= 0:
        messagebox.showerror("Error", "Age must be a valid positive integer")
        return
    
    if age < 18:
        messagebox.showinfo("UnderAge", "Age must be greater than 18")
        return
    
    messagebox.showinfo("Form Submission", f"Name: {name}\n Email: {email}\n Age: {age}\n Gender: {gender} ")

root = tk.Tk()
root.title("Detail Form")

label_name = tk.Label(root, text='Name:')
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_email = tk.Label(root, text='Email:')
label_email.grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

label_age = tk.Label(root, text='Age:')
label_age.grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

label_gender = tk.Label(root, text='Gender')
label_gender.grid(row=3, column=0)
gender_var = tk.StringVar(value="")
male_button = tk.Radiobutton(root, text='Male', variable = gender_var, value='Male')
male_button.grid(row=3, column=1, padx = 10)
female_button = tk.Radiobutton(root, text='Female', variable = gender_var, value='Female')
female_button.grid(row=3, column=2, padx=10)
others_button = tk.Radiobutton(root, text='Others', variable = gender_var, value='Others')
others_button.grid(row=3, column=3, padx=10)

submit_button = tk.Button(root, text='Submit', command = submit_form, bg='green', fg='white', font=('Arial', 12))
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()