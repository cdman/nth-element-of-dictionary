"""
Methods to find the index of a word in a complete dictionary and to find the nth word in a complete
dictionary.
"""
import string


def lastWord(base, max_len):
    last_letter = string.ascii_uppercase[base - 1]
    return last_letter * max_len

class BaseNCodec(object):
    def __init__(self, base, max_len):
        self.__base = base
        self.__alphabet = string.ascii_uppercase[:base]
        self.__max_len = max_len
        self.__lastIndex = self.indexOf(lastWord(base, max_len))

    def wordAt(self, index):
        assert 0 <= index <= self.__lastIndex
        if index == 0: return ''
        result = []
        while True:
            index -= 1
            c = self.__alphabet[index % self.__base]
            result.insert(0, c)
            index = index // self.__base
            if index == 0:
                break
        return ''.join(result)

    def indexOf(self, word):
        assert len(word) <= self.__max_len
        multiplier = 1
        result = 0
        for c in word[::-1]:
            ci = self.__alphabet.index(c) + 1
            result += multiplier * ci
            multiplier *= self.__base
        return result


class DictionaryCodec(object):
    def __init__(self, base, max_len):
        self.__base = base
        self.__max_len = max_len
        self.__alphabet = string.ascii_uppercase[:base]
        self.__wordsPerLetterForLen = {
            l: self.__wordsWithSameFirstLetterForLen(l) for l in range(0, max_len+1)}
        self.__lastIndex = self.indexOf(lastWord(base, max_len))

    def __noWordsLen(self, n):
        return self.__base ** n

    def __noWordsLenLessOrEqualTo(self, n):
        return sum(self.__noWordsLen(i) for i in range(0, n+1))

    def __wordsWithSameFirstLetterForLen(self, l):
        return self.__noWordsLenLessOrEqualTo(l) // self.__base

    def wordAt(self, index):
        assert 0 <= index <= self.__lastIndex
        result, current_len = '', self.__max_len
        while index > 0:
            words_per_column = self.__wordsPerLetterForLen[current_len]
            column_idx = (index - 1) // words_per_column
            result += self.__alphabet[column_idx]
            index_of_first_word_in_col = 1 + column_idx * words_per_column
            index -= index_of_first_word_in_col
            current_len -= 1
        return result

    def __valueInBaseN(self, word):
        result = 0
        multiplier = 1
        for c in word[::-1]:
            ci = self.__alphabet.index(c)
            result += multiplier * ci
            multiplier *= self.__base
        return result

    def indexOf(self, word):
        assert len(word) <= self.__max_len
        result = 0
        for i in range(0, self.__max_len + 1):
            if i < len(word):
                subword = word[:i]
                result += self.__valueInBaseN(subword) + 1
            else:
                subword = word + (i - len(word)) * self.__alphabet[0]
                result += self.__valueInBaseN(subword)
        return result
