import tkinter as tk

def show_hex(color):
  """Display the hexadecimal code of the clicked color"""
  hex_code = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF", "yellow": "#FFFF00"}[color]
  hex_label.config(text=f"{hex_code}")

root = tk.Tk()
root.title("Basic Colors")

# Create labels for color names
red_label = tk.Label(root, text="Red", font=("Arial", 16), fg="red")
red_label.pack(pady=10)
red_label.bind("<Button-1>", lambda event: show_hex("red"))  # Bind click event

green_label = tk.Label(root, text="Green", font=("Arial", 16), fg="green")
green_label.pack(pady=10)
green_label.bind("<Button-1>", lambda event: show_hex("green"))

blue_label = tk.Label(root, text="Blue", font=("Arial", 16), fg="blue")
blue_label.pack(pady=10)
blue_label.bind("<Button-1>", lambda event: show_hex("blue"))

yellow_label = tk.Label(root, text="Yellow", font=("Arial", 16), fg="yellow")
yellow_label.pack(pady=10)
yellow_label.bind("<Button-1>", lambda event: show_hex("yellow"))

# Label for displaying hex code
hex_label = tk.Label(root, text="", font=("Arial", 16))
hex_label.pack(pady=10)

root.mainloop()
