# source: https://www.deep-ml.com/problems/85

# newer implementation

import numpy as np

def pos_encoding(position: int, d_model: int):
    pos_encoding = np.zeros((position, d_model))

    for pos in range(position):
        even = np.array([float(x) for x in range(0, d_model, 2)])
        even /= d_model
        even = np.power(10000, even)
        val = pos / even

        encoding = np.zeros(d_model)
        encoding[::2] = np.sin(val)
        encoding[1::2] = np.cos(val)
        pos_encoding[pos] = encoding

	return np.float16(pos_encoding)



# older implementation


import numpy as np

def pos_encoding(position: int, d_model: int):
    final_pos_encoding = np.zeros((position, d_model))
    for pos in range(position):
        n = 10000
        pos_encoding = np.zeros(d_model)
        even = np.array([x for x in range(0, d_model, 2)])
        even = even / d_model

        pos_encoding[::2] = np.sin(pos / np.power(n, even))
        pos_encoding[1::2] = np.cos(pos / np.power(n, even))

        final_pos_encoding[pos] = pos_encoding

	ret = np.float16(final_pos_encoding)
	return ret

if __name__ == "__main__":
    print(pos_encoding(2, 8))

