from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, 'r') as f:
        for word in f:
            words.append(word.strip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    cur_sum = 0
    for ch in word.upper():
        cur_sum += LETTER_SCORES.get(ch, 0)
    return cur_sum

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    cur_value = 0
    word_value = ""
    for word in words:
        cur_value = calc_word_value(word)
        if cur_value > max_value:
            max_value, word_value = cur_value, word
    return word_value

if __name__ == "__main__":
    pass # run unittests to validate
    # $ py -3.5 -m unittest test_wordvalue.py