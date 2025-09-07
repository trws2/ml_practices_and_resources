from typing import List

def get_different_number(arr: List[int]) -> int:
    # s = set(arr)
    # for i in range(len(arr)):
    #     if i not in s:
    #         return i
    # return len(arr)

    n = len(arr)

    for i in range(n):
        while arr[i] >= 0 and arr[i] < n and arr[arr[i]] != arr[i]:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]

        for i in range(n):
            if arr[i] != i:
                return i

        return n 

