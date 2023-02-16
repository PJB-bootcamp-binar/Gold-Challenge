from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load Kamus Alay
alay_dict = pd.read_csv('new_kamusalay.csv', encoding='latin-1')
alay_dict = dict(zip(alay_dict['slang'], alay_dict['formal']))

# Create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Create stopword remover
stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.create_stop_word_remover()

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*\]','', text).strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub('\S*\d\S*\s*','', text).strip()
    return text.strip()

# Clean alay function
def clean_alay(text, alay_dict):
    cleaned_text = []
    for word in text.split():
        if word in alay_dict:
            cleaned_text.append(alay_dict[word])
        else:
            cleaned_text.append(word)
    return " ".join(cleaned_text)

# Define home page
@app.route('/')
def home():
    return render_template('index.html')

# Define clean page
@app.route('/clean', methods=['POST'])
def clean():
    # Get input text from form
    input_text = request.form['input_text']

    # Tokenize
    tokens = nltk.tokenize.word_tokenize(input_text)

    # Clean text
    cleaned_text = clean_text(input_text)

    # Clean alay
    cleaned_alay = clean_alay(cleaned_text, alay_dict)

    # Stemming
    cleaned_alay_stemmed = stemmer.stem(cleaned_alay)

    # Remove stopwords
    cleaned_alay_no_stopwords = stopwords.remove(cleaned_alay)

    # Create chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Input Text', 'Cleaned Text', 'Cleaned Alay', 'Stemmed', 'No Stopwords'],
           [len(input_text), len(cleaned_text), len(cleaned_alay), len(cleaned_alay_stemmed), len(cleaned_alay_no_stopwords)])
    ax.set_title('Length of Text After Cleaning')
    ax.set_ylabel('Number of Characters')
    ax.grid(True)

    # Render result page
    return render_template('result.html',
                           input_text=input_text,
                           tokens=tokens,
                           cleaned_text=cleaned_text,
                           cleaned_alay=cleaned_alay,
                           cleaned_alay_stemmed=cleaned_alay_stemmed,
                           cleaned_alay_no_stopwords=cleaned_alay_no_stopwords,
                           plot=fig)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
