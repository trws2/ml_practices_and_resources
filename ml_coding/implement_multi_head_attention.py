# newer implementation

import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
	Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V

def self_attention(Q, K, V):
    def softmax(M):
        # note that it is subtracting max that prevents overflow
        tmp = M - np.max(M, axis=1, keepdims=True)
        tmp = np.exp(tmp)
        return tmp / np.sum(tmp, axis=1, keepdims=True)
    d_k = np.sqrt(Q.shape[1])
    attention = softmax(np.dot(Q, K.T) / np.sqrt(d_k))
    return np.dot(attention, V)

def multi_head_attention(Q, K, V, n_heads):
    d = Q.shape[1]
    d_k = d // n_heads

    Q_transpose = Q.reshape(Q.shape[0], n_heads, d_k).transpose(1, 0, 2)
    K_transpose = K.reshape(K.shape[0], n_heads, d_k).transpose(1, 0, 2)
    V_transpose = V.reshape(V.shape[0], n_heads, d_k).transpose(1, 0, 2)

    attn_list = []
	for i in range(n_heads):
        attn_list.append(self_attention(Q_transpose[i], K_transpose[i], V_transpose[i]))
    attn = np.concatenate(attn_list, axis=1)
    return attn


# older implementation

import numpy as np
from typing import Tuple, List

def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V


def self_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
    d_k = Q.shape[1]
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    score_max = np.max(scores, axis=1, keepdims=True)
    attention_weights = np.exp(scores - score_max) / np.sum(np.exp(scores - score_max), axis=1, keepdims=True)
    attention_output = np.dot(attention_weights, V)
    return attention_output


def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, n_heads: int) -> np.ndarray:
    d_model = Q.shape[1] 
    assert d_model % n_heads == 0 
    d_k = d_model // n_heads 

    Q_reshaped = Q.reshape(Q.shape[0], n_heads, d_k).transpose(1, 0, 2) 
    K_reshaped = K.reshape(K.shape[0], n_heads, d_k).transpose(1, 0, 2) 
    V_reshaped = V.reshape(V.shape[0], n_heads, d_k).transpose(1, 0, 2) 

    attentions = []

    for i in range(n_heads):
        attn = self_attention(Q_reshaped[i], K_reshaped[i], V_reshaped[i]) 
        attentions.append(attn) 

    attention_output = np.concatenate(attentions, axis=-1) 
    return attention_output 
