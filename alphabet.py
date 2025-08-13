class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(''.join(self.letters))

    def letters_num(self):
        return len(self.letters)