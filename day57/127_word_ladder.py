# runtime: O(26 x n x m x m) = O(n x m^2), where n = |words| and m = |source| (|source| == |target|)
# space: O(n x m)

from typing import List
from collections import deque

def shortestWordEditPath(source: str, target: str, words: List[str]) -> int:
	if source == target:
		return 0

	st = set(words)

	res = -1

	queue = deque()
	queue.append(source)

	while len(queue) > 0:
		res += 1

		# iterate over all words at the same level
		for _ in range(len(queue)):
			word = queue.popleft()

			for j in range(len(word)):
				ch = word[j]

				for c in range(ord('a'), ord('z')+1):
					new_word = word[:j] + chr(c) + word[j+1:]
				
					if new_word not in st:
						continue
				
					if new_word == target:
						return res + 1

					st.remove(new_word)

					queue.append(new_word)

	return -1


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

res = shortestWordEditPath(source, target, words)
print(res)



