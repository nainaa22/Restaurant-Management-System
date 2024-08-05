import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to add employee to the database
def add_employee():
    # Retrieve data from the entry fields
    name = entry_name.get()
    phone_no = entry_phone.get()
    address = entry_address.get()
    role = combo_role.get()
    shift = entry_additional_detail.get() if role in ['cashier', 'waiter'] else 'NIL'
    cuisine = entry_additional_detail.get() if role == 'chef' else 'NIL'

    # Insert data into the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger123",
        database="restaurant"
    )
    cursor = conn.cursor()

    sql = "INSERT INTO employee (name, phone_no, address, role, shift, cuisine) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, phone_no, address, role, shift, cuisine)
    cursor.execute(sql, val)

    conn.commit()
    conn.close()

    # Show success message
    messagebox.showinfo("Success", "Employee added successfully.")

# Tkinter main window
root = tk.Tk()
root.title("Employee Management")

# Labels
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_phone = tk.Label(root, text="Phone No:")
label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_address = tk.Label(root, text="Address:")
label_address.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_role = tk.Label(root, text="Role:")
label_role.grid(row=3, column=0, padx=5, pady=5, sticky="e")
label_additional_detail = tk.Label(root, text="Additional Detail:")
label_additional_detail.grid(row=4, column=0, padx=5, pady=5, sticky="e")

# Entry fields
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=2, column=1, padx=5, pady=5)
combo_role = tk.StringVar(root)
combo_role.set("cashier")
combo_role_menu = tk.OptionMenu(root, combo_role, "cashier", "chef", "waiter")
combo_role_menu.grid(row=3, column=1, padx=5, pady=5)
entry_additional_detail = tk.Entry(root)  # Define entry_additional_detail
entry_additional_detail.grid(row=4, column=1, padx=5, pady=5)

# Function to update additional detail field based on selected role
def update_additional_detail(*args):
    selected_role = combo_role.get()
    if selected_role == "cashier":
        label_additional_detail.config(text="Shift:")
    elif selected_role == "chef":
        label_additional_detail.config(text="Cuisine:")
    elif selected_role == "waiter":
        label_additional_detail.config(text="Shift:")

combo_role.trace('w', update_additional_detail)  # Call update_additional_detail when role selection changes

# Button to add employee
btn_add_employee = tk.Button(root, text="Add Employee", command=add_employee)
btn_add_employee.grid(row=5, columnspan=2, padx=5, pady=10)

root.mainloop()
