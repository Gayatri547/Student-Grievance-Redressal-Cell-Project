import tkinter as tk
from tkinter import messagebox

def home():
    messagebox.showinfo("Home", "Welcome to the Home page")

def raise_complain():
    messagebox.showinfo("Raise Complain", "You clicked on Raise Complain")

def track():
    messagebox.showinfo("Track", "You clicked on Track")

def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("Menu Example")

# Function to create a new window
def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window")
    label.pack()

# Create a menu bar
menubar = tk.Menu(root)

# Create the File menu and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Home", command=home)
filemenu.add_command(label="Raise Complain", command=raise_complain)
filemenu.add_command(label="Track", command=track)
filemenu.add_separator()
filemenu.add_command(label="Logout", command=logout)
menubar.add_cascade(label="View", menu=filemenu)

# Display the menu
root.config(menu=menubar)

# Start the main event loop
root.mainloop()
