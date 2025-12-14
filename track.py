import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from dbConnect import DBConnect as db
from UserData import UserDetail as ud
import os
import feedback_popup


# Function to retrieve data from the database
def retrieve_data():
    try:
        # Connect to the database
        conn = db.getDbConnection()
        cursor = conn.cursor()
        # Retrieve data from the database
        cursor.execute("SELECT * FROM complaints WHERE username=%s",(ud.getUserName(),))
        data = cursor.fetchall()

        # Close connection
        conn.close()

        return data
    except Exception as e:
        print(f"Failed to retrieve data: {e}")

# Function to open the feedback popup window
def open_feedback_popup(event):
    # Get the item clicked in the treeview
    #item = tree.selection()[0]
    # Get the feedback text from the clicked item
    feedback_text = tree.item(item, "values")[4]  # Assuming "Feedback" column is index 4
    # Open the feedback popup window
    popup = feedback_popup.FeedbackPage()


# Create main window
root = tk.Tk()
root.title("Table View")

# Create Treeview widget
tree = ttk.Treeview(root, columns=("Complain Type", "Complaint Sub Type", "Specification", "Status","Feedback"), show="headings")
tree.heading("Complain Type", text="Complain Type",anchor="center")
tree.heading("Complaint Sub Type", text="Complaint Sub Type",anchor="center")
tree.heading("Specification", text="Specification",anchor="center")
tree.heading("Status", text="Status",anchor="center")
tree.heading("Feedback", text="Feedback", anchor="center")
tree.pack(fill="both", expand=True)

# Set alignment of column values to center
for col in tree["columns"]:
    tree.column(col, anchor="center")

# Retrieve and display data in the Treeview
data = retrieve_data()
for row in data:
    tree.insert("", "end", values=[row[0],row[1],row[2],row[4],"feedback"])

# Make feedback text clickable
tree.tag_configure("feedback_tag", foreground="blue")
tree.tag_bind("feedback_tag", "<Button-1>", open_feedback_popup)

# Set the "Feedback" text to be clickable and display it in blue color
for item in tree.get_children():
    tree.item(item, tags=("feedback_tag",))

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

root.mainloop()
