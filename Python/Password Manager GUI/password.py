import random
import string


class Password:

    def __init__(self):
        self.alphabet = list(string.ascii_letters)
        self.symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                        '}',
                        '.',
                        '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
        self.numbers = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # This method generates random password for the users if they click the generate password button.
    def random_password(self):
        strong_password_list = random.sample(self.alphabet, random.randint(1, 4)) + random.sample(self.symbols,
                                                                                                  random.randint(1,
                                                                                                                 4)) + \
                               (random.sample(self.numbers, random.randint(1, 4)))

        strong_password = "".join(strong_password_list)

        return strong_password
