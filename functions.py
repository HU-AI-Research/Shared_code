import json

def open_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)

def clean_words(word):
    word = word.lower()
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace("?", "")
    word = word.replace("#", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("!", "")
    word = word.replace("'", "")
    word = word.replace(";", "")
    word = word.replace("&", "")
    return word

def sentiment(word):
    words = open_file('all_assesssments.json')
    for index, w in words['word'].items():
        if w == word:
            sentiment1 = words['evaluation1'][index]
            sentiment2 = words['evaluation2'][index]
            if sentiment1 == '++':
                sentiment1 = 2
            elif sentiment1 == '+':
                sentiment1 = 1
            elif sentiment1 == '0':
                sentiment1 = 0
            elif sentiment1 == '-':
                sentiment1 = -1
            elif sentiment1 == '--':
                sentiment1 = -2
            else:
                sentiment1 = 'no'

            if sentiment2 == '++':
                sentiment2 = 2
            elif sentiment2 == '+':
                sentiment2 = 1
            elif sentiment2 == '0':
                sentiment2 = 0
            elif sentiment2 == '-':
                sentiment2 = -1
            elif sentiment2 == '--':
                sentiment2 = -2
            else:
                sentiment2 = 'no'
            
            if sentiment2 == 'no' and sentiment1 == 'no':
                sentiment = 0
            elif sentiment2 == 'no' and sentiment1 != 'no':
                sentiment = sentiment1
            elif sentiment2 != 'no' and sentiment1 == 'no':
                sentiment = sentiment2
            else:
                sentiment = (sentiment1 + sentiment2)/2
    return sentiment
