ancestors = {} # сюда сложим всю инфу о наследовании
for i in range(int(input())):
    inheritance = input().split(' : ')
    if len(inheritance) == 1:
        ancestors[inheritance[0]] = [] # если предков нет, то записываем пустой лист
    else:
        ancestors[inheritance[0]] = inheritance[1].split(' ')

ancestors = {'D': [], 'B': ['C'], 'C': ['D'], 'A': ['B']}

def find_ancestor(child, parent, ancestors): #рекурсивная функция поиска
    if parent in ancestors[child]: #если напрямую наследуется - то вернули "yes"
         return "Yes"
    for i in ancestors[child]:
        if find_ancestor(i,parent,ancestors):
            return 'Yes'
    return 'No'

child = input()
parent = input()
print(find_ancestor(child, parent, ancestors))




