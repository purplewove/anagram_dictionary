import unittest
from anagrams import AnagramDictionary, Phrase
'''
Created on Oct 26, 2015

@author: templetonc
'''


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = AnagramDictionary()
    
    def test_insert_word(self):
        word = "friend"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 7, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3}, {"e":4}, {"n":5}, {"d":6}, {}], "node list = {}".format(self.dictionary.node_list)
        assert self.dictionary.back_pointers == [None, 0, 1, 2, 3, 4, 5], "backpointers = {}".format(self.dictionary.back_pointers)
        word = "freight"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 12, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend", None, None, None, None, "freight"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {}], "node list = {}".format(self.dictionary.node_list)
        assert self.dictionary.back_pointers == [None, 0, 1, 2, 3, 4, 5, 2, 7, 8, 9, 10], "backpointers = {}".format(self.dictionary.back_pointers)
        word = "friends"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 13, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend", None, None, None, None, "freight", "friends"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {"s":12}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {}, {}], "node list = {}".format(self.dictionary.node_list)
        assert self.dictionary.back_pointers == [None, 0, 1, 2, 3, 4, 5, 2, 7, 8, 9, 10, 6], "backpointers = {}".format(self.dictionary.back_pointers)
        word = "freighted"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend", None, None, None, None, "freight", "friends", None, "freighted"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {"s":12}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {"e":13}, {}, {"d":14}, {}], "node list = {}".format(self.dictionary.node_list)
        word = "frei"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend", None, "frei", None, None, "freight", "friends", None, "freighted"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {"s":12}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {"e":13}, {}, {"d":14}, {}], "node list = {}".format(self.dictionary.node_list)
        
    def test_set_dictionary(self):
        path = "test_dictionary.txt"
        self.dictionary.set_dictionary(path)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.words == [None, None, None, None, None, None, "friend", None, None, None, None, "freight", "friends", None, "freighted"], "dictionary.words = {}".format(self.dictionary.words)
        assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {"s":12}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {"e":13}, {}, {"d":14}, {}], "node list = {}".format(self.dictionary.node_list)
       
    def test_phrase(self):
        import operator
        test_phrase = Phrase("the fat cat sat on the mat")
        assert test_phrase.full == "the fat cat sat on the mat"
        assert test_phrase.stripped == "thefatcatsatonthemat"
        assert test_phrase.dictionary == {"a":4, "b":0, "c":1, "d":0, "e":2, "f":1, "g":0, "h":2, "i":0, "j":0, "k":0, "l":0, "m":1, "n":1, "o":1, "p":0, "q":0, "r":0, "s":1, "t":6, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}, "dictionary is {}".format(sorted(test_phrase.dictionary.items(), key=operator.itemgetter(0)))
    
    def test_is_solution(self):
        phrase = Phrase("this is a test phrase")
        solution = "jjjjjjjjjjjjjjjjj"
        assert self.dictionary._is_solution(phrase, solution) == True
        solution = "jjjjjjjjjjjjjjjj"
        assert self.dictionary._is_solution(phrase, solution) == False
        solution = "jjjjjjjjjjjjjjjjjj"
        assert self.dictionary._is_solution(phrase, solution) == False

    def test_find_anagrams(self):
        path = "test_dictionary.txt"
        self.dictionary.set_dictionary(path)
        phrase = Phrase("redefined frights")
        expected_anagrams = ["friends freighted", "freighted friends"]
        self.dictionary.find_anagrams(phrase)
        assert set(self.dictionary.anagrams) == set(expected_anagrams), "self.dictionary.anagrams == {}".format(self.dictionary.anagrams)

#test set_dictionary (additive)
#test set_dictionary (reset)
#should address upper/lower case
            