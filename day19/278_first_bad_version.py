# runtime O(log(n))
# space O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n

        while first < last:
            mid = (first + last) // 2
            if isBadVersion(mid) == True:
                last = mid
            else:
                first = mid + 1

        return first


# n = 1, bad = 1

# first = 1
# last = 1

# loop 1: mid = 1, isBadVersion(1) == true, first = 1, last 1

# return 1, which is correct.

