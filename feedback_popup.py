import tkinter as tk
from tkinter import ttk, messagebox

class FeedbackPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Feedback Page")
        
        # Create label for feedback
        self.feedback_label = ttk.Label(self.root, text="Enter your feedback:")
        self.feedback_label.pack(pady=10)
        
        # Create text area for entering feedback
        self.feedback_text = tk.Text(self.root, width=40, height=10)
        self.feedback_text.pack(pady=5)
        
        # Create submit button
        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_feedback)
        self.submit_button.pack(pady=5)
        
        self.root.mainloop()
    
    # Function to handle submit button click
    def submit_feedback(self):
        feedback = self.feedback_text.get("1.0", "end").strip()  # Get feedback from text area
        if feedback:
            # In a real application, you may want to save the feedback to a database or file
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
            self.clear_feedback()
            self.root.destroy()
        else:
            messagebox.showwarning("Feedback Empty", "Please enter your feedback before submitting.")
    
    # Function to clear the feedback text area
    def clear_feedback(self):
        self.feedback_text.delete("1.0", "end")

"""# Create main window
if __name__ == "__main__":
    feedback_page = FeedbackPage()"""
