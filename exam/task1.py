with open("C:\\Users\\User\\git\python-course\\exam\\yazkora.txt", "r", encoding="utf8") as file:
    text = file.read() # ������� ���� ����

def find_sentences(file): # ���� �����������, ����������� ������
    sentences = []
    sentences.append(text.split("."))
    return sentences # �������� �� � ����


def find_adj_in_sentence(file): # ������ ���� ��������������
    adjectives = [] # ������� ������ ���� ��� �������������� �� ������ �����������
    k = find_sentences(file)
    for i in k:
        words = [] #���� ����
        words.append(k.split(' '))
        for t in words:
            if

sentences =