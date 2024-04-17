import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")

# Create a function to handle button click
def button_click():
    label.config(text="Button Clicked!")

# Create a label widget
label = tk.Label(root, text="Welcome to Simple GUI")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

# Run the main event loop
root.mainloop()
