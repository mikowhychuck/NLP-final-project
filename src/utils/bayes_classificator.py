import json
import spacy
import re
import os

nlp = spacy.load("pl_core_news_sm")

def clean_text(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = re.sub(r'[^a-ząćęłńóśźż\s]', '', text)
    text = text.strip()
    return text

def lemmatize_text(text):
    text = clean_text(text)
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized_text

#info dla Adasia - to przyjmuje lista[i] a nei całą liste, i zapisujmey w jsonie zeby łatwo było odczytac
def create_vocab_with_counts_for_one_description(text):
    vocab = {}
    line = lemmatize_text(text)
    words = line.split(' ')
    for word in words:
        if word in vocab:
            vocab[word] += 1
        else:
            vocab[word] = 1
    return json.dumps(vocab, ensure_ascii=False)

#Odpalic jak chce sie wygenrerowac nowe pliki - vocab_with_counts.json, czyli w osobnym wierszu osobny słownik i total_words.txt, czyli ile jest słow w sumie
def files_generator(description_path):
    description_file = open(f'{description_path}.txt', 'r', encoding='utf-8')
    descriptions = description_file.readlines()

    vocab_file = open('vocab_with_counts.json', 'w', encoding='utf-8')
    vocab_file.write('[')
    for i in range(len(descriptions)):
        vocab = create_vocab_with_counts_for_one_description(descriptions[i])
        if i < len(descriptions) - 1:
            vocab_file.write(str(vocab) + ',\n')
        else:
            vocab_file.write(str(vocab) + '\n')
    
    vocab_file.write(']')

    vocab_file = open('vocab_with_counts.json', 'r', encoding='utf-8')

    dict = json.load(vocab_file)

    total_words = 0
    total_words_file = open('total_words.txt', 'w', encoding='utf-8')
    for i in range(len(dict)):
        total_words = sum(dict[i].values())
        total_words_file.write(str(total_words)+'\n')

    vocab_size = 0
    vocab_size_file = open('vocab_size.txt', 'w', encoding='utf-8')
    for i in range(len(dict)):
        vocab_size = len(dict[i])
        vocab_size_file.write(str(vocab_size)+'\n')

# nie wiem nie rozumiem zabije sie pozdrawiam nowy rok nowa ja wiec nowa ja będzie martwa uwu nie no serio zarcik kckc
def calculate_probability_of_word_in_class(class_vocab, total_words_in_class, class_vocab_size):
    probability_of_words = {}
    for word, count in class_vocab.items():
        probability_of_words[word] = (count + 1) / (total_words_in_class + class_vocab_size)
    return probability_of_words


total_words = open('total_words.txt', 'r', encoding='utf-8').read().split()
total_words = [int(i) for i in total_words]

vocab_size = open('vocab_size.txt', 'r', encoding='utf-8').read().split()
vocab_size = [int(i) for i in vocab_size]

vocab_file = open('vocab_with_counts.json', 'r', encoding='utf-8')
dict = json.load(vocab_file)
print(dict[0])

print(calculate_probability_of_word_in_class(dict[0], total_words[0], vocab_size[0]))