from transformers import pipeline
classifier = pipeline("text-classification", model="./dog_breed_classifier", tokenizer="./dog_breed_classifier")
result = classifier("Duży pies odpowiedni dla dzieci, ale taki który obroni dom i kiedyś pracował w policji")
print(result)
