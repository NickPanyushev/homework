import os
import re

os.chdir('/home/nickolay/ACTN4 projects/NF-kB_Chip-seq/')
with open("NF-kb_list.txt", "r") as file:  # opening file and reading the entire contents
    text = file.read()

lines = text.split("\n")  # splitting descriptions by symbol "\n"

experiments = {'header': [], 'description': [], 'organism': [], 'platforms': [], 'num_of_samples': [], 'ftp_links': [],
               'GEO_accession': [], 'ID': []}  # это и будет наш ответ
for index, i in enumerate(lines):  # распарсили названия экспериментов и сделали словарь из них
    regexp = re.compile('^\d+. ')
    if re.findall(regexp, i):
        header = re.sub(regexp, '', i)
        experiments['header'].append(header)  # записываем заголовок в словарь

        descriptions = re.sub('(Submitter supplied)', '', lines[index + 1])  # удалили заголовок
        experiments['description'].append(descriptions)  # записываем описание в словарь

        organism = (re.sub('Organism:\t', '', lines[index + 2]))  # убрали заголовок,
        experiments['organism'].append(organism.split('; '))  # записали организмы

        tmp = re.sub('Platforms?: ', '', lines[index + 4])  # удалили заголовок слева
        platforms = re.sub(' \d+ Samples$', '', tmp)  # удалили все, что справа
        experiments['platforms'].append(platforms.split(' '))  # убрали заголовок, записали платформы

        num_of_samples = tmp.split(' ')[-2]
        experiments['num_of_samples'].append(num_of_samples)  # записали количество образцов

        ftp_links = lines[index + 5].split(' ')[-1]
        experiments['ftp_links'].append(ftp_links)

        GEO_accession = re.sub('\t', ' ', lines[index + 6])
        experiments['GEO_accession'].append(GEO_accession.split(' ')[-3])
        experiments['ID'].append(GEO_accession.split(' ')[-1])

with open("NF-kb_table.txt", "w") as new_file:  # создание файла
    keys = ['header', 'description', 'organism', 'platforms', 'num_of_samples', 'ftp_links', 'GEO_accession', 'ID']
    parsed_headers = '\t'.join(keys)
    print(parsed_headers)
    new_file.write(parsed_headers + '\n')
    parsed_header = []

    for i in range(len(experiments['header'])):  # бежимся по элементам словаря
        parsed_header = []
        for k in keys:  # бежимся по ключам словаря
            parsed_header.append(experiments[k][i])  # добавили к списку элемент из словаря ключ-[k] элемент [i]
            final_line = '\t'.join(str(i) for i in parsed_header)
        # new_file.writelines(final_line)
        print(final_line, file=new_file)
    print(final_line)
