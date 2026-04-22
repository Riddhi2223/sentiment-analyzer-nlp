from datasets import load_dataset
from analyzer import analyze
from sklearn.metrics import classification_report, accuracy_score

# Load SST-2 validation dataset
dataset = load_dataset("sst2", split="validation")

true_labels = []
pred_labels = []

# Extract all sentences first (for clarity)
sentences = [row["sentence"] for row in dataset]

# Run predictions
for i, text in enumerate(sentences):
    # True label
    true = "Positive" if dataset[i]["label"] == 1 else "Negative"

    # Model prediction
    result = analyze(text)
    pred = result["sentiment"]

    # Convert Neutral → Negative (since SST-2 is binary)
    if pred == "Neutral":
        pred = "Negative"

    true_labels.append(true)
    pred_labels.append(pred)

# Print evaluation metrics
print("\nClassification Report:\n")
print(classification_report(true_labels, pred_labels))

print("Accuracy:", round(accuracy_score(true_labels, pred_labels), 4))
print("Total samples:", len(true_labels))