# Sentiment-Analysis
Sentiment analysis using Twitter dataset

# Twitter Sentiment Analysis using VADER

## 📂 Dataset
This project uses two datasets:
- `twitter_training.csv` (large training set)
- `twitter_validation.csv` (used for evaluation)

Each dataset contains tweets labeled with sentiments: `Positive`, `Negative`, `Neutral`, and `Irrelevant`.
You can download using this link https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis
## 🧠 What is VADER?
**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a rule-based sentiment analysis tool specifically designed for social media text. It’s part of the `nltk` library and excels at analyzing short, informal text like tweets, using a lexicon and heuristics to assign sentiment scores.

VADER outputs:
- **Positive**, **Negative**, **Neutral** scores
- A **compound score** summarizing overall sentiment

## 🚀 How to Run

### 1. 📦 Install Dependencies
pip install pandas nltk

### 2. Run Sentiment_analysis_vader.py file
python Sentiment_analysis_vader.py


