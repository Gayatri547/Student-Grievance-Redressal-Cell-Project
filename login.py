import tkinter as tk
from tkinter import messagebox
from dbConnect import DBConnect as db
import os
from UserData import UserDetail as ud

# Create main window
root = tk.Tk()
root.title("Login Page")
conn = db.getDbConnection()

def checkCredentail(uname, pswd):
    try:
        if uname =="admin" and pswd =="12345":
            return True,"admin"
        else:
            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            # SQL query to retrieve data from the table
            sql = "SELECT * FROM credential;"

            # Executing the SQL command
            cursor.execute(sql)

            # Fetching all rows from the result set
            rows = cursor.fetchall()

            for row in rows:
                if uname == row[0] and pswd == row[1]:
                    # Closing the cursor and connection
                    cursor.close()
                    conn.close()
                    return True,row[3]  
            
        return False,""
    except Exception as err:
        print(err)
    

def login():
    username = username_entry.get()
    password = password_entry.get()

    condition,mail = checkCredentail(username, password)
    # Check if username and password match
    if condition and mail=="admin":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()
        os.system("python viewComplain.py") 
    elif condition:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        ud.setUserName(username,mail)
        root.destroy()
        os.system("python raiseComplain.py")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    root.destroy()
    os.system("python reg.py")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, padx=10, pady=5)

# Create registration button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
