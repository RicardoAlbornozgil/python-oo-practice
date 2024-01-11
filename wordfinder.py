"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    235886 words read
        
    """
    def __init__(self, file_path):
        """Constructor for WordFinder, makes list of words in file and prints total elements"""
        self.words = self.read_words_from_file(file_path)
        print(f"{len(self.words)} words read")

    def read_words_from_file(self, file_path):
        """Reads file and returns list by line"""
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Generates a random choice for the words in list"""
        return random.choice(self.words)

    