
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def translate(phrase):
    translation = ""
    for letter in phrase:
        #find the index of the letter in the alphabet
        index = alphabet.index(letter)
        #shift it 13 positions
        translation = translation + alphabet[(index + 13) % 26]
    return translation


user_input = input("Enter a phrase: ")
print(translate(user_input))
print(translate(translate(user_input)))
