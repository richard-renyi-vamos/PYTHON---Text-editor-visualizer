import tkinter as tk

# Function to update second screen with typed text
def update_mirror_text(event=None):
    mirrored_text.delete("1.0", tk.END)
    mirrored_text.insert(tk.END, text_input.get("1.0", tk.END))

# Main editor window
root = tk.Tk()
root.title("Text Editor ✍️")

text_input = tk.Text(root, height=20, width=60, font=("Arial", 14))
text_input.pack(padx=10, pady=10)
text_input.bind("<KeyRelease>", update_mirror_text)

# Second display window
mirror_window = tk.Toplevel(root)
mirror_window.title("Live Mirror 🪞")

mirrored_text = tk.Text(mirror_window, height=20, width=60, font=("Arial", 14), bg="light yellow", fg="dark blue")
mirrored_text.pack(padx=10, pady=10)
mirrored_text.config(state="normal")

root.mainloop()
