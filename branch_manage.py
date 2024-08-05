import tkinter as tk
from tkinter import messagebox
import mysql.connector

def insert_branch_details():
    try:
        # Retrieve store details from the input fields
        b_name= name_entry.get()
        branch_id = b_id_entry.get()
        email_id_val = email_id_entry.get()
        GST_no_val = gst_no_entry.get()
        manager_n=n.get()
        phone_no=phone.get()

        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user=" root",
            password="tiger123",
            database="restaurant"
        )
        cursor = conn.cursor()

        # Execute SQL command to insert store details into the database
        sql = "INSERT INTO branch(branch_name, branch_id, email_id, GST_no,manager_name,phone_no) VALUES (%s,%s,%s, %s, %s, %s)"
        values = (b_name,branch_id,email_id_val, GST_no_val, manager_n,phone_no)
        cursor.execute(sql, values)

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Branch details inserted successfully.")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Restaurant Management System")

# Create labels and entry fields for store details
name_label = tk.Label(root, text="Branch Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

branch_label = tk.Label(root, text="Branch Id:")
branch_label.grid(row=1, column=0, padx=10, pady=5)
b_id_entry= tk.Entry(root)
b_id_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email Id:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_id_entry = tk.Entry(root)
email_id_entry.grid(row=2, column=1, padx=10, pady=5)

GST_no_label = tk.Label(root, text="GST No:")
GST_no_label.grid(row=3, column=0, padx=10, pady=5)
gst_no_entry = tk.Entry(root)
gst_no_entry.grid(row=3, column=1, padx=10, pady=5)

manager_label = tk.Label(root, text="Manager Name:")
manager_label.grid(row=4, column=0, padx=10, pady=5)
n= tk.Entry(root)
n.grid(row=4, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone No:")
phone_label.grid(row=5, column=0, padx=10, pady=5)
phone= tk.Entry(root)
phone.grid(row=5, column=1, padx=10, pady=5)



# Create a button to insert store details
insert_button = tk.Button(root, text="Insert Branch details", command=insert_branch_details)
insert_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display instructions
instructions_label = tk.Label(root, text="Enter branch details and click 'Insert Branch details' to store in the database.")
instructions_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()