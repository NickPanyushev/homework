with open("dict.txt", "r", encoding="utf8") as file:
    text = file.read()  # открыли файл


def find_words(file):  # функция выдает лист
    words = file.split("\n")
    return words


def count_word_classes(file):  # функция возвращает словарь с количеством nouns, adj, verbs
    words = find_words(file)  # нашли все слова из списка
    word_classes = {'nouns': 0, 'adj': 0, 'verbs': 0}
    for k in words:  # бежимся по списку слов
        if k[-2:] == "yo":  # нашли adj
            word_classes['adj'] += 1
        elif k[-2:] == "ka":  # нашли nouns
            word_classes['nouns'] += 1
        else:  # иначе- глаголы
            word_classes['verbs'] += 1
    return word_classes


def combinations(n, k):  # считает количество вариантов для adj
    total = 0

    for t in range(1, k+1):
        number = 1
        for i in range(0, t):  # считает количество из n по k
            number = number * (n - i)
        total += number
    return total


def number_good_sentences(file):
    word_classes = count_word_classes(file)  # посчитали все части речи
    number = combinations(word_classes['adj'], 7) * word_classes['nouns'] * word_classes['verbs']
    return number

print(number_good_sentences(text))
