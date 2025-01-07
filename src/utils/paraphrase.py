'''
This code is paraphrasing given text by translating it polish->english->german->polish using google translator
'''
from deep_translator import GoogleTranslator

text = '''
Jest to pies myśliwski, aportojuący i bardzo lubi wodę. Jest żywiołowy, pracujący. ambitny i mający potencjał szkoleniowy.
Szczekliwa, zadziorna, przemądrzały, pewny siebie i ruchliwy. Jest mały, bywają w wersji miniaturowej. Jest z reguły długowłosy. Do torebki.
Dobry do polowań. Policja go chyba używa.
Beagle to rasa małych psów myśliwskich, pochodząca z Wielkiej Brytanii. Zaliczane do psów gończych, posokowców i ras pokrewnych.
Ładny, pływa i jest miły. Lubię.
Fajny, śpiący, leniwym ślini się. bardzo lubię. potężnie zbudowany. Poleciłbym go komuś kto jest ustatkowanie aktywny fizycznie. Dla starszych ludzi.
Poleciłbym go do niedużego mieszkania. małe takie pomarszczone, wyłupiaste oczka. Dla starszych ludzi.
To takie rude, dłuższe włosy, pływające. wydają się szlachetne i myśliwskie. Ładne i fajne.
Też takie małe, energiczne. Trochę głupkowate i włochate. nadają się do mieszkania.
Bardzo energiczne. pasterskie, raczej nie do mieszkania. bardzo inteligentne. Ładne fajne i łatwew w tresurze. Dużo ruchu potrzebują.
Malutkie, małe, włochate kulki do mieszkania. Nie potrzebują ruchu. Idealne dla starszych ludzi.
Dużo ruchu potrzebuje. Wymagająca tresura. inteligentne. Potrzebują dużo przestrzeni. Raczej dla młodych ludzi i doświadczonych opiekunów. Duże są.
Podobne do rottweilera. Troche mniej masywne ale też duże. Uszka im tak śmiesznie stoją. ale nie zawsze.
Japońska rasa, bardzo mięciusie i ładne ale trzeba je tresować. Są bardzo inteligentne i potrzebują dużo ruchu.
Dosyć spore, ładne, fajne ale trzeba też porządnie tresować bo inaczej będą głupie. W sumie jak każdy kejter.
Malutkie, śmieszne, do mieszkania, głośne bardzo. Głupkowate, ale może nie. Do starszych ludzi mogą być.
'''
translated_to_english = GoogleTranslator(source='pl', target='en').translate(text)
translated_to_german = GoogleTranslator(source='en', target='de').translate(translated_to_english)
back_translated = GoogleTranslator(source='de', target='pl').translate(translated_to_german)

print("Oryginał:", text)
print("Parafraza:", back_translated)
