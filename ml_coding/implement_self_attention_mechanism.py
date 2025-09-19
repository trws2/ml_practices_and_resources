import numpy as np



def compute_qkv(X, W_q, W_k, W_v):
    """
    Compute Query, Key, and Value matrices from input X and weight matrices.
    
    Args:
        X: Input matrix of shape (seq_len, d_model)
        W_q: Query weight matrix of shape (d_model, d_k)
        W_k: Key weight matrix of shape (d_model, d_k)
        W_v: Value weight matrix of shape (d_model, d_v)
    
    Returns:
        Q, K, V: Query, Key, Value matrices
    """
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V    

def softmax(x, axis=-1):
    """
    Numerically stable softmax implementation.
    
    Args:
        x: Input array
        axis: Axis along which to compute softmax
    
    Returns:
        Softmax of input array
    """
    # Subtract max for numerical stability
    x_shifted = x - np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x_shifted)
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)

def self_attention(Q, K, V):
    """
    Compute self-attention using Query, Key, and Value matrices.
    
    Args:
        Q: Query matrix of shape (seq_len, d_k)
        K: Key matrix of shape (seq_len, d_k)
        V: Value matrix of shape (seq_len, d_v)
    
    Returns:
        attention_output: Output of self-attention mechanism
    """
    d_k = Q.shape[1]  # Use d_k (dimension of keys) for scaling
    
    # Compute attention scores
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    
    # Apply softmax to get attention weights
    attention_weights = softmax(scores, axis=1)  # Apply softmax along each row
    
    # Compute final output
    attention_output = np.dot(attention_weights, V)
    
    return attention_output


X = np.array([[1, 0, 1], [0, 1, 0]])
W_q = np.array([[1, 0, 2], [0, 1, 1], [0, 1, 5]])
W_k = np.array([[1, 0, 1], [0, 1, 2], [0, 1, 1]])
W_v = np.array([[1, 2, 3], [3, 4, 5], [3, 4, 0]])
Q, K, V = compute_qkv(X, W_q, W_k, W_v)
output = self_attention(Q, K, V)
print(output)

