from transformers import pipeline

def get_breed(text):
    classifier = pipeline("text-classification", model="dog_breed_classifier", tokenizer="dog_breed_classifier")
    result = classifier(text)
    result = result[0]['label']
    return result
