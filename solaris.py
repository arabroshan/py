import tkinter as tk
import math

# Define the planets as dictionaries
planets = {
    "Mercury": {
        "distance": 36 * 10**6 * math.cos(math.radians(48)),  # Distance in km from the Sun
        "radius": 2440,  # Radius in km
        "mass": 3.3011 * 10**23,  # Mass in kg
        "orbital_period": 0.24 * 365.25,  # Orbital period in Earth days
        "rotation_period": 58.67,  # Rotation period in Earth hours
        "moons": 0,  # Number of moons
        "atmosphere": "Trace amounts of helium, sodium, oxygen, and argon"
    },
    "Venus": {
        "distance": 108 * 10**6 * math.cos(math.radians(35)),  # Distance in km from the Sun
        "radius": 6052,  # Radius in km
        "mass": 4.8675 * 10**24,  # Mass in kg
        "orbital_period": 224.7,  # Orbital period in Earth days
        "rotation_period": -243.02,  # Rotation period in Earth hours (retrograde)
        "moons": 0,  # Number of moons
        "atmosphere": "Thick carbon dioxide, nitrogen, and sulfuric acid"
    },
    # ... other planets ...
}

# Create the main window
root = tk.Tk()
root.title("Solar System Information")

# Define a function to display planet information
def show_planet_info(planet_name):
    planet_info = planets[planet_name]
    info_text = f"""Planet: {planet_name}
Distance from Sun: {planet_info['distance']:,} km
Radius: {planet_info['radius']:,} km
Mass: {planet_info['mass']:,.2f} kg
Orbital Period: {planet_info['orbital_period']:,.2f} Earth days
Rotation Period: {planet_info['rotation_period']:,.2f} Earth hours
Moons: {planet_info['moons']}
Atmosphere: {planet_info['atmosphere']}"""
    info_label.config(text=info_text)

# Create a dropdown menu to select a planet
planet_options = list(planets.keys())
planet_dropdown = tk.OptionMenu(root, show_planet_info, *planet_options)
planet_dropdown.pack()

# Create a label to display planet information
info_label = tk.Label(root, text="")
info_label.pack()

# Run the main event loop
root.mainloop()
