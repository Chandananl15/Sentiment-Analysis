# Sentiment-Analysis  
Sentiment analysis using Twitter dataset

## 🐦 Twitter Sentiment Analysis using VADER

### 📂 Dataset  
This project uses two datasets:
- `twitter_training.csv` (large training set)  
- `twitter_validation.csv` (used for evaluation)  

Each dataset contains tweets labeled with sentiments: `Positive`, `Negative`, `Neutral`, and `Irrelevant`.

📥 You can download the datasets from [Kaggle](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)

---

### 🧠 What is VADER?  
**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a rule-based sentiment analysis tool specifically designed for social media text.  

It is part of the `nltk` library and excels at analyzing short, informal text like tweets using a lexicon and heuristics to assign sentiment scores.

VADER outputs:
- **Positive**, **Negative**, **Neutral** scores  
- A **Compound Score** summarizing overall sentiment

---

### 🚀 How to Run

#### 1. 📦 Install Dependencies
Install required libraries using pip:
```bash
pip install pandas nltk

#### 2. 📁 Create `results` Folder

Make sure to create a folder named `results` to store the analyzed CSV output:

```bash
mkdir results
```

Alternatively, the folder is automatically created by the script using:

```python
import os
os.makedirs("results", exist_ok=True)
```

#### 3. ▶️ Run the Script

Run the Python script to perform sentiment analysis:

```bash
python Sentiment_analysis_vader.py
```

---

### 📊 Output

Analyzed sentiment results will be saved inside the `results/` folder in CSV format.

---

### 🔧 Dependencies

* Python 3.x
* pandas
* nltk

