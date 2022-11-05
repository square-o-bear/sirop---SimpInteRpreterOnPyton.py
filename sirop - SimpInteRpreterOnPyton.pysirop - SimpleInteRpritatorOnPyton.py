import tkinter
import random


def findSplit (spis, finded):
    for i in range(0, len(spis)):
        if spis[i] == finded:
            return i


c = open('codi', 'r')
codi = [str(i) for i in c.read().split()]
mods = {'TKconsole': False}
settings = {'ru': False, 'short': False}
per = {}
root = tkinter.Tk()
textLabel = tkinter.Label(text='')

def siropCodi (spis):
    for ii in range(0, len(spis)):
        #print(ii)
        if spis[ii] == '/settings':
            for i in range(findSplit(spis, '/settings'), findSplit(spis, '/')):
                if spis[i] == 'ru':
                    settings['ru'] = True
                elif spis[i] == 'short':
                    settings['short'] = True
            print(settings)
        elif spis[ii] == '/import':
            mods[spis[ii+1]] = True
            # TKconsole
            textLabel = tkinter.Label(text=f'import {spis[ii+1]}')
            textLabel.pack()
        elif spis[ii] == 'var':
            if spis[ii+1] == 'int:':
                per[spis[ii+2]] = 0
                # TKconsole
                textLabel = tkinter.Label(text=f'var int {spis[ii+2]}')
                textLabel.pack()
            if spis[ii+1] == 'text:':
                per[spis[ii+2]] = ''
                # TKconsole
                textLabel = tkinter.Label(text=f'var text {spis[ii+2]}')
                textLabel.pack()

        elif (spis[ii] == 'writeln') | (spis[ii] == 'println'):
            if spis[ii+1] == 'per:':
                print(per[spis[ii+2]])
                # TKconsole
                textLabel = tkinter.Label(text=f'write / print per {spis[ii + 2]}')
                textLabel.pack()
            elif (spis[ii+1] == 'text:') | (spis[ii+1] == 'int:'):
                print(spis[ii+2])
                # TKconsole
                textLabel = tkinter.Label(text=f'write / print text {spis[ii + 2]}')
                textLabel.pack()

        elif (spis[ii] == 'write') | (spis[ii] == 'print'):
            if spis[ii+1] == 'per:':
                print(per[spis[ii+2]], end='')
                # TKconsole
                textLabel = tkinter.Label(text=f'write / print per {spis[ii + 2]}')
                textLabel.pack()
            if (spis[ii+1] == 'text:') | (spis[ii+1] == 'int:'):
                print(spis[ii+2], end='')
                # TKconsole
                textLabel = tkinter.Label(text=f'write / print text {spis[ii + 2]}')
                textLabel.pack()

        elif spis[ii] == '+=':
            if spis[ii+1] == 'int:':
                per[spis[ii-1]] = int(per[spis[ii-1]]) + int(spis[ii+2])
            if spis[ii+1] == 'text:':
                per[spis[ii-1]] += spis[ii+2]
            # TKconsole
            textLabel = tkinter.Label(text=f'{spis[ii-1]} + {spis[ii+2]}')
            textLabel.pack()
        elif spis[ii] == '-=':
            if spis[ii+1] == 'int:':
                per[spis[ii-1]] = int(per[spis[ii-1]]) - int(spis[ii+2])
            # TKconsole
            textLabel = tkinter.Label(text=f'{spis[ii-1]} - {spis[ii+2]}')
            textLabel.pack()

        elif spis[ii] == '=':
            if spis[ii+1] == 'random':
                per[spis[ii-1]] = random.random()*(10*len(codi[ii+2]))//1
                # TKconsole
                textLabel = tkinter.Label(text=f'{spis[ii+1]} = random {per[spis[ii-1]]}')
                textLabel.pack()
            elif (spis[ii+1] == 'read') | (spis[ii+1] == 'input'):
                if type(per[spis[ii-1]]).__name__ == 'str':
                    per[spis[ii-1]] = input()
                    # TKconsole
                    textLabel = tkinter.Label(text=f'{spis[ii+1]} = read/input text {per[spis[ii-1]]}')
                    textLabel.pack()
                if type(per[spis[ii-1]]).__name__ == 'int':
                    per[spis[ii-1]] = int(input())
                    # TKconsole
                    textLabel = tkinter.Label(text=f'{spis[ii+1]} = read/input int {per[spis[ii-1]]}')
                    textLabel.pack()
            else:
                per[spis[ii-1]] = spis[ii+1]

        elif spis[ii] == 'repeat':
            textLabel = tkinter.Label(text=f'repeat {int(spis[ii+1])}')
            textLabel.pack()
            # TKconsole /\
            for i in range(1, int(spis[ii+1])):
                siropCodi(spis[findSplit(spis, '{') : findSplit(spis, '}')+1])

siropCodi(codi)

if mods['TKconsole']:
    root.geometry('400x400')
    root.title('sirop #TKconsole')
    root.mainloop()
