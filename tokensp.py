import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Process the text with spaCy
doc = nlp(text)

# Tokenization
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# Stop words removal
filtered_tokens = [token.text for token in doc if not token.is_stop]
print("Filtered Tokens:", filtered_tokens)

# Stemming (approximated using lemmatization as spaCy does not provide a direct stemmer)
stemmed_tokens = [token.lemma_ for token in doc if not token.is_stop]
print("Stemmed Tokens:", stemmed_tokens)

# Lemmatization
lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop]
print("Lemmatized Tokens:", lemmatized_tokens)
