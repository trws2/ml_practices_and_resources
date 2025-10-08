import numpy as np
import random
import math

def top_p_sampling(logits, p=0.9, temperature=1.0):
    def sample_a_token(probs):
        rand_num = random.uniform(0, 1)
        cumprob = 0
        for i, prob in probs:
            cumprob += prob
            if cumprob > rand_num:
                return i
        return probs[-1][0]

    tmp = np.array(logits) / temperature
    tmp = tmp - np.max(tmp, axis=-1, keepdims=True)
    tmp = np.exp(tmp)
    probs = tmp / np.sum(tmp, axis=-1, keepdims=True)
    probs = probs.tolist()
    probs = [(i, p) for i, p in enumerate(probs)]
    probs.sort(key=lambda x: x[1], reverse=True)

    cumprob = 0
    cut_off_idx = -1
    for i, prob in probs:
        cumprob += prob
        if cumprob > p:
            cut_off_idx = i+1
            break
    if cut_off_idx > 0:
        probs = probs[:cut_off_idx]
    probs_sum = sum(x[1] for x in probs)
    probs = [(i, prob/probs_sum) for i, prob in probs]
    token_idx = sample_a_token(probs)
    return token_idx


# Test the implementation
def test_top_p_sampling():
    """Test cases for top_p_sampling function"""
    
    print("Test 1: Basic functionality")
    logits1 = [2.0, 1.0, 0.5, 0.1, -1.0]
    print(f"Logits: {logits1}")
    
    # Compute expected probabilities
    exp_logits = np.exp(logits1 - np.max(logits1))
    probs = exp_logits / np.sum(exp_logits)
    print(f"Probabilities: {probs}")
    print(f"Cumulative: {np.cumsum(sorted(probs, reverse=True))}")
    
    # Run multiple samples to see distribution
    samples = [top_p_sampling(logits1, p=0.9) for _ in range(1000)]
    unique, counts = np.unique(samples, return_counts=True)
    print(f"Sample distribution (1000 samples, p=0.9):")
    for idx, count in zip(unique, counts):
        print(f"  Token {idx}: {count/10:.1f}%")
    print()
    
    print("Test 2: p=1.0 (should include all tokens)")
    logits2 = [1.0, 1.0, 1.0]
    samples2 = [top_p_sampling(logits2, p=1.0) for _ in range(300)]
    unique2, counts2 = np.unique(samples2, return_counts=True)
    print(f"Sample distribution (300 samples, p=1.0):")
    for idx, count in zip(unique2, counts2):
        print(f"  Token {idx}: {count/3:.1f}%")
    print()
    
    print("Test 3: Temperature effect")
    logits3 = [2.0, 1.0]
    print(f"Logits: {logits3}")
    
    # Low temperature (more peaked)
    samples3_low = [top_p_sampling(logits3, p=0.95, temperature=0.5) for _ in range(1000)]
    count_0_low = np.sum(np.array(samples3_low) == 0)
    print(f"Temperature=0.5: Token 0 selected {count_0_low/10:.1f}%")
    
    # High temperature (more uniform)
    samples3_high = [top_p_sampling(logits3, p=0.95, temperature=2.0) for _ in range(1000)]
    count_0_high = np.sum(np.array(samples3_high) == 0)
    print(f"Temperature=2.0: Token 0 selected {count_0_high/10:.1f}%")
    print()
    
    print("Test 4: Very small p (should still include at least one token)")
    logits4 = [2.0, 1.0, 0.5]
    sample4 = top_p_sampling(logits4, p=0.1)
    print(f"With p=0.1, sampled token: {sample4} (should be 0 most of the time)")
    samples4 = [top_p_sampling(logits4, p=0.1) for _ in range(100)]
    print(f"100 samples: {np.bincount(samples4)}")
    print()
    
    print("All tests completed!")


if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)
    
    test_top_p_sampling()
    
    print("\n" + "="*50)
    print("Example usage:")
    print("="*50)
    logits = [3.0, 2.0, 1.0, 0.5, 0.1]
    print(f"Logits: {logits}")
    for _ in range(5):
        token = top_p_sampling(logits, p=0.9, temperature=1.0)
        print(f"Sampled token: {token}")
