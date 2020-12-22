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

def add_sentiment(tweet):
    #open the dictionary with the sentiment and set default sentiment to 0 (neutral)
    words = open_file('sentiment_dict.json')
    sentiment = 0
    
    #for each word in the tweet
    for w in tweet.split():
        #clean the word, remove hashtags, punctuation, etc. and make it lower case
        w = clean_words(w)
        w = w.lower()
    
        #loop through dictionary and see if we can find a match
        for word in words:
            if word == w:
                #if we have a match add this sentiment to the total amount
                sentiment += words[w]
            else: pass

    #after all words are matched return total sum of sentiment
    return sentiment

def word_count(tweet):
    #set defaults to 0
    word_count = 0
    #for each word in the tweet that is received as input
    for w in tweet.split():
        #if the word is a mention or a link we don't count them
        if '@' in w or 'http' in w:
            pass
        else:
            #add 1 to the count of the amount of words
            word_count +=1

    #return the word count        
    return word_count

def contains_link(tweet):
    #if a tweet contains a link (has 'http' in it) return 1 (true) otherwise return 0 (false)
    if 'http' in tweet:
        return 1
    else:
        return 0

def average_word_length(tweet):
    #set defaults to 0
    word_count = 0
    word_length = 0

    #for each word in the tweet that is received as input
    for w in tweet.split():
        #if the word is a mention or a link we don't count them
        if '@' in w or 'http' in w:
            pass
        else:
            #clean the word, remove hashtags, punctuation, etc.
            w = clean_words(w)
            #add the length of this word to the total
            word_length = word_length + len(w)
            #add 1 to the count of the amount of words
            word_count +=1
    #calculate average by dividing word length with the amount of words
    if word_count != 0 and word_length != 0:
        average_word_length = word_length/word_count
    else:
        average_word_length = 0
    #returning the average
    return average_word_length

def longest_word(tweet):
    #set default to 0
    longest_word = 0

    #for each word in the tweet that is received as input
    for w in tweet.split():
        #if the word is a mention or a link we don't count them
        if '@' in w or 'http' in w:
            pass
        else:
            #clean the word, remove hashtags, punctuation, etc.
            w = clean_words(w)
            #calculate the length of the word (amount of characters)
            word_length = len(w)

            #if this word is the longest word replace the length of the longest word
            if word_length > longest_word:
                longest_word = word_length
            else:
                pass
    #after for loop return result of the longest word
    return longest_word

def check_for_numbers(tweet):
    #set default to 0
    contains_digit = 0

    #loop through words
    for w in tweet.split():
        #if the word is a mention or a link we don't count them
        if '@' in w or 'http' in w:
            pass
        else:
            #loop through characters
            for character in w:
                if character.isdigit():
                    #there is a digit
                    contains_digit = 1
                else: 
                    pass
    
    return contains_digit

def amount_of_numbers(tweet):
    #set default to 0
    digits = 0

    #loop through words
    for w in tweet.split():
        #if the word is a mention or a link we don't count them
        if '@' in w or 'http' in w:
            pass
        else:
            #loop through characters
            for character in w:
                if character.isdigit():
                    #there is a digit
                    digits += 1
                else: 
                    pass
    
    return digits

def percentage_use(tweet):
    #if percentage sign or word is in tweet than it's true (1) other is false (0)
    if '%' in tweet:
        return 1
    elif 'percentage' in tweet:
        return 1
    else:
        return 0
