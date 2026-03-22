# similarity.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def download_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except:
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('stopwords')


download_nltk()


def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]

    return " ".join(filtered_tokens)


# ✅ THIS FUNCTION MUST EXIST
def compute_similarity(doc1, doc2):
    doc1_clean = preprocess(doc1)
    doc2_clean = preprocess(doc2)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([doc1_clean, doc2_clean])

    similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return similarity_score