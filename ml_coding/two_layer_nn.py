import numpy as np
import matplotlib.pyplot as plt

class TwoLayerDNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        """
        Initialize a 2-layer Deep Neural Network without bias terms.
        
        Args:
            input_size: Number of input features
            hidden_size: Number of neurons in hidden layer
            output_size: Number of output neurons
            learning_rate: Learning rate for gradient descent
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        
        # Initialize weights with Xavier/Glorot initialization
        # W1: weights from input to hidden layer (input_size x hidden_size)
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        # W2: weights from hidden to output layer (hidden_size x output_size)
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        
    def relu(self, z):
        """ReLU activation function"""
        return np.maximum(0, z)
    
    def relu_derivative(self, z):
        """Derivative of ReLU function"""
        return (z > 0).astype(float)
    
    def sigmoid(self, z):
        """Sigmoid activation function (for output layer)"""
        # Clip z to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(self, z):
        """Derivative of sigmoid function"""
        return z * (1 - z)
    
    def forward_pass(self, X):
        """
        Perform forward pass through the network.
        
        Args:
            X: Input data (batch_size x input_size)
            
        Returns:
            Dictionary containing intermediate values for backpropagation
        """
        # Hidden layer (using ReLU)
        # Z1 = X @ W1 (no bias)
        Z1 = np.dot(X, self.W1)
        A1 = self.relu(Z1)
        
        # Output layer (using Sigmoid)
        # Z2 = A1 @ W2 (no bias)
        Z2 = np.dot(A1, self.W2)
        A2 = self.sigmoid(Z2)
        
        # Store values for backpropagation
        cache = {
            'X': X,
            'Z1': Z1,
            'A1': A1,
            'Z2': Z2,
            'A2': A2
        }
        
        return A2, cache
    
    def compute_loss(self, y_true, y_pred):
        """
        Compute binary cross-entropy (log loss).
        
        Args:
            y_true: True labels (batch_size x output_size)
            y_pred: Predicted probabilities (batch_size x output_size)
            
        Returns:
            Binary cross-entropy loss
        """
        m = y_true.shape[0]
        # Clip predictions to prevent log(0)
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        
        # Binary cross-entropy formula: -1/m * sum(y*log(p) + (1-y)*log(1-p))
        loss = -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / m
        return loss
    
    def backward_pass(self, y_true, cache):
        """
        Perform backpropagation to compute gradients.
        
        Args:
            y_true: True labels (batch_size x output_size)
            cache: Dictionary containing forward pass intermediate values
            
        Returns:
            Dictionary containing gradients
        """
        m = y_true.shape[0]
        
        # Extract cached values
        X = cache['X']
        A1 = cache['A1']
        A2 = cache['A2']
        
        # Backpropagation
        # Output layer gradients (for binary cross-entropy + sigmoid)
        # Simplified gradient: dZ2 = A2 - y_true (derivative of cross-entropy with sigmoid)
        dZ2 = (A2 - y_true) / m
        dW2 = np.dot(A1.T, dZ2)
        
        # Hidden layer gradients
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * self.relu_derivative(cache['Z1'])  # Use Z1, not A1 for ReLU derivative
        dW1 = np.dot(X.T, dZ1)
        
        gradients = {
            'dW1': dW1,
            'dW2': dW2
        }
        
        return gradients
    
    def update_weights(self, gradients):
        """
        Update weights using gradient descent.
        
        Args:
            gradients: Dictionary containing gradients
        """
        self.W1 -= self.learning_rate * gradients['dW1']
        self.W2 -= self.learning_rate * gradients['dW2']
    
    def train_step(self, X, y):
        """
        Perform one training step (forward pass + backpropagation + weight update).
        
        Args:
            X: Input data (batch_size x input_size)
            y: True labels (batch_size x output_size)
            
        Returns:
            Loss value
        """
        # Forward pass
        y_pred, cache = self.forward_pass(X)
        
        # Compute loss
        loss = self.compute_loss(y, y_pred)
        
        # Backward pass
        gradients = self.backward_pass(y, cache)
        
        # Update weights
        self.update_weights(gradients)
        
        return loss
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X: Input data (batch_size x input_size)
            
        Returns:
            Predictions (batch_size x output_size)
        """
        y_pred, _ = self.forward_pass(X)
        return y_pred


# Example usage and demonstration
if __name__ == "__main__":
    # Generate synthetic dataset (XOR problem)
    np.random.seed(42)
    
    # XOR dataset
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])
    
    # Create and train the network
    dnn = TwoLayerDNN(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
    
    # Training
    epochs = 500
    losses = []
    
    print("Training 2-Layer DNN with ReLU hidden layer and Binary Cross-Entropy Loss on XOR problem...")
    print("Architecture: Input -> ReLU Hidden Layer -> Sigmoid Output")
    print("Loss Function: Binary Cross-Entropy (Log Loss)")
    print("Initial predictions:")
    initial_pred = dnn.predict(X)
    for i in range(len(X)):
        print(f"Input: {X[i]}, Target: {y[i][0]}, Prediction: {initial_pred[i][0]:.4f}")
    
    print(f"\nTraining for {epochs} epochs...")
    
    for epoch in range(epochs):
        loss = dnn.train_step(X, y)
        losses.append(loss)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.6f}")
    
    # Final predictions
    print(f"\nFinal predictions after {epochs} epochs:")
    final_pred = dnn.predict(X)
    for i in range(len(X)):
        print(f"Input: {X[i]}, Target: {y[i][0]}, Prediction: {final_pred[i][0]:.4f}")
    
    # Plot training loss
    plt.figure(figsize=(10, 6))
    plt.plot(losses)
    plt.title('Training Loss Over Time')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.show()
    
    # Display learned weights
    print(f"\nLearned Weights:")
    print(f"W1 (Input to Hidden):\n{dnn.W1}")
    print(f"W2 (Hidden to Output):\n{dnn.W2}")
    
    # Test forward pass step by step for one example
    print(f"\n--- Step-by-step Forward Pass for input [1, 0] ---")
    test_input = np.array([[1, 0]])
    
    # Manual forward pass
    Z1 = np.dot(test_input, dnn.W1)
    A1 = dnn.relu(Z1)
    Z2 = np.dot(A1, dnn.W2)
    A2 = dnn.sigmoid(Z2)
    
    print(f"Input: {test_input[0]}")
    print(f"Z1 (Hidden layer pre-activation): {Z1[0]}")
    print(f"A1 (Hidden layer activation): {A1[0]}")
    print(f"Z2 (Output layer pre-activation): {Z2[0]}")
    print(f"A2 (Final output): {A2[0]}")
    print(f"Target: {y[2][0]}")

