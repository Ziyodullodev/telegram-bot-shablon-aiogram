import json
import os

class Localizator:
    def __init__(self, language="uz"):
        self.language = language
        self.translations = self.load_translations()

    def load_translations(self):
        file_path = f"locales/{self.language}.json"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}  # Agar til topilmasa, bo'sh lug'at qaytariladi

    def set_language(self, language):
        self.language = language
        self.translations = self.load_translations()

    def get(self, key):
        return self.translations.get(key, key)  # Agar kalit bo‘lmasa, aynan o‘zi qaytariladi