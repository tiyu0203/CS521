"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/30/21
Homework Problem #5_1
Description of Problem: 
Take in a string and return the letter count and the most frequent letter
"""
def letter_counts(sentence):
    letter_frequency = {}
    for i in sorted(sentence.upper()):
        if i.isalpha():
            keys = letter_frequency.keys()
            if i in keys:
                letter_frequency[i] += 1
            else:
                letter_frequency[i] = 1
    return letter_frequency

def most_common_letter(sentence):
    letter_frequency = letter_counts(sentence)
    freq_letters = list()
    max_value = max(letter_frequency.values())

    for key, val in letter_frequency.items(): 
        if val == max_value:
            freq_letters.append(key)
    return freq_letters

def string_count_histogram(sentence):
    letter_frequency = letter_counts(sentence)
    letters = list(letter_frequency.keys())
    freqs = list(letter_frequency.values())
    
    for n, i in enumerate(letters):
        letters[n] = "   "+freqs[n]*letters[n]
    return letters


if __name__ == '__main__':
    sentence = "WaS IT A RAT I SAW"
    print('The string being analyzed is: "', sentence , '"')
    letter_frequency = letter_counts(sentence)
    print("1. Letter counts:", ', '.join('%s: %s' % (k,letter_frequency[k]) for k in letter_frequency.keys()))
    max_value = max(letter_frequency.values())
    freq_letters = most_common_letter(sentence)
    if (len(freq_letters) > 1):
        print("2. Most frequent letters", str(freq_letters)[1:-1], "appear", max_value, "times.")
    else:
        print('2. Most frequent letter', str(freq_letters)[1:-1], 'appears', max_value, "times.")
    letters = string_count_histogram(sentence)
    print("3. Histogram:")
    print(*letters, sep = "\n")