'''
This code is paraphrasing given text by translating it to czech and back into polish using google translator
'''
from deep_translator import GoogleTranslator

text = 'ho ho ho(es)'
translated_to_english = GoogleTranslator(source='pl', target='en').translate(text)
translated_to_german = GoogleTranslator(source='en', target='de').translate(translated_to_english)
back_translated = GoogleTranslator(source='de', target='pl').translate(translated_to_german)

print("Oryginał:", text)
print("Parafraza:", translated_to_english)
