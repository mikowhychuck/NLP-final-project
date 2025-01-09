from transformers import pipeline
classifier = pipeline("text-classification", model="./dog_breed_classifier", tokenizer="./dog_breed_classifier")
result = classifier("potrzebuję psa do mieszkania, ale chcę żeby był duży. chciałbym żeby nie wymagał dużej ilości ruchu i dawał się tresować.")
print(result)
