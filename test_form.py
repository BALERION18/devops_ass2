import unittest
import os
from html.parser import HTMLParser

class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'form':
            self.form_found = True
        elif tag == 'input':
            self.inputs.append(attrs_dict)
        elif tag == 'button':
            self.buttons.append(attrs_dict)

class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = 'index.html'
        if not os.path.exists(cls.file_path):
            raise FileNotFoundError(f"{cls.file_path} does not exist.")
        with open(cls.file_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.parser = FormParser()
        cls.parser.feed(cls.content)

    def test_file_exists(self):
        """Verify that index.html exists."""
        self.assertTrue(os.path.exists(self.file_path), "index.html file does not exist")

    def test_form_presence(self):
        """Verify that <form> element is present."""
        self.assertTrue(self.parser.form_found, "Form element (<form>) is not present in HTML")

    def test_name_input_presence(self):
        """Verify that Name input field is present."""
        has_name = any(
            inp.get('name') == 'name' or inp.get('id') == 'name'
            for inp in self.parser.inputs
        )
        self.assertTrue(has_name, "Name input field is missing")

    def test_email_input_presence(self):
        """Verify that Email input field is present."""
        has_email = any(
            inp.get('type') == 'email' or inp.get('name') == 'email' or inp.get('id') == 'email'
            for inp in self.parser.inputs
        )
        self.assertTrue(has_email, "Email input field is missing")

    def test_contact_input_presence(self):
        """Verify that Contact Number input field is present."""
        has_contact = any(
            inp.get('type') == 'tel' or inp.get('name') == 'contact' or inp.get('id') == 'contact'
            for inp in self.parser.inputs
        )
        self.assertTrue(has_contact, "Contact Number input field is missing")

    def test_submit_button_presence(self):
        """Verify that Submit button is present."""
        has_submit_input = any(
            inp.get('type') == 'submit'
            for inp in self.parser.inputs
        )
        has_submit_button = any(
            btn.get('type') == 'submit' or btn.get('id') == 'submit' or 'type' not in btn
            for btn in self.parser.buttons
        )
        self.assertTrue(has_submit_input or has_submit_button, "Submit button is missing")

if __name__ == '__main__':
    unittest.main(verbosity=2)
