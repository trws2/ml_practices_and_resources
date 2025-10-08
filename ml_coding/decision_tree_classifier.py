# reference: https://github.com/Suji04/ML_from_Scratch/blob/master/decision%20tree%20classification.ipynb

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, info_gain=None, value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.info_gain = info_gain
        
        # for leaf node
        self.value = value

class DecisionTree:
    def __init__(self, min_sample_split=2, max_depth=2):
        pass

    def build_tree(self, dataset, curr_depth=0):
        pass

    def get_best_split(self, dataset, num_samples, num_features):
        pass

    def split(self, dataset, feature_index, threshold):
        pass

    def information_gain(self, parent, l_child, r_child, mode="entropy"):
        pass

    def entropy(self, y):
        pass

    def gini_index(self, y):
        pass

    def calculate_leaf_value(self, y):
        pass

    def print_tree(self, tree=None, indent="  "):
        pass

    def fit(self, X, Y):
        pass

    def predict(self, X):
        pass

    def make_prediction(self, X, tree):
        pass


if __name__ == "__main__":
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']
    data = pd.read_csv("iris.csv", skiprows=1, header=None, names=col_names)
    print(data)

    X = data.iloc[:, :-1].values
    Y = data.iloc[:, -1-.values.reshape(-1, 1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=41)

    classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
    classifier.fit(X_train,Y_train)
    classifier.print_tree()    

