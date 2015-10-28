from enum import Enum, unique
'''
Created on Oct 26, 2015

@author: templetonc
'''

class AnagramDictionary():
    def __init__(self, path=None):
        self.node_list = [{}]
        self.words = [None]
        self.back_pointers = [None]
        self.anagrams = []
        if path:
            self.set_dictionary(path)
                
    def set_dictionary(self, path, additive=False):
        if additive == False:
            while len(self.node_list) > 1 : self.node_list.pop()
            while len(self.words) > 1: self.words.pop()
            while len(self.words) > 1: self.back_pointers.pop()
        with open(path, 'rb') as infile:
                for line in infile:
                	self._insert_word(line.strip())
                        
    def _insert_word(self, word, word_pos=0, array_pos=0):
        if word_pos == len(word):
            self.words[array_pos] = word
        else:
            letter = word[word_pos]
            if letter in self.node_list[array_pos]:
                self._insert_word(word, word_pos + 1, self.node_list[array_pos][letter])
            else:
                for letter in word[word_pos:len(word) - 1]:
                    self.node_list[array_pos][letter] = len(self.node_list)
                    self.back_pointers.append(array_pos)
                    array_pos = len(self.node_list)
                    self.node_list.append({})
                    self.words.append(None)
                letter = word[len(word) - 1]
                self.node_list[array_pos][letter] = len(self.node_list)
                self.back_pointers.append(array_pos)
                array_pos = len(self.node_list)
                self.node_list.append({})
                self.words.append(word)
                
    def find_anagrams(self, phrase):           
        assert isinstance(phrase, Phrase), "Argument to find_anagrams must be of type Phrase()"
        self._backtrack(phrase, [])
        
    def _backtrack(self, phrase, solution, array_pos=0):
        if self._is_solution(phrase, solution):
            if self.words[array_pos]:
                self._process_solution(phrase, solution)
        else:
            candidates = self._construct_candidates(phrase, array_pos)
            for candidate in candidates:
                array_pos = self._make_move(candidate, solution, array_pos, phrase)
                self._backtrack(phrase, solution, array_pos)
                array_pos = self._unmake_move(solution, array_pos, candidate, phrase)
     
    def _construct_candidates(self, phrase, array_pos):
        candidates = []
        for letter in self.node_list[array_pos]:
            if phrase.dictionary[letter] > 0:
                candidates.append(letter)
        if self.words[array_pos]:
            candidates.append(' ')
        return candidates
    
    def _make_move(self, candidate, solution, array_pos, phrase):
        if candidate == ' ':
            solution.append(' ')
            array_pos = 0
        else:
            solution.append(candidate)
            phrase.dictionary[candidate] = phrase.dictionary[candidate] - 1
            array_pos = self.node_list[array_pos][candidate]
        return array_pos
    
    def _unmake_move(self, solution, array_pos, candidate, phrase):
        solution.pop()
        array_pos = self.back_pointers[array_pos]
        if candidate != ' ':
            phrase.dictionary[candidate] = phrase.dictionary[candidate] + 1
        return array_pos
        
    def _is_solution(self, phrase, solution):
        if len(self._remove_spaces("".join(solution))) == len(phrase.stripped):
            return True
        else:
            return False
    
    def _remove_spaces(self, phrase):
        stripped_phrase = []
        for char in phrase:
            if char != ' ':
                stripped_phrase.append(char)
        return "".join(stripped_phrase)
    
    def _process_solution(self, phrase, solution):
        self.anagrams.append("".join(solution))
        print "{} is an anagram of {}".format("".join(solution), phrase.full) 
        
class Phrase():
    def __init__(self, phrase):
        self.full = phrase
        self.stripped = self._remove_spaces(self.full)
        self.dictionary = self._make_dictionary(self.stripped)
    
    def _remove_spaces(self, phrase):
        stripped_phrase = []
        for char in phrase:
            if char != ' ':
                stripped_phrase.append(char)
        return "".join(stripped_phrase)
    
    def _make_dictionary(self, l):
        d = {letter.name:0 for letter in Alphabet}
        for letter in l:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1 
        return d

@unique
class Alphabet(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
    
    
if __name__ == "__main__":
	import os, sys
	if len(sys.argv) > 1:
		path = os.path.join(*sys.argv[1:])
	else:
		path = "test_dictionary.txt"
	anagram_dictionary = AnagramDictionary(path)
	phrase = Phrase("redefined frights")
	anagram_dictionary.find_anagrams(phrase)

