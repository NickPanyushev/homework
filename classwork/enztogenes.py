# Практика по файлам от 24 октября
# Задание на практике было максимально приближено к реальной жизни
# Был дан файл enzyme.small.txt, содержащий данные об энзимах
# Никакой дополнительной информации о формате файла не приводилось
# Необходимо для каждого энзима достать описанные в этом файле гены

# opening file and reading the entire contents
with open("enzyme.small.txt", "r") as f:
    text = f.read()

# splitting descriptions by symbol "///\n"
descriptions = text.split("///\n")

# this will be our answer
genes = {}


for description in descriptions:
    # description consists of lines, lets split them
    lines = description.split("\n")

    # first line contains ID and some key words
    header = lines[0]
    trash = header.split(" ")

    # removing empty lines
    clean = [line for line in trash if line]

    # third element is enzyme_id
    enzyme_id = clean[2]

    # now we have to find information
    # about genes in this enzyme description
    begin, end = 0, 0
    for i, line in enumerate(lines):
        # line that starts with "GENES" is the first line describing genes
        if line.startswith("GENES"):
            for j, line_end in enumerate(lines[i + 1:]):
                # line that doesn't start with " " is the first line not describing genes
                if not line_end.startswith(" "):
                    # so all the information about genes is between this lines
                    genes[enzyme_id] = lines[i: j - 1]
                    break

print(genes["1.1.1.4"])
print(len(descriptions))