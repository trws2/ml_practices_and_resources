import numpy as np

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    label = np.array(actual)
    pred = np.array(predicted)

    TP = sum(label[pred == 1])
    FP = sum(label[pred == 1] == 0)
    TN = sum(label[pred == 0] == 0)
    FN = sum(label[pred == 0] == 1)

    prec = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * prec * recall / (prec + recall)

    confusion_matrix = [[TP, FN], [FP, TN]]
    accuracy = (TP + TN) / (TP + FN + FP + TN)
    specificity = TN / (TN + FP)
    negativePredictive = TN / (TN + FN)

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

