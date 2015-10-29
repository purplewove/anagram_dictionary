import unittest
from anagrams import AnagramDictionary, Phrase, Node
'''
Created on Oct 26, 2015

@author: templetonc
'''


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = AnagramDictionary()
    
    def test_insert_word(self):
        self.dictionary.clear_dictionary()
        word = "friend"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 7, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({}, 5, "friend")], "node_list = {}".format(self.dictionary.node_list)     
        word = "freight"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 12, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3, "e":7}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({}, 5, "friend"), Node({"i":8}, 2, None), Node({"g":9}, 7, None), Node({"h":10}, 8, None), Node({"t":11}, 9, None), Node({}, 10, "freight")], "node_list = {}".format(self.dictionary.node_list)
        word = "friends"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 13, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3, "e":7}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({"s":12}, 5, "friend"), Node({"i":8}, 2, None), Node({"g":9}, 7, None), Node({"h":10}, 8, None), Node({"t":11}, 9, None), Node({}, 10, "freight"), Node({}, 6, "friends")], "node_list = {}".format(self.dictionary.node_list)
        word = "freighted"
        self.dictionary._insert_word(word)
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3, "e":7}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({"s":12}, 5, "friend"), Node({"i":8}, 2, None), Node({"g":9}, 7, None), Node({"h":10}, 8, None), Node({"t":11}, 9, None), Node({"e":13}, 10, "freight"), Node({}, 6, "friends"), Node({"d":14}, 11, None), Node({}, 13, "freighted")], "node_list = {}".format(self.dictionary.node_list)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list)) 
        word = "frei"
        self.dictionary._insert_word(word)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3, "e":7}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({"s":12}, 5, "friend"), Node({"i":8}, 2, None), Node({"g":9}, 7, "frei"), Node({"h":10}, 8, None), Node({"t":11}, 9, None), Node({"e":13}, 10, "freight"), Node({}, 6, "friends"), Node({"d":14}, 11, None), Node({}, 13, "freighted")], "node_list = {}".format(self.dictionary.node_list)   
        print ("finished insert word test")
        
    def test_set_dictionary(self):
        path = "test_dictionary.txt"
        self.dictionary.set_dictionary(path)
        assert len(self.dictionary.node_list) == 15, "node list length = {}".format(len(self.dictionary.node_list))
        assert self.dictionary.node_list == [Node({"f":1}, None, None), Node({"r":2}, 0, None), Node({"i":3, "e":7}, 1, None), Node({"e":4}, 2, None), Node({"n":5}, 3, None), Node({"d":6}, 4, None), Node({"s":12}, 5, "friend"), Node({"i":8}, 2, None), Node({"g":9}, 7, None), Node({"h":10}, 8, None), Node({"t":11}, 9, None), Node({"e":13}, 10, "freight"), Node({}, 6, "friends"), Node({"d":14}, 11, None), Node({}, 13, "freighted")], "node_list = {}".format(self.dictionary.node_list)
        #assert self.dictionary.node_list == [None, None, None, None, None, None, "friend", None, None, None, None, "freight", "friends", None, "freighted"], "dictionary.words = {}".format(self.dictionary.words)
        #assert self.dictionary.node_list == [{"f":1}, {"r":2}, {"i":3, "e":7}, {"e":4}, {"n":5}, {"d":6}, {"s":12}, {"i":8}, {"g":9}, {"h":10}, {"t":11}, {"e":13}, {}, {"d":14}, {}], "node list = {}".format(self.dictionary.node_list)
       
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
        print ("testing find_anagrams")
        path = "test_dictionary.txt"
        self.dictionary.set_dictionary(path)
        phrase = Phrase("redefined frights")
        expected_anagrams = ["friends freighted", "freighted friends"]
        self.dictionary.find_anagrams(phrase)
        assert set(self.dictionary.anagrams) == set(expected_anagrams), "self.dictionary.anagrams == {}".format(self.dictionary.anagrams)

#test set_dictionary (additive)
#test set_dictionary (reset)
#should address upper/lower case