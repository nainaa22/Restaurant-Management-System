import tkinter as tk
from tkinter.font import Font
import subprocess

# Function to open bill file
def open_bill():
    subprocess.Popen(["python", "C:\\Users\\Admin\\python\\bill_restaur.py"])

# Function to open branch file
def open_branch():
    subprocess.Popen(["python", "C:\\Users\\Admin\\python\\restaurant_manage.py"])

# Function to open employee file
def open_employee():
    subprocess.Popen(["python", "C:\\Users\\Admin\\python\\res_employee.py"])

# Function to exit the program
def exit_program():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("500x400")  # Set window size

# Define button font
button_font = Font(family="Arial", size=14, weight="bold")

# Create label for title
title_label = tk.Label(root, text="RESTAURANT MANAGEMENT SYSTEM", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Define button colors

button_fg = "white"

# Create buttons
btn_bill = tk.Button(root, text="Bill", command=open_bill, font=button_font, width=20, height=2, bg="yellow", fg=button_fg)
btn_bill.pack(pady=10)

btn_branch = tk.Button(root, text="Branch", command=open_branch, font=button_font, width=20, height=2, bg="red", fg=button_fg)
btn_branch.pack(pady=10)

btn_employee = tk.Button(root, text="Employee", command=open_employee, font=button_font, width=20, height=2, bg="green", fg=button_fg)
btn_employee.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=exit_program, font=button_font, width=20, height=2, bg="blue", fg=button_fg)
btn_exit.pack(pady=10)

root.mainloop()