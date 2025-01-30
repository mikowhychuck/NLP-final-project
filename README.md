# HowHau

<img src="howhau.png" alt="Logo HowHau" width="300">

## Instrukcja uruchomienia programu

Aby uruchomić program należy:

1. uruchomić `src/bert_model_train.py`
2. uruchomić `src/app.py`

## Proces tworzenia projektu

### Założenia projektu

Program który stworzyliśmy jest aplikacją webową, dzięki której użytkownik może dowiedzieć się, jaka rasa psa jest dla niego odpowiednia po opisaniu swoich osobistych preferencji.

### Tworzenie zbioru danych

Zdecydowaliśmy się na to, aby model klasyfikował 16 najpopularniejszych ras psów w Polsce. Po dogłębnej analizie wybraliśmy następujące rasy:

- labrador retriever
- yorkshire terrier
- owczarek niemiecki
- beagle
- golden retriever
- buldog francuski
- mops
- cocker spaniel
- shihtzu
- border collie
- maltańczyk
- rottweiler
- doberman
- akita inu
- husky
- chihuahua

Dla każdej z ras zebraliśmy kilkadziesiąt opisów, z bardzo zróżnicowanych źródeł - od wikipedii, poprzez blogi i inne strony internetowe, aż do danych syntetycznych i tych najbardziej naturalnych - zebranych od naszych bliskich.

### Trenowanie modelu

Podchodziliśmy do realizacji projektu dwukrotnie - najpierw wykorzystując klasyfikator bayesa, a po odkryciu, że jego działanie jest niesatysfakcjonujące, dokonaliśmy finetuningu polskiego modelu BERT - sdadas/polish-roberta-base-v2. Ostateczny projekt opiera się na tym drugim rozwiązaniu, ale plik realizujący klasyfikator bayesa jest także dodany do tego katalogu.

W pliku results.txt znajdują się rezultaty modelu przy trenowaniu go z różnymi parametrami - pozwoliło nam to na analizę który zestaw parametrów daje najlepsze wyniki.

### Aplikacja webowa

Stworzyliśmy prostą aplikację webową w Flasku, dzięki której cały system jest bardziej user-friendly.

## Autorzy projektu

- Adam Mikołajczak
- Małgorzata Farbotko
