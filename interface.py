import tkinter as tk
from tkinter import filedialog

filepath = "" # needs definition to avoid NameError in generate_button_clicked()

def select_file():
    """Allow the user to select a file using a file dialog."""

    global filepath

    filepath = filedialog.askopenfilename(title="Select a file")

    if filepath:
        filename = filepath.split("/")[-1] # separates the filename from the filepath
        file_label.config(text=filename) # display filename now
        status_label.config(text="File selected successfully.")
    else:
        status_label.config(text="No file selected.")


def generate_button_clicked():
    """Handle the generate button."""

    if not filepath:
        status_label.config(text="Please select a file first.")
        return

    status_label.config(text="Ready to generate artwork!")


def create_window():
    """Create main application window."""

    global file_label, status_label

    root = tk.Tk()
    root.title("Art Generator")
    root.geometry("500x400")

    title_label = tk.Label(root, text="art generator", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    description_label = tk.Label(root, text="turn your files into abstract artwork.")
    description_label.pack(pady=20)

    select_button = tk.Button(root, text="Select File", command=select_file)
    select_button.pack(pady=10)

    file_label = tk.Label(root,text="No file selected")
    file_label.pack(pady=5)

    generate_button = tk.Button(root,text="Generate Artwork", command=generate_button_clicked)
    generate_button.pack(pady=20)

    status_label = tk.Label(root,text="Waiting for file selection...")
    status_label.pack(pady=30)

    root.mainloop()

create_window()