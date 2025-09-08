
import torch
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW, get_linear_schedule_with_warmup, Trainer, TrainingArguments
from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

data = []

for i in range(100):
    ## Read original file
    original = open('./Webis-CPC-11/' + str(i+1) + '-original.txt', 'r')
    original_text = original.read()

    ## Read candidate file
    candidate = open('./Webis-CPC-11/' + str(i+1) + '-paraphrase.txt', 'r')
    candidate_text = candidate.read()

    ## Read metadata file
    with open('./Webis-CPC-11/' + str(i+1) + '-metadata.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(':')
            if key == 'Paraphrase':
                verdict = value.strip()
    
    sample = [original_text, candidate_text, verdict]
    data.append([s.replace('\n', ' ') for s in sample])

df = pd.DataFrame(np.array(data), columns = ["source", "target", "label"])
df["label"] = df["label"].map({"Yes": 1, "No": 0})


print(df.shape)
print(df.head())

train_df = df[:60]
val_df = df[60:80]
test_df = df[80:]

tokenizer = AutoTokenizer.from_pretrained("EducativeCS2023/roberta-similarity")
train_encodings = tokenizer(train_df["source"].tolist(), train_df["target"].tolist(), truncation=True, padding=True)
val_encodings = tokenizer(val_df["source"].tolist(), val_df["target"].tolist(), truncation=True, padding=True)
test_encodings = tokenizer(test_df["source"].tolist(), test_df["target"].tolist(), truncation=True, padding=True)


class ParaphraseDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


train_dataset = ParaphraseDataset(train_encodings, train_df["label"].tolist())
val_dataset = ParaphraseDataset(val_encodings, val_df["label"].tolist())
test_dataset = ParaphraseDataset(test_encodings, test_df["label"].tolist())

model = AutoModelForSequenceClassification.from_pretrained('EducativeCS2023/roberta-similarity', num_labels=2)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)

print("A--")
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=0,
    weight_decay=0.01,
    learning_rate=5e-5,
    logging_dir="./logs",
    logging_steps=10,
    eval_strategy="steps",
    save_total_limit=3,
    load_best_model_at_end=True
)

print("B--")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=lambda data: {
        'input_ids': torch.stack([item['input_ids'] for item in data]),
        'attention_mask': torch.stack([item['attention_mask'] for item in data]),
        'labels': torch.tensor([item['labels'] for item in data])
    },
    compute_metrics=lambda pred: {
        'accuracy': accuracy_score(pred.label_ids, pred.predictions.argmax(-1))
    }
)

print("C--")
trainer.train()

print("D--")
# Get the predicted labels for the test dataset
predictions = trainer.predict(test_dataset)
predicted_labels = np.argmax(predictions.predictions, axis=1)

# Get the true labels for the test dataset
true_labels = test_df['label'].tolist()

print('Accuracy:', accuracy_score(true_labels, predicted_labels))


# Compute the confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Display the confusion matrix
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = [False, True])
cm_display.plot()
plt.show()

