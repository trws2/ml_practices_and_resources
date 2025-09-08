import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer


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


# Split dataset
train_df = df[:60]
val_df = df[60:80]
test_df = df[80:]


model = SentenceTransformer(
    "Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"attn_implementation": "flash_attention_2", "device_map": "auto"},
    tokenizer_kwargs={"padding_side": "left"}
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

class PairDataset(Dataset):
    def __init__(self, df):
        self.pairs = df[["source","target"]].values
        self.labels = df["label"].to_numpy()
    def __len__(self): return len(self.labels)
    def __getitem__(self, i):
        return {
            "source": self.pairs[i][0],
            "target": self.pairs[i][1],
            "label": int(self.labels[i])
        }

train_ds = PairDataset(train_df)
test_ds = PairDataset(test_df)
train_loader = DataLoader(train_ds, batch_size=8, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=8)

# 2. Classifier head
class EmbClassifier(nn.Module):
    def __init__(self, emb_dim=1024):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(2*emb_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 2)
        )
    def forward(self, src_emb, tgt_emb):
        x = torch.cat([src_emb, tgt_emb], dim=1)
        return self.fc(x)

classifier = EmbClassifier().to(device)
optimizer = torch.optim.AdamW(classifier.parameters(), lr=1e-4)
loss_fn = nn.CrossEntropyLoss()

# 3. Training
for epoch in range(5):
    classifier.train()
    total_loss = 0
    for batch in train_loader:
        src_emb = model.encode(batch["source"], convert_to_tensor=True, device=device)
        tgt_emb = model.encode(batch["target"], convert_to_tensor=True, device=device)
        labels = torch.tensor(batch["label"], device=device)
        logits = classifier(src_emb, tgt_emb)
        loss = loss_fn(logits, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}: Loss = {total_loss/len(train_loader):.4f}")

# 4. Evaluation
classifier.eval()
all_preds, all_labels = [], []
with torch.no_grad():
    for batch in test_loader:
        src_emb = model.encode(batch["source"], convert_to_tensor=True, device=device)
        tgt_emb = model.encode(batch["target"], convert_to_tensor=True, device=device)
        logits = classifier(src_emb, tgt_emb)
        preds = logits.argmax(dim=1).cpu().numpy()
        all_preds.extend(preds)
        all_labels.extend(batch["label"])

acc = accuracy_score(all_labels, all_preds)
print(f"Test Accuracy: {acc:.4f}")
cm = confusion_matrix(all_labels, all_preds)
ConfusionMatrixDisplay(cm, display_labels=["No","Yes"]).plot(cmap=plt.cm.Blues)
plt.show()

