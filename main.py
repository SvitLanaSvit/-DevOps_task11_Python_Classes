from eng_alphabet import EngAlphabet

if __name__ == "__main__":
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print("Number of letters:", eng_alphabet.letters_num())
    print("Is 'F' English?:", eng_alphabet.is_en_letter('F'))
    print("Is 'Щ' English?:", eng_alphabet.is_en_letter('Щ'))
    print("Example:", eng_alphabet.example())