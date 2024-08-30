pip install nltk spacy
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy


nltk.download('punkt')
nltk.download('stopwords')


nlp = spacy.load('en_core_web_sm')

def process_message(message):
    # Tokenize the message
    words = word_tokenize(message.lower())

    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Stem the words
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    # Process the message using spaCy
    doc = nlp(message)

    # Extract named entities
    entities = [ent.text for ent in doc.ents]

    # ... (Implement your chatbot logic here)

    return response

def get_response(message):
    processed_message = process_message(message)
    # ... (Implement your response generation logic here)
    return response

while True:
    message = input("You: ")
    if message.lower() == "quit":
        break
    response = get_response(message)
    print("Bot:", response)
    
    
def get_response(message):
    if "hello" in message:
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm doing well, thank you! How can I assist you?"
    else:
        return "I'm still learning. Could you please rephrase your question?"