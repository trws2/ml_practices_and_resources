import numpy as np

# def self_attention(Q, K, V):
    
#     def softmax(x):
#         return np.exp(x)/sum(np.exp(x))        

#     d = len(Q)
#     tmp = np.dot(np.transpose(Q), K) * 1/np.sqrt(d)
#     for i in range(len(tmp)):
#         tmp[i] = softmax(tmp[i])
    
#     attention_output = np.dot(tmp, V)
# 	return attention_output


# def compute_qkv(X, W_q, W_k, W_v):
#     Q = np.dot(X, W_q)
#     K = np.dot(X, W_k)
#     V = np.dot(X, W_v)
#     return Q, K, V


def compute_qkv(X, W_q, W_k, W_v):
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V    

def softmax(mat):
    for i in range(len(mat)):
        mat[i] = np.exp(mat[i])/sum(np.exp(mat[i]))
    return mat

def self_attention(Q, K, V):
    d = Q.shape[1]
    tmp = np.dot(Q, K.T)

    attention_output = np.dot(softmax(np.dot(Q, K.T)/np.sqrt(d)), V)
    return attention_output


X = np.array([[1, 0, 1], [0, 1, 0]])
W_q = np.array([[1, 0, 2], [0, 1, 1], [0, 1, 5]])
W_k = np.array([[1, 0, 1], [0, 1, 2], [0, 1, 1]])
W_v = np.array([[1, 2, 3], [3, 4, 5], [3, 4, 0]])
Q, K, V = compute_qkv(X, W_q, W_k, W_v)
output = self_attention(Q, K, V)
print(output)

