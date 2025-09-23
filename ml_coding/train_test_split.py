# source: https://www.tryexponent.com/courses/ml-coding/split-dataset-training-evaluation-testing

import random as random
from typing import List, Tuple
from collections import defaultdict


def proportional_sampling(dataset: List[Tuple[str, str]], train_fraction=0.9):
  label_to_example_map = defaultdict(list)

  for text, label in dataset:
    label_to_example_map[label].append((text, label))

  # print dataset stat
  for label, examples in label_to_example_map.items():
    print(f"label={label}, len(examples)={len(examples)}")

  train, test = [], []
  for label, examples in label_to_example_map.items():
    random.shuffle(examples)
    train_size = int(len(examples) * train_fraction)
    train.extend(examples[:train_size])
    test.extend(examples[train_size:])

  random.shuffle(train)
  random.shuffle(test)
  return train, test


def under_sampling(dataset: List[Tuple[str, str]], train_fraction=0.9):
  label_to_example_map = defaultdict(list)

  for text, label in dataset:
    label_to_example_map[label].append((text, label))

  # print dataset stat
  for label, examples in label_to_example_map.items():
    print(f"label={label}, len(examples)={len(examples)}")

  min_class_size = min(len(v) for v in label_to_example_map.values())

  train, test = [], []
  for label, examples in label_to_example_map.items():
    random.shuffle(examples)
    examples = examples[:min_class_size]
    train_size = int(len(examples) * train_fraction)
    train.extend(examples[:train_size])
    test.extend(examples[train_size:])

  # shuffle again so that training see examples randomly
  random.shuffle(train)
  random.shuffle(test)
  return train, test


if __name__ == "__main__":
    dataset = [
        ("Text1", "A"),
        ("Text2", "A"),
        ("Text3", "A"),
        ("Text4", "A"),
        ("Text5", "A"),
        ("Text6", "A"),
        ("Text7", "B"),
        ("Text8", "B"),
        ("Text9", "B"),
        ("Text10", "A"),
        ("Text11", "A"),
        ("Text12", "C"),
        ("Text13", "A"),
        ("Text14", "C"),
        ("Text15", "C"),
        ("Text16", "A"),
        ("Text17", "B"),
        ("Text18", "B")
    ]

    print("proportional_sampling ...")
    train, test = proportional_sampling(dataset)
    print(f"train={train}")
    print(f"test={test}")

    print("under_sampling ...")
    train, test = under_sampling(dataset)
    print(f"train={train}")
    print(f"test={test}")

