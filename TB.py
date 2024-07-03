
import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius} Celsius = {fahrenheit} Fahrenheit")
    except ValueError:
        result_label.config(text="Please enter a valid number for Celsius")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit} Fahrenheit = {celsius} Celsius")
    except ValueError:
        result_label.config(text="Please enter a valid number for Fahrenheit")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Celsius to Fahrenheit conversion
celsius_frame = tk.Frame(root)
celsius_frame.pack(pady=10)

celsius_label = tk.Label(celsius_frame, text="Celsius:")
celsius_label.grid(row=0, column=0, padx=5)

celsius_entry = tk.Entry(celsius_frame)
celsius_entry.grid(row=0, column=1, padx=5)

celsius_to_fahrenheit_button = tk.Button(celsius_frame, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.grid(row=0, column=2, padx=5)

# Fahrenheit to Celsius conversion
fahrenheit_frame = tk.Frame(root)
fahrenheit_frame.pack(pady=10)

fahrenheit_label = tk.Label(fahrenheit_frame, text="Fahrenheit:")
fahrenheit_label.grid(row=0, column=0, padx=5)

fahrenheit_entry = tk.Entry(fahrenheit_frame)
fahrenheit_entry.grid(row=0, column=1, padx=5)

fahrenheit_to_celsius_button = tk.Button(fahrenheit_frame, text="Convert to Celsius", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.grid(row=0, column=2, padx=5)

# Display conversion result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


