with open("C:\\Users\\User\\git\python-course\\exam\\yazkora.txt", "r", encoding="utf8") as file:
    text = file.read() # считали весь файл

def find_sentences(file): # ищем предложения, разделенные точкой
    sentences = []
    sentences.append(text.split("."))
    return sentences # записали их в лист


def find_adj_in_sentence(file): # теперь ищем прилагательные
    adjectives = [] # создали пустой лист для прилагательных из одного предложения
    k = find_sentences(file)
    for i in k:
        words = [] #лист слов
        words.append(k.split(' '))
        for t in words:
            if

sentences =