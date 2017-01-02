import unittest

import nth_element


class TestBaseNCodec(unittest.TestCase):
    def setUp(self):
        self.codec = nth_element.BaseNCodec(base=4, max_len=3)

    def testWordAtIndexZeroIsThemEmpyString(self):
        self.assertEqual('', self.codec.wordAt(0))

    def testWordAt(self):
        cases = (
            (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'AA'), (42, 'BBB'), (84, 'DDD'))
        for index, expected in cases:
            self.assertEqual(expected, self.codec.wordAt(index))

    def testIndexOf(self):
        self.assertEqual(0, self.codec.indexOf(''))
        self.assertEqual(1, self.codec.indexOf('A'))
        self.assertEqual(4, self.codec.indexOf('D'))
        self.assertEqual(5, self.codec.indexOf('AA'))
        self.assertEqual(42, self.codec.indexOf('BBB'))
        self.assertEqual(84, self.codec.indexOf('DDD'))


class TestDictionaryCodec(unittest.TestCase):
    def setUp(self):
        self.codec = nth_element.DictionaryCodec(base=4, max_len=3)

    def testWordAtIndexZeroIsThemEmpyString(self):
        self.assertEqual('', self.codec.wordAt(0))

    def testWordAt(self):
        cases = (
            (1, 'A'), (2, 'AA'), (3, 'AAA'), (4, 'AAB'), (5, 'AAC'), (6, 'AAD'), (42, 'BDD'),
            (84, 'DDD')
        )
        for index, expected in cases:
            self.assertEqual(expected, self.codec.wordAt(index))

    def testIndexOf(self):
        self.assertEqual(0, self.codec.indexOf(''))
        self.assertEqual(1, self.codec.indexOf('A'))
        self.assertEqual(3, self.codec.indexOf('AAA'))
        self.assertEqual(4, self.codec.indexOf('AAB'))
        self.assertEqual(10, self.codec.indexOf('ABC'))
        self.assertEqual(84, self.codec.indexOf('DDD'))


class TestDictionaryCodecCompletely(unittest.TestCase):
    _CASES_BASE_AND_LEN = ((2, 4), (3, 2), (4, 3))

    def test(self):
        for base, max_len in self._CASES_BASE_AND_LEN:
            codec = nth_element.DictionaryCodec(base, max_len)
            self.assertEqual(0, codec.indexOf(''))
            self.assertEqual('', codec.wordAt(0))

            last_word = nth_element.lastWord(base, max_len)
            last_word_index = codec.indexOf(last_word)
            prev_word = ''
            for i in range(1, last_word_index+1):
                word = codec.wordAt(i)
                self.assertTrue(prev_word < word)
                self.assertEqual(
                    i, codec.indexOf(word),
                    'Expected index %d for "%s" (base %d, max_len %d)' % (i, word, base, max_len)
                )
                prev_word = word
