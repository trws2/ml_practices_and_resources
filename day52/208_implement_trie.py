# runtime: O(|max_word_length|)
# space: O(|max_word_length| x |nums_of_words|)

# newer implementation

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[-1] = None

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False

        if -1 in cur:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False

        return True



# older implementation
class Trie:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
