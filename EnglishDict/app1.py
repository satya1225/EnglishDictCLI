import json
from difflib import get_close_matches as gcm

data = json.load(open('EnglishDict/data.json'))


def translate(word):
    word = word.lower()
    word_c = word.capitalize()
    word_u = word.upper()
    if word in data:
        return data[word]
    elif word_c in data:
        return data[word_c]
    elif word_u in data:
        return data[word_u]
    elif gcm(word, data.keys()):
        yn = input("Did you mean %s instead? Enter Y for yes, N for no: " % gcm(word, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[gcm(word, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."    


word = input("Enter the word: ")
output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
