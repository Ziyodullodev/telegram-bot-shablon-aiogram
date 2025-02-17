import json
import os

class Lang: 
    lang = None 
    data = None
    def __init__(self, lang):
        self.lang = lang
    
    def set_lang(self):
        with open(f'./locales/{self.lang}.json', 'r') as file:
            self.data = json.load(file)
            return self.data
            