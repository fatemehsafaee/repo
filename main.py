from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

def encrypt(code, key):
    encrypted = ""
    key_length = len(key)

    for i, char in enumerate(code):
        encrypted_char = ord(char) ^ ord(key[i % key_length])
        encrypted += format(encrypted_char, '02x')  # Convert to hexadecimal 

    return encrypted


class MainApp(App):
    def build(self):
        # Create a button that opens a popup when pressed
        button = Button(text='change the password', on_press=self.open_popup)
        button.background_color = get_color_from_hex('#00D8E6')  # Light blue
        return button

    def open_popup(self, *args):
        # Create a popup with a text input, a crypt button, and a close button
        content = BoxLayout(orientation='vertical')
        text_input = TextInput(hint_text='Enter the new password up to 8 characters_just numbers', multiline=False)
        crypt_button = Button(text='Crypt it')
        close_button = Button(text='back')
        content.add_widget(text_input)
        content.add_widget(crypt_button)
        content.add_widget(close_button)
        popup = Popup(title='reset the password', content=content, size_hint=(None, None), size=(600, 700))

        # Bind the crypt button to a custom function
        def on_crypt(instance):
            # Add your cryptography code here
            encryption_key = "thekey" 
            encrypted_code = encrypt(text_input.text, encryption_key)
            print('Encrypted password:', encrypted_code)
            print('new password:', text_input.text)

            # Create a new popup to display the encrypted text
            encrypted_popup = Popup(title='Encrypted password', size_hint=(None, None), size=(600, 700))
            encrypted_content = BoxLayout(orientation='vertical')
            input_label = Label(text=f'your new password: {text_input.text}', size_hint=(1, 0.2))
            encrypted_label_text = Label(text='Encrypted password:')
            encrypted_label = Label(text=f'{encrypted_code}', size_hint=(1, 0.8), font_size='20sp')
            back_button = Button(text='set a new password', size_hint=(1, 0.2))
            encrypted_content.add_widget(input_label)
            encrypted_content.add_widget(encrypted_label_text)
            encrypted_content.add_widget(encrypted_label)
            encrypted_content.add_widget(back_button)
            encrypted_popup.content = encrypted_content

            encrypted_popup.open()

            # back button
            def on_back(instance):
                encrypted_popup.dismiss()
                popup.open()

            back_button.bind(on_press=on_back)

            # Close the popup when done
            popup.dismiss()

        crypt_button.bind(on_press=on_crypt)

        # Bind the close button to dismiss the popup
        close_button.bind(on_press=popup.dismiss)

        # Open the popup
        popup.open()


if __name__ == '__main__':
    MainApp().run()