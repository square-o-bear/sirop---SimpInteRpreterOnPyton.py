import tkinter
import random


def findSplit (spis, finded):
    for i in range(0, len(spis)):
        if spis[i] == finded:
            return i


root = tkinter.Tk()
c = open('codi', 'r')
codi = [str(i) for i in c.read().split()]
doit = True
ii = 0
per = {}
mods = {'TKconsol': False}
a = 0
ifi = []

while doit:
    # dop
    if (codi[ii] == '/stop') | (codi[ii] == '/стоп'):
        doit = False
    elif (codi[ii] == '/import') | (codi[ii] == '/добавить'):
        mods[codi[ii+1]] = True

    # sozdanie
    elif (codi[ii] == 'var') | (codi[ii] == 'создать'):
        if (codi[ii+1] == 'int') | (codi[ii+1] == 'число'):
            per[codi[ii+2]] = 0
        elif (codi[ii+1] == 'str') | (codi[ii+1] == 'строка'):
            per[codi[ii+2]] = ''
        elif (codi[ii+1] == 'tf') | (codi[ii+1] == 'пл'):
            per[codi[ii+2]] = False

    elif codi[ii] == '+=':
        if (codi[ii+1] == 'int:') | (codi[ii+1] == 'число:'):
            per[codi[ii-1]] += int(codi[ii+2])
        if (codi[ii+1] == 'per:') | (codi[ii+1] == 'переменная:'):
            per[codi[ii-1]] += int(per[codi[ii+2]])
    elif (codi[ii] == '=') & ((codi[ii+1] == 'read') | (codi[ii + 1] == 'прочитать')):
        if type(per[codi[ii-1]]).__name__ == 'int':
            per[codi[ii-1]] = int(input())
        elif type(per[codi[ii-1]]).__name__ == 'str':
            per[codi[ii-1]] = input()

    elif (codi[ii] == '=') & ((codi[ii+1] == 'random') | (codi[ii+1] == 'рандомное')):
        per[codi[ii-1]] = random.random()*10*len(codi[ii+2])//1

    elif (codi[ii] == '=') & ((codi[ii+1] == 'text:') | (codi[ii + 1] == 'текст:')):
        if type(per[codi[ii-1]]).__name__ == 'str':
            per[codi[ii-1]] = codi[ii+2]
        elif type(per[codi[ii-1]]).__name__ == 'int':
            per[codi[ii-1]] = int(codi[ii+2])
        elif type(per[codi[ii-1]]).__name__ == 'bool':
            if (codi[ii+2] == 'true') | (codi[ii+2] == 'True') | (codi[ii+2] == 'правда') | (codi[ii+2] == 'Правда'):
                per[codi[ii-1]] = True
            if (codi[ii+2] == 'false') | (codi[ii+2] == 'False') | (codi[ii+2] == 'ложь') | (codi[ii+2] == 'Ложь'):
                per[codi[ii-1]] = False

    # pechati
    elif (codi[ii] == 'write') | (codi[ii] == 'напечатать'):
        if (codi[ii+1] == 'text:') | (codi[ii+1] == 'текст:'):
            print(codi[ii+2], end='')
        else:
            print(per[codi[ii+1]], end='')
    elif (codi[ii] == 'writeln') | (codi[ii] == 'напечататьСтрока'):
        if (codi[ii+1] == 'text:') | (codi[ii+1] == 'текст:'):
            print(codi[ii+2])
        else:
            print(per[codi[ii+1]])

    # if / esli
    elif (codi[ii] == 'if') | (codi[ii] == 'если'):
        ifi = []
        for i in range(ii, findSplit(codi, '}')):
            if (codi[i] == 'per:') | (codi[i] == 'переменная:'):
                ifi.append(per[codi[i+1]])
            elif (codi[i] == 'text:') | (codi[i] == 'строка:'):
                ifi.append(codi[ii+5])
            elif (codi[i] == 'int:') | (codi[i] == 'число:'):
                ifi.append(int(codi[ii+5]))
        if codi[ii+3] == '==':
            if ifi[0] != ifi[1]:
                codi[ii+1:findSplit(codi, '}') + 1] = ''
        if codi[ii+3] == '>':
            if ifi[0] <= ifi[1]:
                codi[ii:findSplit(codi, '}') + 1] = ''
        if codi[ii+3] == '>=':
            if ifi[0] < ifi[1]:
                codi[ii:findSplit(codi, '}') + 1] = ''
        if codi[ii+3] == '<':
            if ifi[0] >= ifi[1]:
                codi[ii:findSplit(codi, '}') + 1] = ''
        if codi[ii+3] == '<=':
            if ifi[0] > ifi[1]:
                codi[ii:findSplit(codi, '}') + 1] = ''
        if (codi[ii+3] == '<>') | (codi[ii+3] == '><') | (codi[ii+3] == '!=') | (codi[ii+3] == '=!'):
            if ifi[0] != ifi[1]:
                codi[ii:findSplit(codi, '}') + 1] = ''

    # repeat
    elif codi[ii] == 'repeat':
        if codi[ii+1] == 'int:':
            print('ok')
        if codi[ii+1] == 'per:':
            print('ok')

    ii += 1

if mods['TKconsol']:
    root.geometry('400x400')
    root.title('sirop #TKconsole')
    root.mainloop()
