import tkinter as tk

root = tk.Tk()
root.title("Canvas Demo")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw a red rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="red", outline="blue")

# Draw a blue oval
canvas.create_oval(200, 150, 300, 250, fill="blue")

# Draw a green line
canvas.create_line(50, 250, 350, 50, fill="green", width=3)

# Add some text
canvas.create_text(200, 20, text="Hello Canvas!", font=("Arial", 16))

root.mainloop()