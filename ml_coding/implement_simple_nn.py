import numpy as np

def matrix_multiply(a, b):
    shape_a = a.shape
    shape_b = b.shape

    if a.shape[1] != b.shape[0]:
        raise Exception(f"a.shape[1]={a.shape[1]} != b.shape[0]={b.shape[0]}")

    rows = a.shape[0]
    cols = b.shape[1]
    ret = np.zeros((rows, cols))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            # ret[i,j] = a[i,:].dot(b[:,j])
            # ret[i,j] = np.dot(a[i,:], b[:,j])
            ret[i,j] = np.matmul(a[i,:], b[:,j])
    return ret


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = matrix_multiply(A, B)
print(f"Result: \n{result}")
print(f"NumPy verification: \n{A @ B}")
print("==============")



def dot_product(a, b):
    """Compute dot product of two vectors"""
    if len(a) != len(b):
        raise Exception(f"len(a)={len(a)} != len(b)={len(b)}")
    return sum([e1*e2 for e1, e2 in zip(a, b)])

def vector_norm(v):
    """Compute L2 norm of vector"""
    return np.sqrt(sum([x**2 for x in v]))


def cosine_similarity(a, b):
    """Compute cosine similarity between vectors"""
    norm_a = vector_norm(a)
    norm_b = vector_norm(b)

    print(f"a = {a}")
    print(f"b = {b}")

    print(f"norm_a = {norm_a}")
    print(f"norm_b = {norm_b}")
    print(f"dot_product(a, b) = {dot_product(a, b)}")

    return dot_product(a, b) / (norm_a * norm_b)


# Test
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Dot product: {dot_product(a, b)}")
print(f"Cosine similarity: {cosine_similarity(a, b)}")
print(f"Cosine similarity (numpy): {np.dot(np.array(a), np.array(b)) / (np.linalg.norm(np.array(a)) * np.linalg.norm(np.array(b)))}")
print("==============")




import numpy as np

class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) / np.sqrt(input_size)
        self.W2 = np.random.randn(hidden_size, output_size) / np.sqrt(hidden_size)

    def sigmoid(self, x):
        if x > 0:
            return 1 / (1 + np.exp(-x))
        else:
            return exp(x) / (exp(x) + 1)
    
    def sigmoid_derivative(self, x):
        s = sigmoid(x)
        return s * (1 - s)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        self.a2 = self.sigmoid(self.z2)
        return self.a2


# Test
nn = SimpleNN(3, 4, 2)
X = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
])
output = nn.forward(X)
print(f"Output shape: {output.shape}")
print(f"Output: \n{output}")
print("==============")




def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

def stable_relu_derivative(x):
    grad = np.zeros_like(x)
    grad[x > 0] = 1
    return grad

x = np.array([-2, -1, 0, 1, 2])
print(f"ReLU: {relu(x)}")
print(f"ReLU derivative: {relu_derivative(x)}")
print(f"Stable ReLU derivative: {stable_relu_derivative(x)}")
