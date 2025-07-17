def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text):
    words = text.lower()
    letter_counts = {}
    for line in words:
        for letter in line:
            if letter in letter_counts:
                letter_counts[letter] +=1
            else:
                letter_counts[letter] = 1
    return letter_counts

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    converted_dictlist = [{"key": l, "num": n} for l, n in dict.items()]
    converted_dictlist.sort(reverse=True, key=sort_on)
    return converted_dictlist