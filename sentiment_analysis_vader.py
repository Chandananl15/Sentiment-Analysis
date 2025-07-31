import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

# Download VADER lexicon if not already present
nltk.download('vader_lexicon')

# Initialize VADER analyzer
sia = SentimentIntensityAnalyzer()

# Files to process
files = {
    "training": "C:\\Users\\Mcs\\Desktop\\sentiment\\data\\twitter_training.csv",
    "validation": "C:\\Users\\Mcs\\Desktop\\sentiment\\data\\twitter_validation.csv"
}

# Create output folder
os.makedirs("results", exist_ok=True)

# Function to apply VADER sentiment analysis
def analyze_sentiment(text):
    if pd.isna(text):
        return 0.0
    score = sia.polarity_scores(str(text))['compound']
    return score

# Function to classify compound score
def classify_sentiment(score):
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Process each file
for name, path in files.items():
    print(f"🔍 Processing {name} dataset...")
    
    df = pd.read_csv(path, header=None, names=["tweet_id", "entity", "label", "text"])
    
    # Apply VADER
    df['vader_score'] = df['text'].apply(analyze_sentiment)
    df['vader_label'] = df['vader_score'].apply(classify_sentiment)
    
    # Save result
    output_file = f"results/{name}_with_sentiment.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Saved: {output_file}")
