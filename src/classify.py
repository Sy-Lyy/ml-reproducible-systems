import pandas as pd, os, sqlite3
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. load data (from CSV or SQLite) ---
# Option a: CSV
df = pd.read_csv("data/processed/books_clean.csv")

# option B: SQLite
# conn = sqlite3.connect("data/books.db")
# df = pd.read_sql("SELECT * FROM books;", conn)
# conn.close()

print(f"Loaded {len(df)} rows for classification")

# 2. train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    df["title"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# 3. vectorize text ---
# you can try Bag-of-Words or TF-IDF
vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

# 4. train model 
clf = LogisticRegression(max_iter=1000)
# clf = MultinomialNB()   # Try Naive Bayes too
clf.fit(X_train_vec, y_train)

# --- 5. evaluate ---
y_pred = clf.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.3f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# --- 6. save metrics ---
os.makedirs("logs", exist_ok=True)
pd.DataFrame([{"accuracy": acc}]).to_csv("logs/metrics.csv", index=False)
print("Metrics saved to logs/metrics.csv")

import joblib
import os

# --- 7. save model + vectorizer ---
os.makedirs("models", exist_ok=True)

joblib.dump(clf, "models/model.pkl")
joblib.dump(vec, "models/vectorizer.pkl")

print("Model and vectorizer saved in 'models/'")

# Exploration : Accuracy


from sklearn.metrics import accuracy_score, f1_score
from pathlib import Path
import json, time, joblib


y_pred = clf.predict(X_val)

metrics = {
    "task": "classification",
    "accuracy": float(accuracy_score(y_val, y_pred)),
    "f1_macro": float(f1_score(y_val, y_pred, average="macro")),
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "model_file": "model.pkl",
    "vectorizer_file": "vectorizer.pkl",
}

MODELS_DIR = Path(__file__).resolve().parents[1] / "models" 
MODELS_DIR.mkdir(exist_ok=True)


joblib.dump(clf, MODELS_DIR / "model.pkl")
joblib.dump(vec, MODELS_DIR / "vectorizer.pkl")


with open(MODELS_DIR / "metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)

print("Saved model, vectorizer, and metrics.json in /models")