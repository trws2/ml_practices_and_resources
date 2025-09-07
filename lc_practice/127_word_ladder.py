# runtime: O(M x L^2) M is the size of wordList and L is length of each word
# space: O(N + M) N for queue length and M for size of wordList

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                original = word[i]
                for ch in range(26):
                    transformed = word[:i] + chr(ord('a') + ch) + word[i+1:]
                    if transformed in wordSet:
                        wordSet.remove(transformed)
                        queue.append((transformed, steps+1))
        
        return 0

