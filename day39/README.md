Day 37:

- cross entropy for binary classification
```math
- \sum_{i}^{N} (y_i log(p_i) + (1-y_i)log(1 - p_i))
```
where $`y_i \in \{0, 1\}`$ is the ground truth label for positive class for example i and $`p_i \in [0, 1]`$ is the positive class probability for example i.
- normalized cross entropy for binary classification
```math
\frac{\frac{1}{N}\sum_{i}^{N} (y_i log(p_i) + (1-y_i)log(1 - p_i))}{p_{base} log(p_{base}) + (1-p_{base}) log(1-p_{base})}
```
where $`p_{base} \ \frac{1}{N} \sum_{i}^{N} `$ is the positive class probability from training samples
