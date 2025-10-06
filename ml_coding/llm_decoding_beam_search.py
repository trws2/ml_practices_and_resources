import numpy as np
from typing import Any, Tuple, List

VOCAB_SIZE = 10
STOP_TOKEN_ID = VOCAB_SIZE - 1
EPS = 1e-12

def softmax(z: np.ndarray) -> np.ndarray:
    tmp = z - np.max(z, axis=-1, keepdims=True)
    tmp = np.exp(tmp)
    prob = tmp / np.sum(tmp, axis=-1, keepdims=True)
    return prob

def beam_search(model_step: Any, start_token: int, beam_size: int, max_len: int) -> Tuple[List[int], float]:
    seq_candidates = [([start_token], 0)]
    
    for i in range(max_len):
        all_pairs = []
        for seq_pair in seq_candidates:
            seq = seq_pair[0]
            cum_log_prob = seq_pair[1]
            logits = model_step(seq)
            if len(logits) == 0:
                print(f"stop token reach, no need to check this sequence, seq={seq}, cum_log_prob={cum_log_prob}")
                all_pairs.append(seq_pair)
                continue

            probs = softmax(logits)
            log_probs = np.log(probs + EPS)
            
            # get token logit pairs
            pairs = [(seq + [token_id], (cum_log_prob + log_prob) / (len(seq) + 1)) for token_id, log_prob in enumerate(log_probs)]
            all_pairs.extend(pairs)

        # sort by commulative prob scores
        all_pairs.sort(key=lambda x : x[1], reverse=True)

        # pick top beam_size sequences and continue
        seq_candidates = all_pairs[:beam_size]

    for k, seq in enumerate(seq_candidates):
        print(f"Top {k} sequence = {seq}")

    return seq_candidates[0]


if __name__ == "__main__":
    def dummy_model_step(tokens: List[int]) -> np.ndarray:
        """Fake model that outputs random logits"""
        if tokens[-1] == STOP_TOKEN_ID:
            return np.empty(0)

        vocab_size = 10
        logits = np.random.randn(vocab_size)
        return logits

    start_token = 0
    beam_size = 3
    max_len = 100
    decoded_seq, score = beam_search(dummy_model_step, start_token, beam_size, max_len)
    print(f"Best sequence: {decoded_seq}, len={len(decoded_seq)}")
    print(f"Score: {score}")


