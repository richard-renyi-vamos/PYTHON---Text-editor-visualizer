Here’s a small Python script that opens up a simple text editor. Whatever you type in it will instantly show up in a second window. It’s handy if you want to display text somewhere else as you type — like for presentations, live notes, or just for fun.

The whole thing runs using Tkinter, which is built into Python, so no extra installs needed.

python
Copy
Edit
import tkinter as tk

# Updates the second window with the latest text
def update_mirror_text(event=None):
    mirrored_text.delete("1.0", tk.END)
    mirrored_text.insert(tk.END, text_input.get("1.0", tk.END))

# Main window (where you type)
root = tk.Tk()
root.title("Text Editor")

text_input = tk.Text(root, height=20, width=60, font=("Arial", 14))
text_input.pack(padx=10, pady=10)
text_input.bind("<KeyRelease>", update_mirror_text)

# Second window (shows live updates)
mirror_window = tk.Toplevel(root)
mirror_window.title("Live Display")

mirrored_text = tk.Text(mirror_window, height=20, width=60, font=("Arial", 14), bg="light yellow", fg="dark blue")
mirrored_text.pack(padx=10, pady=10)

root.mainloop()
To use it:
Save the script as text_editor.py.

Run it with Python.

You’ll see two windows: type in the first one, and the second one updates in real time.
