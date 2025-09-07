# runtime: 
# space: O(number_of_chars_in_all_words)

class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[-1] = None

    def search(self, word: str) -> bool:
        def search_helper(word, cur_map, cur_ind):
            if cur_ind == len(word):
                return -1 in cur_map
            c = word[cur_ind]
            if c == '.':
                if (len(cur_map) == 0) or ((len(cur_map) == 1) and (-1 in cur_map)):
                    return False
                else:
                    for new_c, new_map in cur_map.items():
                        if new_c == -1:
                            continue
                        res = search_helper(word, new_map, cur_ind+1)
                        if res:
                            return True
                    return False
            if c not in cur_map:
                return False
            return search_helper(word, cur_map[c], cur_ind+1)
        
        return search_helper(word, self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
