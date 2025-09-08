# reference: https://github.com/Exorust/TorchLeet/blob/main/e2/custom-dataset.ipynb 

"""
Problem Statement
You are tasked with creating a custom Dataset and Dataloader in PyTorch to load data from a given data.csv file. The loaded data will be used to run a pre-implemented linear regression model.

Requirements

Dataset Class:
  Implement a class CustomDataset that:
    Reads data from a provided data.csv file.
    Stores the features (X) and target values (Y) separately.
    Implements PyTorch's __len__ and __getitem__ methods for indexing.
  Dataloader:
    Use PyTorch's DataLoader to create an iterable for batch loading the dataset.
    Support user-defined batch sizes and shuffling of the data.
"""

import torch
import pandas as pd

torch.manual_seed(42)
X = torch.rand(100, 1) * 10
y = 2*X + 3 + torch.rand(100, 1)

data = torch.cat((X, y), dim=1)
df = pd.DataFrame(data.numpy(), columns=['X', 'y'])
df.to_csv('data.csv', index=False)

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader


class LinearRegressionDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.X = torch.tensor(self.data['X'].values, dtype=torch.float32).view(-1, 1)
        self.y = torch.tensor(self.data['y'].values, dtype=torch.float32).view(-1, 1)

    def __getitem__(self, ind):
        return self.X[ind], self.y[ind]

    def __len__(self):
        return len(self.data)


dataset = LinearRegressionDataset('data.csv')
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)


# Define the Linear Regression Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # Single input and single output

    def forward(self, x):
        return self.linear(x)

# Initialize the model, loss function, and optimizer
model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
epochs = 1000
for epoch in range(epochs):
    for batch_X, batch_y in dataloader:
        # Forward pass
        predictions = model(batch_X)
        loss = criterion(predictions, batch_y)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Log progress every 100 epochs
    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")


# Display the learned parameters
[w, b] = model.linear.parameters()
print(f"Learned weight: {w.item():.4f}, Learned bias: {b.item():.4f}")

# Testing on new data
X_test = torch.tensor([[4.0], [7.0]])
with torch.no_grad():
    predictions = model(X_test)
    print(f"Predictions for {X_test.tolist()}: {predictions.tolist()}")

