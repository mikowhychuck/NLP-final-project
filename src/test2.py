from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

def train_model(descriptions, breeds):
    X_train, X_test, y_train, y_test = train_test_split(descriptions, breeds, test_size=0.2, random_state=42)
    
    model = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=10000, stop_words='polish')),
        ('classifier', MultinomialNB())
    ])

    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy}")
    return model

# Wczytaj dane i trenuj model
with open('data/descriptions.txt', 'r', encoding='utf-8') as desc_file, \
     open('data/breeds.txt', 'r', encoding='utf-8') as breed_file:
    descriptions = desc_file.read().split('\n')
    breeds = breed_file.read().split('\n')

model = train_model(descriptions, breeds)

def predict_breed(description):
    return model.predict([description])[0]

# Przykład użycia
print(predict_breed("Mały, krótkowłosy pies o brązowej sierści"))
