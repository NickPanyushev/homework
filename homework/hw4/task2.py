with open("dict.txt", "r", encoding="utf8") as file:
    text = file.read()  # открыли файл


def find_words(file):  # функция выдает лист
    words = file.split("\n")
    return words


def count_word_classes(file): # функция возвращает словарь с количеством nouns, adj, verbs
    words = find_words(text) # нашли все слова из списка
    word_classes = {'nouns':0, 'adj':0, 'verbs':0}
    for k in words: # бежимся по списку слов
        if k[-2:] == "yo":  # нашли adj
            word_classes['adj'] += 1
        elif k[-2:] == "ka": # нашли nouns
            word_classes['nouns'] += 1
        else: # иначе- глаголы
            word_classes['verbs'] += 1
    return word_classes

def combinations(n,k): #считает количество вариантов для adj
    number = 1
    for i in range(0,k-1):
        number = number * (number-i)
    return number

def number_good_sentences(file):
    word_classes = count_word_classes(file) # посчитали все части речи
    for i in word_classes: # теперь смотрим количество сочетаний
        if i == 'adj':
            number = combinations(len(word_classes.items()), 7)

        #print (i)

    return(number)

print (combinations(5,2))