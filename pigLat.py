# Englihs to Pig Latin

print("Enter the English message to translate into Pig Latin")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pigLatin = []  # A list of words in Pig Latin

for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNoneLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNoneLetters += word[0]
        print(prefixNoneLetters)
        word = word[1:]
        print(word)
    if len(word) == 0:
        pigLatin.append(prefixNoneLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ""
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase ot title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # make the word lowercase for translation

    # Separate the consonants at the start of this word:
    prefixConsonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word:
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word += "yay"

    # set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNoneLetters + word + suffixNonLetters)

# join all the words back together into a single string:
print(" ".join(pigLatin))
