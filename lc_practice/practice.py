# Award Budget Cuts problem

from typing import List

def find_grants_cap(grantsArray: List[int], newBudget: int) -> float:
    grantsArray.sort()
    lower_bound = 0
    upper_bound = newBudget
    num_grants = len(grantsArray)
    remaining_grants = num_grants
    prefix_sum = 0
    prev_grant = 0
    for grant in grantsArray:
        prefix_sum += prev_grant
        total = grant * remaining_grants
        prev_grant = grant
        new_total = prefix_sum + total

        if new_total < newBudget:
            remaining_grants -= 1            
            lower_bound = grant
            continue
        if new_total >= newBudget:
            res = (newBudget - prefix_sum) / remaining_grants
            break

    return res


res = find_grants_cap(grantsArray = [2, 100, 50, 120, 1000], newBudget = 190)
print(f"res = {res}")

