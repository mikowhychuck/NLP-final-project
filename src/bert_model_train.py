from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.model_selection import train_test_split
import numpy as np
import torch

with open("data/descriptions.txt", "r", encoding="utf-8") as desc_file:
    descriptions = desc_file.readlines()

with open("data/breeds.txt", "r", encoding="utf-8") as breeds_file:
    breeds = breeds_file.readlines()

descriptions = [desc.strip() for desc in descriptions]
breeds = [breed.strip() for breed in breeds]

data = {"text": descriptions, "label": breeds}
labels_set = sorted(set(breeds))
label_to_id = {label: idx for idx, label in enumerate(labels_set)}
id_to_label = {idx: label for label, idx in label_to_id.items()}
data["label"] = [label_to_id[label] for label in breeds]

train_texts, val_texts, train_labels, val_labels = train_test_split(
    data["text"], data["label"], test_size=0.2, stratify=data["label"], random_state=42
)

train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels})
val_dataset = Dataset.from_dict({"text": val_texts, "label": val_labels})

model_name = "sdadas/polish-roberta-base-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=64)

train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

train_dataset = train_dataset.rename_column("label", "labels")
val_dataset = val_dataset.rename_column("label", "labels")

train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
val_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(label_to_id))

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=3e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=20,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    save_total_limit=2,
    no_cuda=True,
)

from sklearn.metrics import accuracy_score, f1_score

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average="weighted")
    return {"accuracy": acc, "f1": f1}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

trainer.train()

results = trainer.evaluate()
print("Results:", results)

model.config.id2label = id_to_label
model.config.label2id = label_to_id
model.save_pretrained("./dog_breed_classifier")
tokenizer.save_pretrained("./dog_breed_classifier")
