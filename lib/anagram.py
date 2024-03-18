# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []

        for anagram in words:
            if sorted(self.word) == sorted(anagram) and self.word != anagram:
                matches.append(anagram)

        return matches