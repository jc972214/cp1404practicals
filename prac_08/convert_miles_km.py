from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class ConvertMilesKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_miles(self):
        """Receives input miles from user and checks that it is a valid input"""
        try:
            miles = float(self.root.ids.user_input.text)
            return miles
        except ValueError:
            return 0

    def handle_conversion(self):
        """Converts miles to kilometres when button is pressed"""
        miles = self.get_valid_miles()
        conversion = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(conversion)

    def handle_increments(self, increment):
        """Adjusts miles input by +/-1 when up or down button is pressed"""
        miles = self.get_valid_miles() + increment
        self.root.ids.user_input.text = str(miles)
        self.handle_conversion()





ConvertMilesKm().run()