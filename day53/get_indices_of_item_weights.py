from typing import List

def get_indices_of_item_weights(arr: List[int], limit: int) -> List[int]:
    #arr = [2,5,5,3] lim = 8 | op/ - [2,1]
    
    # map = {2: (6, 0), 5: (3, 2), 3: (5, 1)}
                                   # ^. :   
    # [(6,0), (5,1), (3,2)]
    # [2, 1]

    remainer_map = {}
    for ind, num in enumerate(arr):
        remainer = limit - num
        if remainer in remainer_map:
            return [ind, remainer_map[remainer]]
        remainer_map[num] = ind

    return []


res = get_indices_of_item_weights([2,5,5,3], 8)
print(res)

res = get_indices_of_item_weights([4, 6, 10, 15, 16], 21)
print(res)

# runtime: O(n)
# space: O(n)

