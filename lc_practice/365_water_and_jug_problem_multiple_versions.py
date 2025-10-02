def measure_water_dfs(capacities, target):
    """
    Find a sequence of operations to measure exactly 'target' gallons.
    
    Args:
        capacities: list of bucket capacities [b_1, b_2, ..., b_n]
        target: target volume to measure
    
    Returns:
        list of operations if possible, None otherwise
    """
    n = len(capacities)
    visited = set()
    
    def state_to_tuple(state):
        return tuple(state)
    
    def dfs(state, path):
        # Check if we've reached the target in any bucket
        if target in state:
            return path
        
        state_tuple = state_to_tuple(state)
        if state_tuple in visited:
            return None
        
        visited.add(state_tuple)
        
        # Try all possible operations
        
        # Operation 1: Fill bucket i to capacity
        for i in range(n):
            if state[i] < capacities[i]:
                new_state = state[:]
                new_state[i] = capacities[i]
                result = dfs(new_state, path + [f"Fill bucket {i+1} to {capacities[i]} gallons: {new_state}"])
                if result is not None:
                    return result
        
        # Operation 2: Pour from bucket i to bucket j
        for i in range(n):
            for j in range(n):
                if i != j and state[i] > 0:
                    # Amount we can pour is limited by source and destination capacity
                    amount = min(state[i], capacities[j] - state[j])
                    if amount > 0:
                        new_state = state[:]
                        new_state[i] -= amount
                        new_state[j] += amount
                        result = dfs(new_state, path + [f"Pour {amount} gallons from bucket {i+1} to bucket {j+1}: {new_state}"])
                        if result is not None:
                            return result
        
        # Operation 3: Dump bucket i completely
        for i in range(n):
            if state[i] > 0:
                new_state = state[:]
                new_state[i] = 0
                result = dfs(new_state, path + [f"Dump bucket {i+1}: {new_state}"])
                if result is not None:
                    return result
        
        return None
    
    # Start with all buckets empty
    initial_state = [0] * n
    result = dfs(initial_state, [f"Initial state: {initial_state}"])
    
    return result


# Example usage
if __name__ == "__main__":
    # Example 1: Two buckets with capacities 3 and 5, target 4
    print("Example 1: Buckets [3, 5], Target = 4")
    print("=" * 50)
    capacities = [3, 5]
    target = 4
    operations = measure_water_dfs(capacities, target)
    
    if operations:
        print("Solution found!")
        for i, op in enumerate(operations):
            print(f"{i}. {op}")
    else:
        print("No solution found.")
    
    print("\n" + "=" * 50)
    
    # Example 2: Three buckets
    print("\nExample 2: Buckets [2, 3, 5], Target = 4")
    print("=" * 50)
    capacities = [2, 3, 5]
    target = 4
    operations = measure_water_dfs(capacities, target)
    
    if operations:
        print("Solution found!")
        for i, op in enumerate(operations):
            print(f"{i}. {op}")
    else:
        print("No solution found.")
    
    print("\n" + "=" * 50)
    
    # Example 3: Impossible case
    print("\nExample 3: Buckets [2, 4], Target = 3 (Impossible)")
    print("=" * 50)
    capacities = [2, 4]
    target = 3
    operations = measure_water_dfs(capacities, target)
    
    if operations:
        print("Solution found!")
        for i, op in enumerate(operations):
            print(f"{i}. {op}")
    else:
        print("No solution found (gcd(2,4) = 2, and 3 is not divisible by 2).")
