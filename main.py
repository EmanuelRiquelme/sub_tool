import tkinter as tk

def close_window(event):
    root.destroy()

def resize(event):
    window_width = event.width
    window_height = event.height
    text_widget.config(width=window_width // 10, height=window_height // 20)

root = tk.Tk()
root.overrideredirect(True)
root.configure(bg="black")  # Set window background color to black
root.attributes("-alpha", 0.9)  # Set window transparency (0.0 to 1.0)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.4)
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set the font to a monospaced font and change text color to white
text_widget = tk.Text(root, wrap=tk.WORD, font=("Courier", 14), fg="white", bg="black")
text_widget.pack(expand=True, fill=tk.BOTH)

text_widget.insert(tk.END, "This is a resizable text-only Tkinter app.\nPress Escape to close the window.")

# Bind the <Escape> key event to close the window
root.bind_all("<Escape>", close_window)

# Bind the <Configure> event to resize the app
root.bind("<Configure>", resize)

root.mainloop()

