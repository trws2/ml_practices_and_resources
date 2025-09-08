import numpy as np

def self_attention(Q, K, V):
    
    def softmax(x):
        return np.exp(x)/sum(np.exp(x))        

    d = len(Q)
    tmp = np.dot(np.transpose(Q), K) * 1/np.sqrt(d)
    for i in range(len(tmp)):
        tmp[i] = softmax(tmp[i])
    
    attention_output = np.dot(tmp, V)
	return attention_output


def compute_qkv(X, W_q, W_k, W_v):
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V



X = np.array([[1, 0], [0, 1]])
W_q = np.array([[1, 0], [0, 1]])
W_k = np.array([[1, 0], [0, 1]])
W_v = np.array([[1, 2], [3, 4]])
Q, K, V = compute_qkv(X, W_q, W_k, W_v)
output = self_attention(Q, K, V)
print(output)

