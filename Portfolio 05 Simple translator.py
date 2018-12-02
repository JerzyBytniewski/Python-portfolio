# Simple translator - is it a vowel or a consonant?

def translate(word):
    translation = ""
    for letter in word:
        if letter.lower() in "aeoiuy":
            if letter.isupper():
                translation = translation + letter.upper() + " - vowel, "
            else:
                translation = translation + letter.lower() + " - vowel, "
        elif letter.lower() in "prmnbcdfhjzxtsgwvklq":
            if letter.isupper():
                translation = translation + letter.upper() + " - consonant, "
            else:
                translation = translation + letter.lower() + " - consonant, "
        else:
            print("Invalid Signs")
    return translation

print(translate(input("Enter a word or a phrase: ")))