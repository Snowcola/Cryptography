import string
from collections import deque


class VigenereCipher:
    def __init__(self, alphabet=string.ascii_lowercase, x_fill=0, y_fill=0):
        self.alphabet = alphabet
        self.vigenere_table = []

        alphabet = deque(alphabet)
        for x in range(len(alphabet)):
            self.vigenere_table.append(list(alphabet))
            alphabet.rotate(-1)

    def encrypt(self, char, key_char):
        self.message = ""
        x = self.alphabet.index(char.lower())
        y = self.alphabet.index(key_char.lower())
        encrypted_char = self.vigenere_table[y][x]
        return encrypted_char

    def decrypt(self, encrypted_char, key_char):
        self.message = ""
        y = self.alphabet.index(key_char.lower())
        key_index = self.vigenere_table[y].index(encrypted_char.lower())
        char = self.alphabet[key_index]
        return char
