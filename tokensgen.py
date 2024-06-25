import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Get user input for a sentence
sentence = input("Enter a sentence: ")

# Tokenization using gensim (optional, since we'll use nltk for more flexibility)
words = word_tokenize(sentence)
print("Word Tokens (before stopwords removal):", words)

# Stop words removal using gensim
words = [word for word in words if word.lower() not in STOPWORDS]
print("Filtered Words (after stopwords removal):", words)

# Initialize NLTK's Porter Stemmer and WordNet Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


# Stemming using NLTK's Porter Stemmer
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)

# Lemmatization using NLTK's WordNet Lemmatizer
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized Words:", lemmatized_words)