import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from dbConnect import DBConnect as db
from UserData import UserDetail as ud
import os

complainType = ['All', 'Infrastructure', 'Academic', 'Administration', 'Campus Life', 'Faculty and Staff','Old Complaints']

# Function to retrieve data from the database
def retrieve_data(complaint_type="All"):
    try:
        # Connect to the database
        conn = db.getDbConnection()
        cursor = conn.cursor()

        # Construct SQL query based on complaint type
        if complaint_type == "All":
            cursor.execute("SELECT * FROM complaints WHERE track=%s", ("In_progress",))
        elif complaint_type == "Old Complaints":
            cursor.execute("SELECT * FROM complaints")
        else:
            cursor.execute("SELECT * FROM complaints WHERE complaint_type = %s and track=%s", (complaint_type,"In_progress"))

        data = cursor.fetchall()

        # Close connection
        conn.close()

        return data
    except Exception as e:
        print(f"Failed to retrieve data: {e}")

# Function to handle accepting a complaint
def accept_complaint():
    # Get the selected complaint ID
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        complaint_id = item["values"][0]  # Assuming the complaint ID is in the first column
        # Perform the action for accepting the complaint
        # Update the status in the database for the selected complaint_id
        # Reload the data in the Treeview
        updateComplaint(complaint_id,"Accepted")
        selected_type = combobox.get()
        data = retrieve_data(selected_type)
        reload_data(data)

# Function to handle declining a complaint
def decline_complaint():
    # Get the selected complaint ID
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        complaint_id = item["values"][0]  # Assuming the complaint ID is in the first column
        # Perform the action for declining the complaint
        # Update the status in the database for the selected complaint_id
        # Reload the data in the Treeview
        updateComplaint(complaint_id,"Rejected")

        selected_type = combobox.get()
        data = retrieve_data(selected_type)
        reload_data(data)

# Function to update table content based on selected complaint type
def update_table(event):
    selected_type = combobox.get()
    data = retrieve_data(selected_type)
    reload_data(data)

# Function to reload data in the Treeview
def reload_data(data):
    tree.delete(*tree.get_children())  # Clear existing data
    for row in data:
        tree.insert("", "end", values=[row[6],row[0],row[1],row[2],row[4],row[5]])

def updateComplaint(complaint_id,status):
    print(complaint_id)
    print(status)
    try:
        # Connect to the database
        conn = db.getDbConnection()
        cursor = conn.cursor()
        
        # Execute the DELETE query
        cursor.execute("UPDATE complaints SET track=%s WHERE id = %s", (status, complaint_id))
        
        # Commit the transaction
        conn.commit()
        
        # Close connection
        conn.close()
        
        messagebox.showinfo("Success", "Complaint deleted successfully!")
        
        # Reload data in the Treeview
        selected_type = combobox.get()
        data = retrieve_data(selected_type)
        reload_data(data)
    except Exception as e:
        print(f"Failed to delete complaint: {e}")
        messagebox.showerror("Error", "Failed to delete complaint")


# Create main window
root = tk.Tk()
root.title("Table View")

# Create combobox for complaint types
selected_type = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=selected_type, values=complainType)
combobox.current(0)  # Set default value to "All"
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_table)

# Create Treeview widget
tree = ttk.Treeview(root, columns=("ID","Complain Type", "Complaint Sub Type", "Specification", "Status", "Username"), show="headings")
tree.heading("ID", text="ID", anchor="center")
tree.heading("Username", text="Username", anchor="center")
tree.heading("Complain Type", text="Complain Type", anchor="center")
tree.heading("Complaint Sub Type", text="Complaint Sub Type", anchor="center")
tree.heading("Specification", text="Specification", anchor="center")
tree.heading("Status", text="Status", anchor="center")
tree.pack(fill="both", expand=True)

# Set alignment of column values to center
for col in tree["columns"]:
    tree.column(col, anchor="center")

# Retrieve and display data in the Treeview
data = retrieve_data()
reload_data(data)

# Set column headings to bold
style = ttk.Style()
style.configure("Treeview.Heading", font=("TkDefaultFont", 10, "bold"))

# menu bar
def raise_complain():    
    root.destroy()
    os.system("python raiseComplain.py")

def track():
    root.destroy()
    os.system("python track.py")

def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        root.destroy()

# Create a menu bar
menubar = tk.Menu(root)

# Create the File menu and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Raise Complain", command=raise_complain)
filemenu.add_command(label="Track", command=track)
filemenu.add_separator()
filemenu.add_command(label="Logout", command=logout)
menubar.add_cascade(label="View", menu=filemenu)

# Display the menu
root.config(menu=menubar)

# Add Accept and Decline buttons
accept_button = tk.Button(root, text="Accept", command=accept_complaint)
accept_button.pack(side="left", padx=5, pady=5)

decline_button = tk.Button(root, text="Decline", command=decline_complaint)
decline_button.pack(side="left", padx=5, pady=5)

root.mainloop()
