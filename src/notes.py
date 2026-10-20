from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import json
import os

DATA_FILE = "notes.json"

class NotesApp(App):
    def build(self):
        self.notes = self.load_notes()

        root = BoxLayout(orientation="vertical", spacing=10, padding=10)

        form = BoxLayout(size_hint_y=None, height="48dp", spacing=10)
        self.title_input = TextInput(hint_text="Title")
        form.add_widget(self.title_input)

        add_button = Button(text="Add Note")
        add_button.bind(on_press=self.add_note)
        form.add_widget(add_button)

        root.add_widget(form)

        self.list_container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.list_container.bind(minimum_height=self.list_container.setter("height"))
        root.add_widget(ScrollView(size_hint=(1, 1), do_scroll_x=False))
        root.children[1].add_widget(self.list_container)

        self.refresh_notes()
        return root

    def load_notes(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_notes(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.notes, f)

    def add_note(self, instance):
        title = self.title_input.text.strip()
        if not title:
            return
        self.notes[title] = "New note"
        self.save_notes()
        self.title_input.text = ""
        self.refresh_notes()

    def refresh_notes(self):
        self.list_container.clear_widgets()
        for title in self.notes:
            btn = Button(text=title, size_hint_y=None, height="48dp")
            btn.bind(on_press=self.open_note)
            self.list_container.add_widget(btn)

    def open_note(self, instance):
        title = instance.text
        note_content = self.notes.get(title, "")
        print("Open note:", title, note_content)

if __name__ == "__main__":
    NotesApp().run()