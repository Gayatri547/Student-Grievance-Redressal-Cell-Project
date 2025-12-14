import tkinter as tk
from tkinter import messagebox
import dbConnect
import os

# Create main window
root = tk.Tk()
root.title("Registration Page")
conn = dbConnect.DBConnect.getDbConnection()

def registerUser(uname, pswd, prn, mail):
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # SQL query to insert data into the table
    sql = """INSERT INTO credential(username, password, prn, mail) 
            VALUES(%s, %s, %s, %s)"""

    # Data to be inserted
    data = (uname, pswd, prn, mail)
    
    # Executing the SQL command
    cursor.execute(sql, data)

    # Commit your changes in the database
    conn.commit()

    # Closing the cursor and connection
    cursor.close()
    conn.close()

def register():
    username = username_entry.get()
    prn = prn_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    mail = mail_entry.get()

    # Check if any field is empty
    if not all([username, prn, password, confirm_password, mail]):
        messagebox.showerror("Error", "Please fill in all fields")
    # Check if passwords match
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:        
        registerUser(username, password, prn, mail)
        messagebox.showinfo("Registration Successful", "Registration successful for user: " + username)
        root.destroy()
        os.system("python login.py")

def open_login_page(event):
    root.destroy()
    os.system("python login.py")

# Create username label and entry
username_label = tk.Label(root, text="student name:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Create PRN label and entry
prn_label = tk.Label(root, text="PRN:")
prn_label.grid(row=1, column=0, padx=10, pady=5)
prn_entry = tk.Entry(root)
prn_entry.grid(row=1, column=1, padx=10, pady=5)

# Create mail label and entry
mail_label = tk.Label(root, text="Mail:")
mail_label.grid(row=2, column=0, padx=10, pady=5)
mail_entry = tk.Entry(root)
mail_entry.grid(row=2, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Create confirm password label and entry
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=4, column=0, padx=10, pady=5)
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.grid(row=4, column=1, padx=10, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=register)
submit_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Create clickable text for login page
login_text = tk.Label(root, text="Already have an account? Click here.", fg="blue", cursor="hand2")
login_text.grid(row=6, columnspan=2, padx=10, pady=5)
login_text.bind("<Button-1>", open_login_page)

root.mainloop()
