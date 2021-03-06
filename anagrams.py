from enum import Enum, unique
import logging, os, sys
'''
Created on Oct 26, 2015

@author: templetonc
'''

class Node():
    def __init__(self, forward={}, back=None, word=None):
        self.forward = forward
        self.back = back
        self.word = word
        
    def __repr__(self):
        return "Node({}, {}, {})".format(self.forward, self.back, self.word)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    

class AnagramDictionary():
    def __init__(self, path=None):
        self.start_node = Node()
        self.node_list = [self.start_node]
        self.anagrams = []
        self.logger1 = logging.getLogger("setup")
        self.logger2 = logging.getLogger("lookup")
        if path:
            self.set_dictionary(path)
                
    def set_dictionary(self, path, additive=False):
        if additive == False:
            self.clear_dictionary() 
        with open(path, 'rb') as infile:
                for line in infile:
                    word = line.strip()
                    if self._is_alphabetical(word) and len(word) > 3:
                        self._insert_word(word)
    
    def clear_dictionary(self):
        while len(self.node_list) > 1 : self.node_list.pop()
        self.start_node.forward.clear()
                
    def _is_alphabetical(self, word):
        alphabetical = True
        letters = [letter.name for letter in Alphabet]
        for letter in word:
            if letter not in letters:
                alphabetical = False
        return alphabetical
    
    def _insert_word(self, word, word_pos=0, array_pos=0):
        if word_pos == len(word):
            self.logger1.debug("word = {}".format(word))
            self.node_list[array_pos].word = word
        else:
            letter = word[word_pos]
            if letter in self.node_list[array_pos].forward:
                self.logger1.debug("letter = {}. recursively calling _insert_word".format(letter))
                self._insert_word(word, word_pos + 1, self.node_list[array_pos].forward[letter])
            else:
                for letter in word[word_pos:len(word) - 1]:
                    self.logger1.debug("word_pos, array_pos, letter = {}, {}, {}".format(word_pos, array_pos, letter))
                    self.node_list[array_pos].forward[letter] = len(self.node_list)
                    back = array_pos
                    array_pos = len(self.node_list)
                    self.node_list.append(Node({}, back, None))
                letter = word[len(word) - 1]
                self.logger1.debug ("word_pos, array_pos, letter = {}, {}, {}".format(word_pos, array_pos, letter))
                self.node_list[array_pos].forward[letter] = len(self.node_list)
                back = array_pos
                array_pos = len(self.node_list)
                self.node_list.append(Node({}, back, word))
                
    def find_anagrams(self, phrase):           
        assert isinstance(phrase, Phrase), "Argument to find_anagrams must be of type Phrase()"
        self._backtrack(phrase, [])
        
    def _backtrack(self, phrase, solution, array_pos=0):
        self.logger2.debug ("backtracking. solution is {}, array_pos is {}".format(solution, array_pos))
        if self._is_solution(phrase, solution):
            self.logger2.debug("found a possible solution")
            if self.node_list[array_pos].word:
                self.logger2.debug ("solution is a solution:")
                self._process_solution(phrase, solution)
        else:
            candidates = self._construct_candidates(phrase, array_pos)
            self.logger2.debug("chose candidates. Candidates are {}".format(candidates))
            for candidate in candidates:
                self.logger2.debug("iterating candidate loop. candidate is {}, array_pos is {}".format(candidate, array_pos))
                array_pos = self._make_move(candidate, solution, array_pos, phrase)
                self.logger2.debug("updated array position and chose candidate. Candidate is {}, array position is {}, solution is {}".format(candidate, array_pos, solution))
                self._backtrack(phrase, solution, array_pos)
                array_pos = self._unmake_move(solution, array_pos, candidate, phrase)
     
    def _construct_candidates(self, phrase, array_pos):
        candidates = []
        for letter in self.node_list[array_pos].forward:
            if phrase.dictionary[letter] > 0:
                candidates.append(letter)
        if self.node_list[array_pos].word:
            candidates.append(' ')
        return candidates
    
    def _make_move(self, candidate, solution, array_pos, phrase):
        if candidate == ' ':
            solution.append(' ')
            array_pos = 0
        else:
            solution.append(candidate)
            phrase.dictionary[candidate] = phrase.dictionary[candidate] - 1
            array_pos = self.node_list[array_pos].forward[candidate]
        return array_pos
    
    def _unmake_move(self, solution, array_pos, candidate, phrase):
        #print "unmaking move. array_pos before unmaking move is {}".format(array_pos)
        solution.pop()
        array_pos = self.node_list[array_pos].back
        if candidate != ' ':
            phrase.dictionary[candidate] = phrase.dictionary[candidate] + 1
        #print "unmade move. array_pos after unmaking move is {}".format(array_pos)
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
        #could make solution an instance of phrase
    
        
class Phrase():
    def __init__(self, phrase):
        #do some type checking
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
    levels = {"debut":logging.DEBUG,
             "info":logging.INFO,
             "warning":logging.WARNING,
             "error":logging.ERROR,
             "critical":logging.CRITICAL}
    if len(sys.argv) > 1:
         level = levels.get(sys.argv[1], logging.NOTSET)
    
    logger1 = logging.getLogger("setup")
    logger1.setLevel(logging.DEBUG)
    handler1 = logging.FileHandler("anagram_dictionary_setup.log", 'w')
    logger1.addHandler(handler1)
    
    logger2 = logging.getLogger("lookup")
    logger2.setLevel(logging.DEBUG)
    handler2 = logging.FileHandler("anagram_dictionary_lookup.log", 'w')
    logger2.addHandler(handler2)
    
    path = os.path.join("data", "wordsEn.txt")
    #path = os.path.join("test_dictionary.txt")
    print ("preparing to populate dictionary")
    anagram_dictionary = AnagramDictionary(path)
    phrase = Phrase("blue rider")
    print ("preparing to look up phrase")
    anagram_dictionary.find_anagrams(phrase)
    print ("finished")
