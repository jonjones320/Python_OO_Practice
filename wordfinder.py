import random
import re



class WordFinder:
    """
    Word Finder: finds random words from a dictionary.
    
    Attributes:
    ---------------
    file: path ex: "C:\\Users\\User\\ETC\\ETC\\words.txt"
        path to the desired file to have words found in

    Import:
    ---------------
    random: 
        uses random import to run random.choose

    """

    def __init__(self, file):
        text = (open(f"{file}").read().lower()).split(None)
        self.file = file
        self.text = text
        
    def read(self):
        print(f"Words read: {len(self.text)}")
        return self.text

    def random_word(self):
        return random.choice(self.text)
    
    
class SpecialWordFinder(WordFinder):
    """
    Subclass of WordFinder; specializes in removing extra characters and whitespace.

    Import
    ------------
    re: Regular expression
        uses re.sub to only return the ASCII alphabet (lower/uppercase), and spaces
    """
    
    def __init_subclass__(self, file):
        file = self.file
        return super().__init_subclass__(self, file)
    
    def special_read(self):
        """opens the file, retrieves the words, re.sub returns only A-Z, a-z, and spaces"""

        file = open(f"{self.file}").read()
        text = re.sub('[^a-zA-Z\']+', " ", file)
        return text
    
