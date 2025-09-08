# reference: https://github.com/Exorust/TorchLeet/blob/main/e5/custon-DNN.ipynb
# The model should have:
#   An input layer connected to a hidden layer.
#   A ReLU activation function for non-linearity.
#   An output layer with a single unit for regression.

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

torch.manual_seed(42)
X = torch.rand(10, 2) * 10
y = (X[:, 0] + X[:, 1] * 2).unsqueeze(1) + torch.rand(10, 1) # add non-linear patten to the input data


class DNNModel(nn.Module):
    def __init__(self):
        super(DNNModel, self).__init__()
        self.fc1 = nn.Linear(2, 10)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


# Initialize the model, loss function, and optimizer
model = DNNModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
epochs = 1000
for epoch in range(epochs):
    # Forward pass
    predictions = model(X)
    loss = criterion(predictions, y)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Log progress every 100 epochs
    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")
        

# Testing on new data
X_test = torch.tensor([[4.0, 3.0], [7.0, 8.0]])
with torch.no_grad():
    predictions = model(X_test)
    print(f"Predictions for {X_test.tolist()}: {predictions.tolist()}")

# output
"""
Epoch [100/1000], Loss: 1.1610
Epoch [200/1000], Loss: 0.1082
Epoch [300/1000], Loss: 0.0923
Epoch [400/1000], Loss: 0.0854
Epoch [500/1000], Loss: 0.0798
Epoch [600/1000], Loss: 0.0746
Epoch [700/1000], Loss: 0.0696
Epoch [800/1000], Loss: 0.0648
Epoch [900/1000], Loss: 0.0604
Epoch [1000/1000], Loss: 0.0563
Predictions for [[4.0, 3.0], [7.0, 8.0]]: [[10.60813045501709], [23.293926239013672]]
"""

