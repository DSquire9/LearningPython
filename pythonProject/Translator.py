
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def translate(phrase):
    translation = ""
    for letter in phrase:
        # find the index of the letter in the alphabet
        if letter.isalpha():
            if letter.isupper():
                index = alphabet.index(letter.lower())
                # shift it 13 positions
                translation = translation + alphabet[(index + 13) % 26].upper()
            else:
                index = alphabet.index(letter)
                # shift it 13 positions
                translation = translation + alphabet[(index + 13) % 26]
        else:
            translation = translation + letter

    return translation


user_input = input("Enter a phrase: ")
print("Translated: " + translate(user_input))
print("Double Translated: " + translate(translate(user_input)))
