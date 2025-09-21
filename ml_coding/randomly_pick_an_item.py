import random
from typing import List, Tuple
from collections import Counter

def pick_item(items: List[Tuple[str, int]]) -> str:
    if not items:
        raise ValueError(f"items must not be empty {items}")

    total_weights = sum([x[1] for x in items])
    ran_number = random.uniform(0, total_weights)

    cum_sum = 0
    for name, weight in items:
        cum_sum += weight
        if ran_number < cum_sum:
            return name
    return items[-1][0]


def test_pick_item():
    """Comprehensive test suite for pick_item function"""
    
    print("=== Testing pick_item function ===\n")
    
    # Test 1: Basic functionality
    print("Test 1: Basic two-item selection")
    random.seed(42)
    items = [("Apple", 1), ("Banana", 3)]
    result = pick_item(items)
    print(f"Items: {items}")
    print(f"Result: {result}")
    print()
    
    # Test 2: Single item
    print("Test 2: Single item (should always return that item)")
    single_item = [("Only", 5)]
    results = [pick_item(single_item) for _ in range(5)]
    print(f"Items: {single_item}")
    print(f"5 picks: {results}")
    print()
    
    # Test 3: Equal weights
    print("Test 3: Equal weights distribution")
    random.seed(123)
    equal_items = [("A", 2), ("B", 2), ("C", 2)]
    picks = [pick_item(equal_items) for _ in range(300)]
    counter = Counter(picks)
    print(f"Items: {equal_items}")
    print(f"Distribution over 300 picks: {dict(counter)}")
    print()
    
    # Test 4: Heavily skewed weights
    print("Test 4: Heavily skewed weights")
    random.seed(456)
    skewed_items = [("Rare", 1), ("Common", 99)]
    picks = [pick_item(skewed_items) for _ in range(1000)]
    counter = Counter(picks)
    print(f"Items: {skewed_items}")
    print(f"Distribution over 1000 picks: {dict(counter)}")
    print(f"Expected ~1% Rare, ~99% Common")
    print()
    
    # Test 5: Many items with different weights
    print("Test 5: Multiple items with varied weights")
    random.seed(789)
    multi_items = [
        ("Ultra Rare", 1),
        ("Rare", 5),
        ("Uncommon", 15),
        ("Common", 30),
        ("Very Common", 49)
    ]
    picks = [pick_item(multi_items) for _ in range(2000)]
    counter = Counter(picks)
    print(f"Items: {multi_items}")
    print("Distribution over 2000 picks:")
    total_weight = sum(w for _, w in multi_items)
    for item, weight in multi_items:
        expected_pct = (weight / total_weight) * 100
        actual_count = counter.get(item, 0)
        actual_pct = (actual_count / 2000) * 100
        print(f"  {item}: {actual_count} picks ({actual_pct:.1f}%, expected {expected_pct:.1f}%)")
    print()
    
    # Test 6: Edge case - very large weights
    print("Test 6: Large weight values")
    random.seed(101112)
    large_items = [("Small", 1000000), ("Large", 2000000)]
    picks = [pick_item(large_items) for _ in range(300)]
    counter = Counter(picks)
    print(f"Items: {large_items}")
    print(f"Distribution over 300 picks: {dict(counter)}")
    print()
    
    # Test 7: Error cases
    print("Test 7: Error handling")
    
    # Empty list
    try:
        pick_item([])
        print("ERROR: Should have raised ValueError for empty list")
    except ValueError as e:
        print(f"✓ Correctly caught empty list: {e}")
    
    # Zero weight
    try:
        pick_item([("Item", 0)])
        print("ERROR: Should have raised ValueError for zero weight")
    except ValueError as e:
        print(f"✓ Correctly caught zero weight: {e}")
    
    # Negative weight  
    try:
        pick_item([("Good", 5), ("Bad", -1)])
        print("ERROR: Should have raised ValueError for negative weight")
    except ValueError as e:
        print(f"✓ Correctly caught negative weight: {e}")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    test_pick_item()
