# older implementation

# import numpy as np

# def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray):
#     Q = np.dot(X, W_q)
#     K = np.dot(X, W_k)
#     V = np.dot(X, W_v)
#     return Q, K, V

# def masked_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray) -> np.ndarray:
#     d_k = Q.shape[1]
#     scores = np.matmul(Q, K.T) / np.sqrt(d_k)
#     scores = scores + mask  # Apply mask
#     # substract max score for numerial stability. The final attention weights are the same with
#     # without subtraction.
#     attention_weights = np.exp(scores - np.max(scores, axis=1, keepdims=True))
#     attention_weights = attention_weights / np.sum(attention_weights, axis=1, keepdims=True)
#     return np.matmul(attention_weights, V)


# newer implementation
import numpy as np

def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray):
	"""
	Compute Query (Q), Key (K), and Value (V) matrices.
	"""
	return np.dot(X, W_q), np.dot(X, W_k), np.dot(X, W_v)

def masked_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray) -> np.ndarray:
	"""
	Compute masked self-attention.
	"""
	def softmax(M):
		M = M - np.max(M, axis=1, keepdims=True)
		M = np.exp(M)
		M = M / np.sum(M, axis=1, keepdims=True)
		return M
	
	d_k = Q.shape[1]
	M = np.dot(Q, K.T) / np.sqrt(d_k)
	M = softmax(M + mask)
	return np.dot(M, V)


np.random.seed(42)
X = np.arange(48).reshape(6,8)
X = np.random.permutation(X.flatten()).reshape(6, 8)
mask = np.triu(np.ones((6, 6))*(-np.inf), k=1)
W_q = np.random.randint(0,4,size=(8,8))
W_k = np.random.randint(0,5,size=(8,8))
W_v = np.random.randint(0,6,size=(8,8))
Q, K, V = compute_qkv(X, W_q, W_k, W_v)
print(masked_attention(Q, K, V, mask))


