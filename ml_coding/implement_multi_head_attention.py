import numpy as np
from typing import Tuple, List

def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V

def self_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
    d_k = Q.shape[1] 
    scores = np.matmul(Q, K.T) / np.sqrt(d_k)
    score_max = np.max(scores, axis=1, keepdims=True)
    attention_weights = np.exp(scores - score_max) / np.sum(np.exp(scores - score_max), axis=1, keepdims=True)
    attention_output = np.matmul(attention_weights, V)
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
