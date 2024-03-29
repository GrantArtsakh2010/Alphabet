from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
flag_sound = False
class MainApp(App):
    def build(self):
        self.title = "Alphabet"
        Window.size = (700, 300)
        vowel = [242/255, 36/255, 36/255]
        consonant = [36/255,167/255,242/255]
        button_color = [239 / 255, 242 / 255, 36 / 255]

        box = BoxLayout(orientation = "vertical", spacing = 5)
        box1 = BoxLayout(orientation = "horizontal", spacing = 5)
        box2 = BoxLayout(orientation = "horizontal", spacing = 5)
        box3 = BoxLayout(orientation = "horizontal", spacing = 5)

        box1.add_widget(Button(text="A", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box1.add_widget(Button(text="B", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="C", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="D", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="E", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box1.add_widget(Button(text="F", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="G", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="H", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="I", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box1.add_widget(Button(text="J", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="K", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="L", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box1.add_widget(Button(text="M", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))

        box2.add_widget(Button(text="N", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="O", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box2.add_widget(Button(text="P", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="Q", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="R", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="S", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="T", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="U", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box2.add_widget(Button(text="V", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="W", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="X", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))
        box2.add_widget(Button(text="Y", on_press=self.letters_btn_press, background_color=vowel, background_normal=''))
        box2.add_widget(Button(text="Z", on_press=self.letters_btn_press, background_color=consonant, background_normal=''))

        box3.add_widget(Button(text="Music", on_press=self.sounds_btn_press, background_color=button_color, background_normal=''))

        box.add_widget(box1)
        box.add_widget(box2)
        box.add_widget(box3)

        return box

    def letters_btn_press(self, instance):
        global flag_sound
        if flag_sound == False:
            flag_sound = True
            SoundLoader.load(f'letters\\{instance.text}.mp3').play()
            flag_sound = False

    def sounds_btn_press(self, instance):
        global flag_sound
        if flag_sound == False:
            flag_sound = True
            SoundLoader.load(f'sounds\\{instance.text.lower()}.mp3').play()
            flag_sound = False

if __name__ == "__main__":
    app = MainApp()
    app.run()
