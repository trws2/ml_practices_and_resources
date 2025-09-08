import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    def tanh(x):
        a = np.exp(x)
        b = np.exp(-x)
        return (a - b) / (a + b)

    prev_h = initial_hidden_state
    for x in input_sequence:
        h = tanh(np.dot(Wx, x) + np.dot(Wh, prev_h) + b)
        prev_h = h

    final_hidden_state = prev_h
    return final_hidden_state

print(rnn_forward([[1.0], [2.0], [3.0]], [0.0], [[0.5]], [[0.8]], [0.0]))


