# source: https://www.deep-ml.com/problems/85

import numpy as np

def pos_encoding(position: int, d_model: int):
    final_pos_encoding = np.zeros((position, d_model))
    for pos in range(position):
        n = 10000
        pos_encoding = np.zeros(d_model)
        even = np.array([x for x in range(0, d_model, 2)])
        even = even / d_model
        odd = np.array([x for x in range(1, d_model, 2)])
        odd = odd / d_model
        pos_encoding[::2] = np.sin(pos / np.power(n, even))
        pos_encoding[1::2] = np.cos(pos / np.power(n, even))
        final_pos_encoding[pos] = pos_encoding

    ret = np.float16(final_pos_encoding)
    return ret

if __name__ == "__main__":
    print(pos_encoding(2, 8))

