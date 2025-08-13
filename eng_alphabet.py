from alphabet import Alphabet

class EngAlphabet(Alphabet):
    _letters_num = 26
    def __init__(self):
        super().__init__('En', list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    def letters_num(self):
        return self._letters_num

    def is_en_letter(self, letter):
        return letter in self.letters
    
    @staticmethod
    def example():
        return "Example text!"