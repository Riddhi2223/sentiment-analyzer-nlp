from transformers import pipeline

clf = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

def analyze(text):
    result = clf(text)[0]
    
    label_map = {
        "LABEL_0": "Negative",
        "LABEL_1": "Neutral",
        "LABEL_2": "Positive"
    }

    label = label_map[result["label"]]
    score = result["score"]

    return {
        "sentiment": label,
        "confidence": round(score, 4)
    }