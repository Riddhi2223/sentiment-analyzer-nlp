# Sentiment Analysis using Transformers

**Riddhi Patel**  
Natural Language Processing Project · Durham College

---

## Overview

This project implements a high-performance sentiment analysis system using transformer-based NLP models. It classifies text into three categories:

- Positive  
- Neutral  
- Negative  

Built using modern NLP tools, the system delivers fast, accurate, and scalable sentiment predictions with minimal setup.

---

## Model

We use the Twitter RoBERTa sentiment model from Cardiff NLP via Hugging Face Transformers.

### Why this model?

- Trained on 58M+ tweets  
- Handles real-world informal language  
- Supports 3-class sentiment classification  
- No additional training required  

---

## Tech Stack

- Python  
- Hugging Face Transformers  
- PyTorch  
- Scikit-learn  
- Gradio  

---

## Project Structure


├── app.py # Gradio interface

├── analyzer.py # Core sentiment analysis logic
├── evaluation.py # Model evaluation (SST-2 dataset)
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## How It Works

1. User inputs text  
2. Transformer model processes it  
3. Sentiment is predicted  
4. Confidence score is returned  

---

## Run Locally
git clone https://github.com/Riddhi2223/sentiment-analyzer-nlp.git
cd sentiment-analyzer-nlp
pip install -r requirements.txt
python app.py
Example
analyze("I love this product!")
# Positive

analyze("It was okay, nothing special.")
# Neutral

analyze("Terrible experience.")
# Negative
Evaluation
Dataset: SST-2 (Stanford Sentiment Treebank)
Accuracy: ~88%
Samples tested: 50
Metrics
Accuracy score
Precision, Recall, F1-score
Challenges
Short text ambiguity
Sarcasm detection
Dataset bias (Twitter-trained model)
Future Improvements
Multilingual support
Cloud deployment (Hugging Face Spaces / Render)
Fine-tuning for higher accuracy
Conclusion

This project demonstrates how pre-trained transformers can deliver production-level NLP performance with minimal engineering effort.

Author

Riddhi Patel
Durham College
