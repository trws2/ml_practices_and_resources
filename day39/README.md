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
where $`p_{base} = \frac{1}{N} \sum_{i}^{N} y_i`$ is the positive class probability from training samples.
- you can reference [A Guide To Normalized Cross Entropy](https://forecastegy.com/posts/normalized-cross-entropy/) for more details
- [DLRM: An advanced, open source deep learning recommendation model](https://ai.meta.com/blog/dlrm-an-advanced-open-source-deep-learning-recommendation-model/)
  - [repo](https://github.com/facebookresearch/dlrm)
- completed machine learning system design from educative.io and obtained the certificate.
  - ML system design template
    - Problem statement and metrics
      - Problem Statement
      - Metric design and requirements
        - Metrics
          - offline metrics
          - online metrics
        - Requirements
          - Training
          - Inference
      - Summary 
    - Model
      - Feature engineering
      - Training data
      - Model
        - Selection
        - Evaluation
    - System Design
      - Calculation and estimation
        - Assumptions
        - Data size
        - Scale
      - High level design
      - Scale the design
      - Follow up questions
      - Summary
