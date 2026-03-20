import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data — only runs once
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

def preprocess(text):
    # Step 1 — lowercase
    text = text.lower()

    # Step 2 — remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3 — tokenize (split into words)
    words = nltk.word_tokenize(text)

    # Step 4 — remove stopwords (in, the, is, a, at...)
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w not in stop_words]

    # Step 5 — lemmatize (running → run, models → model)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]

    # Step 6 — join back to string
    return " ".join(words)