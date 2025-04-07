# HowHau (Polish below)

<img src="howhau.png" alt="Logo HowHau" width="300">

## Program Launch Instructions

To run the program, you need to:

1. run `src/bert_model_train.py`
2. run `src/app.py`

## Project Development Process

### Project Assumptions

The program we created is a web application that helps users find out which dog breed suits them best based on their personal preferences.

### Dataset Creation

We decided to train the model to classify the 16 most popular dog breeds in Poland. After thorough analysis, we selected the following breeds:

- labrador retriever  
- yorkshire terrier  
- german shepherd  
- beagle  
- golden retriever  
- french bulldog  
- pug  
- cocker spaniel  
- shihtzu  
- border collie  
- maltese  
- rottweiler  
- doberman  
- akita inu  
- husky  
- chihuahua  

For each breed, we collected several dozen descriptions from highly diverse sources – ranging from Wikipedia, through blogs and various websites, to both synthetic data and the most natural kind – gathered from our close ones.

### Model Training

We approached the project twice – first using a Naive Bayes classifier, and after discovering its performance was unsatisfactory, we fine-tuned a Polish BERT model – `sdadas/polish-roberta-base-v2`. The final project is based on the latter solution, but the file implementing the Naive Bayes classifier is also included in this directory.

The file `results.txt` contains the model's results when trained with different parameters – this allowed us to analyze which parameter set produced the best results.

### Web Application

We built a simple Flask web app to make the whole system more user-friendly.

## Project Authors

- Adam Mikołajczak  
- Małgorzata Farbotko  

# HowHau (Opis po polsku)
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
