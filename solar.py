import kivy # type: ignore
from kivy.app import App # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.gridlayout import GridLayout # type: ignore
from kivy.uix.scrollview import ScrollView # type: ignore
from kivy.uix.button import Button # type: ignore

# Define the planets as dictionaries
planets = {
    # ... (planet data) ...
}

# Create the main app class
class SolarSystemApp(App):
    def build(self):
        # Create the main layout
        main_layout = GridLayout(cols=1, spacing=10, padding=10)

        # Create a scrollview for planet information
        info_scrollview = ScrollView()
        info_layout = GridLayout(cols=1, spacing=10)
        for planet_name in planets:
            planet_button = Button(text=planet_name)
            planet_button.bind(on_press=lambda instance: self.show_planet_info(planet_name))
            info_layout.add_widget(planet_button)
        info_scrollview.add_widget(info_layout)
        main_layout.add_widget(info_scrollview)

        # Create a label to display planet information
        self.info_label = Label(text="", size_hint=(1, None))
        main_layout.add_widget(self.info_label)

        return main_layout

    def show_planet_info(self, planet_name):
        planet_info = planets[planet_name]
