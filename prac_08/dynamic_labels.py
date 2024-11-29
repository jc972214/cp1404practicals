"""Prac08 - Dynamic Labels"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Thomas", "Bob", "Jim", "Terry"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels for each name in list"""
        for name in self.names:
            # create a button for each data entry, specifying the text
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()