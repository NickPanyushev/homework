with open("yazkora.txt", "r", encoding="utf8") as file:
    text = file.read()  # открыли файл


def find_sentences(file):  # найдем все предложения
    lines, sentences = [], []
    lines = file.split("\n")
    for i in range(len(lines)):
        sentences += lines[i].split('.')
    return sentences


def find_words(file):  # найдем слова - эта фигня определяет и знаки переноса строки
    k = find_sentences(file)
    words = []
    for i in k:
        words += i.split(' ')
    return words


def find_adj(file):
    sentences = find_sentences(file)  # нашли все предложения
    adj_in_sent = {}
    for i in sentences:  # бежимся по предложениям
        words = []  # обнулили счетчик слов
        words = find_words(i)  # теперь находим слова в каждом предложении
        adj_in_sent[i] = []  # для каждого предложения завели свой лист с прилагательными()
        for k in words:
            if k[-2:] == "yo":  # нашли нужное окончание
                adj_in_sent[i] += [k]
    return adj_in_sent

with open("result.txt", "w", encoding="utf8") as result:
    for k in find_adj(text).values():
        string = str(" ".join(k)) + "\n"  # разделяет по пробелу k
        result.write(string)
