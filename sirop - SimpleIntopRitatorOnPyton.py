import random


def findSplit (spis, finded):
    for i in range(0, len(spis)):
        if spis[i] == finded:
            return i


c = open('codi', 'r')
codi = [str(i) for i in c.read().split()]
mods = {'TKconsole': False}
per = {'mods': mods}


def siropCodi (spis):
    ii = 0
    doit = True
    while doit:
        if spis[ii] == '/import':
            mods[spis[ii+1]] = True
        if spis[ii] == '/stop':
            doit = False
        elif spis[ii] == 'var':
            if spis[ii+1] == 'int:':
                per[spis[ii+2]] = 0
            if spis[ii+1] == 'text:':
                per[spis[ii+2]] = ''

        elif (spis[ii] == 'writeln') | (spis[ii] == 'println'):
            if spis[ii+1] == 'per:':
                print(per[spis[ii+2]])
            elif (spis[ii+1] == 'text:') | (spis[ii+1] == 'int:'):
                print(spis[ii+2])
        elif (spis[ii] == 'write') | (spis[ii] == 'print'):
            if spis[ii+1] == 'per:':
                print(per[spis[ii+2]], end='')
            elif (spis[ii+1] == 'text:') | (spis[ii+1] == 'int:'):
                print(spis[ii+2], end='')

        elif spis[ii] == '+=':
            if spis[ii+1] == 'int:':
                per[spis[ii-1]] = int(per[spis[ii-1]]) + int(spis[ii+2])
            if spis[ii+1] == 'text:':
                per[spis[ii-1]] += spis[ii+2]

        elif spis[ii] == '=':
            if spis[ii+1] == 'random':
                per[spis[ii-1]] = random.random()*(10*len(codi[ii+2]))//1
            elif (spis[ii+1] == 'read') | (spis[ii+1] == 'input'):
                if type(per[spis[ii-1]]).__name__ == 'str':
                    per[spis[ii-1]] = input()
                if type(per[spis[ii-1]]).__name__ == 'int':
                    per[spis[ii-1]] = int(input())
            else:
                per[spis[ii-1]] = spis[ii+1]

        elif spis[ii] == 'repeat':
            for i in range(1, int(spis[ii+1])):
                siropCodi(spis[findSplit(spis, '{') : findSplit(spis, '}')+1])

        ii += 1


siropCodi(codi)
