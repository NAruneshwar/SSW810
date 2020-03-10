from collections import defaultdict, Counter
""" HW07 implementation file"""


def anagram_lst(str1, str2):
    """ This function takes two strings and compares if they are Anagram using Lists."""
    return sorted(list(str1.lower())) == sorted(list(str2.lower()))


def anagrams_dd(str1, str2):
    """This function takes two strings and compares if they are Anagram using default dictionaries."""
    dd = defaultdict(int)
    for k in str1.lower():
        dd[k]+= 1
    for k in str2.lower():
        dd[k]-=1
        if(dd[k]<0):
            return False
    return sum(dd.values()) == 0


def anagrams_cntr(str1, str2):
    """This function takes two strings and compares if they are Anagram using Counter."""
    return Counter(str1.lower()) == Counter(str2.lower())


def covers_alphabet(sentence):
    """This function takes a string and returns if the given string contains all the alphabets"""
    chars = set(''.join(e for e in sentence.lower() if e.isalpha()))
    return len(chars) == 26
    # return set(s.lower()) >= set("abcdefghijk...")


def book_index(words):
    """ This function takes a list of tuples and returns a book Index."""
    index_words = defaultdict(set)
    for word, page in sorted(words):
        index_words[word].add(page)
    res_lis = list()
    for key, value in index_words.items():
        res_lis.append([key, list(value)])
    return res_lis
