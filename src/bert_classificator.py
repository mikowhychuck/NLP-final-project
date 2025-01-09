from transformers import pipeline
import json

dog_breeds = {
    "labrador retriever": "retriever",
    "yorkshire terrier": "terrier/yorkshire",
    "owczarek niemiecki": "germanshepherd",
    "beagle": "beagle",
    "golden retriever": "retriever/golden",
    "buldog": "bulldog",
    "mops": "pug",
    "cocker spaniel": "spaniel",
    "shih tzu": "shihtzu",
    "border collie": "collie",
    "maltańczyk": "maltese",
    "rottweiler": "rottweiler",
    "doberman": "doberman",
    "akita inu": "akita",
    "husky": "husky",
    "chihuahua": "chihuahua"
}

def get_breed(text):
    classifier = pipeline("text-classification", model="dog_breed_classifier", tokenizer="dog_breed_classifier")
    result = classifier(text)
    result = result[0]['label']
    result = result.replace('-', ' ')
    eng_name = dog_breeds[result]
    return result

def get_eng_name(text):
    return dog_breeds[text]
