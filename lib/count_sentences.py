import re

class MyString:
    def __init__(self, value=''):
        self._value = value if isinstance(value, str) else ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        # Split based on '.', '?', and '!'
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out any empty strings
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)
