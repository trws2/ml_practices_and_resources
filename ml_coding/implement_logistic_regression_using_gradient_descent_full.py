# reference: https://www.geeksforgeeks.org/ml-logistic-regression-using-python/

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
num_examples, feature_dim = X.shape

# Convert the target variable to binary (1 for diabetes, 0 for no diabetes)
y_binary = (y > np.median(y)).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = np.append(X_train, np.ones((X_train.shape[0], 1)), axis=1)
X_test = np.append(X_test, np.ones((X_test.shape[0], 1)), axis=1)

# np.random.seed(42)
# initialize logistic regression model wneights
# include bias at the end
np.random.seed(42)
weights = np.random.rand(feature_dim+1, 1)

def sigmoid(logits):
    return 1 / (1 + np.exp(-logits))

def compute_loss_and_gradient(X, y_binary, weights):

    logits = np.dot(X, weights)
    prob = sigmoid(logits)
    num_examples = len(prob)
    loss = np.sum(y_binary * np.log(prob) + (1 - y_binary) * np.log(1 - prob)) / -num_examples 

    class1_X = X[y_binary == 1, :]
    class0_X = X[y_binary == 0, :]
    class1_prob = prob[y_binary == 1]
    class0_prob = prob[y_binary == 0]

    tmp = class0_prob * class0_X
    part1 = (1 / num_examples) * np.sum(tmp, axis=0)

    tmp = (1 - class1_prob) * class1_X
    part2 = (-1 / num_examples) * np.sum(tmp, axis=0)

    grad = part1 + part2

    grad = grad.reshape(len(grad), 1)

    return (loss, grad)

def predict(X, y, weights):
    class1_prob = sigmoid(np.dot(X, weights))
    pred = class1_prob >= 0.5
    pred = pred.reshape(1, pred.shape[0])
    pred = pred.astype(int).tolist()[0]
    acc = sum(pred == y) / len(pred)
    print(f"acc={acc*100}")


# gradient descent to train the model
learning_rate = 0.01
n_iters = 10000
prev_loss = None
for i in range(n_iters):
    loss, grad = compute_loss_and_gradient(X_train, y_train, weights)

    weights -= learning_rate * grad
    if i % 100 == 0:
        print(f"iter={i}, loss={loss}")

    if prev_loss is None:
        prev_loss = loss
    else:
        if abs((loss - prev_loss) / prev_loss) < 0.0000001:
            print("loss converges; break")
            break
        prev_loss = loss
# output final model weights
print(f"final weights weights={weights}")


predict(X_test, y_test, weights)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))
print(model)

# Print the coefficients (weights)
print("Coefficients:", model.coef_)

# Print the intercept
print("Intercept:", model.intercept_)


