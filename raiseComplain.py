import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import psycopg2
from dbConnect import DBConnect as db
from UserData import UserDetail as ud
import os
import Mail

# Your complaint types and subtypes
complainType = ['Infrastructure', 'Academic', 'Administration', 'Campus Life', 'Faculty and Staff']
Infrastructure = ['Classroom facilities', 'Laboratory equipment', 'Library resources', 'Sports facilities', 'Hostel amenities','other']
Academic = ['Teaching quality', 'Course content', 'Examination process', 'Grading system', 'Project guidance','other']
Administration = ['Admission process', 'Fee structure', 'Timetable management', 'Student record maintenance', 'Scholarship distribution','other']
CampusLife = ['Accommodation issues', 'Food quality in canteen', 'Sanitation and cleanliness', 'Transport facilities', 'Security concerns','other']
Faculty_Staff = ['Behavior of faculty', 'Availability of faculty', 'Support staff behavior', 'Grievance redressal mechanism', 'Staff professionalism','other']

# Create main window
root = tk.Tk()
root.title("Raise a Complaint")



# Function to submit complaint data to PostgreSQL
def submit_complaint():
    # Get user inputs
    complaint_type = complaint_type_combobox.get()
    complaint_subtype = complaint_subtype_combobox.get()
    specification = specification_text.get("1.0", "end-1c")
    file_path = uploaded_file_label.cget("text")

    # Check if all fields are filled
    if not all([complaint_type, complaint_subtype, specification]):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        # Connect to the database
        conn = db.getDbConnection()
        cursor = conn.cursor()

        # Insert data into the complaints table
        cursor.execute("INSERT INTO complaints (complaint_type, complaint_subtype, specification, file_path, track, username) VALUES (%s, %s, %s, %s,%s,%s)", (complaint_type, complaint_subtype, specification, file_path,"In_progress",ud.getUserName()))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()

        messagebox.showinfo("Complaint Submitted", "Complaint submitted successfully!")

        # Reset fields after submission
        complaint_type_combobox.set('')
        complaint_subtype_combobox.set('')
        specification_text.delete("1.0", "end")
        uploaded_file_label.config(text="No file selected")
        Mail.sendMail(ud.getMail())
        Mail.sendMailAdmin(ud.getUserName())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to submit complaint: {e}")

# Function to browse and select file
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        uploaded_file_label.config(text=file_path)

# Function to update complaint subtypes based on selected complaint type
def update_subtype_combobox(event):
    selected_type = complaint_type_combobox.get()
    if selected_type == "Infrastructure":
        complaint_subtype_combobox['values'] = Infrastructure
    elif selected_type == "Academic":
        complaint_subtype_combobox['values'] = Academic
    elif selected_type == "Administration":
        complaint_subtype_combobox['values'] = Administration
    elif selected_type == "Campus Life":
        complaint_subtype_combobox['values'] = CampusLife
    elif selected_type == "Faculty and Staff":
        complaint_subtype_combobox['values'] = Faculty_Staff

# Create complaint type label and combobox
complaint_type_label = tk.Label(root, text="Complaint Type:")
complaint_type_label.grid(row=0, column=0, padx=10, pady=5)
complaint_type_combobox = ttk.Combobox(root, values=complainType)
complaint_type_combobox.grid(row=0, column=1, padx=10, pady=5)
complaint_type_combobox.bind("<<ComboboxSelected>>", update_subtype_combobox)

# Create complaint subtype label and combobox
complaint_subtype_label = tk.Label(root, text="Complaint Subtype:")
complaint_subtype_label.grid(row=1, column=0, padx=10, pady=5)
complaint_subtype_combobox = ttk.Combobox(root)
complaint_subtype_combobox.grid(row=1, column=1, padx=10, pady=5)

# Create specification label and textarea
specification_label = tk.Label(root, text="Specification of Complaint:")
specification_label.grid(row=2, column=0, padx=10, pady=5)
specification_text = tk.Text(root, height=5, width=40)
specification_text.grid(row=2, column=1, padx=10, pady=5)

# Create file upload label and button
upload_button = tk.Button(root, text="Upload File", command=browse_file)
upload_button.grid(row=3, column=0, padx=10, pady=5)
uploaded_file_label = tk.Label(root, text="No file selected", wraplength=200)
uploaded_file_label.grid(row=3, column=1, padx=10, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_complaint)
submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

# menu bar
def raise_complain():
    messagebox.showinfo("Raise Complain", "You clicked on Raise Complain")

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
