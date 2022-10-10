import tkinter
import random

def findSplit (spis, finded):
    for i in range(0, len(spis)):
        if spis[i] == finded:
            return i

c = open('codi', 'r')
codi = [str(i) for i in c.read().split()]
root = tkinter.Tk()
labelText = tkinter.Label(text='')
doit = True
ii = 0
per = {}
mods = {"TKconsol": False}
a = 0

while doit:
    # dop (dio)
    if codi[ii] == '/stop':
        doit = False
    elif codi[ii] == '/import':
        mods[codi[ii+1]] = True

    # sozdanie
    elif (codi[ii] == 'var') & (codi[ii+1] == 'int'):
        per[codi[ii+2]] = 0
        labelText = tkinter.Label(text=f'zadali peremenu {codi[ii+2]} classa int')
        labelText.pack()

    elif (codi[ii] == 'var') & (codi[ii+1] == 'str'):
        per[codi[ii+2]] = ''
        labelText = tkinter.Label(text=f'zadali peremenu {codi[ii+2]} classa str')
        labelText.pack()
    elif (codi[ii] == 'var') & (codi[ii+1] == 'tf'):
        per[codi[ii+2]] = False
        labelText = tkinter.Label(text=f'zadali peremenu {codi[ii+2]} classa tf')
        labelText.pack()

    # zadati
    elif (codi[ii] == '=') & (codi[ii+1] == 'read'):
        if type(per[codi[ii-1]]).__name__ == 'int':
            per[codi[ii-1]] = int(input())
            labelText = tkinter.Label(text=f'perezadali {codi[ii-1]} class int chehez "read"')
            labelText.pack()
        elif type(per[codi[ii-1]]).__name__ == 'str':
            per[codi[ii-1]] = input()
            labelText = tkinter.Label(text=f'perezadali {codi[ii-1]} class str chehez "read"')
            labelText.pack()

    elif (codi[ii] == '=') & (codi[ii+1] == 'random'):
        per[codi[ii-1]] = random.random()*10*len(codi[ii+2])//1

    elif (codi[ii] == '=') & (codi[ii+1] == 'text:'):
        if type(per[codi[ii-1]]).__name__ == 'str':
            per[codi[ii-1]] = codi[ii+2]
            labelText = tkinter.Label(text=f'perezadali {codi[ii-1]} classa str cherez "="')
            labelText.pack()
        elif type(per[codi[ii-1]]).__name__ == 'int':
            per[codi[ii-1]] = int(codi[ii+2])
            labelText = tkinter.Label(text=f'perezadali {codi[ii-1]} classa int cherez "="')
            labelText.pack()
        elif type(per[codi[ii-1]]).__name__ == 'bool':
            if (codi[ii+2] == 'true') | (codi[ii+2] == 'True'):
                per[codi[ii-1]] = True
            if (codi[ii+2] == 'false') | (codi[ii+2] == 'False'):
                per[codi[ii-1]] = False
            labelText = tkinter.Label(text=f'perezadali {codi[ii - 1]} classa tf cherez "="')
            labelText.pack()

    # pechati
    elif codi[ii] == 'write':
        if codi[ii+1] == 'text:':
            print(codi[ii+2], end='')
            labelText = tkinter.Label(text=f'napechatali {codi[ii+2]}')
            labelText.pack()
        else:
            print(per[codi[ii+1]], end='')
        labelText = tkinter.Label(text=f'napechatali peremenu {codi[ii+1]} bez perenosa stroki')
        labelText.pack()

    elif codi[ii] == 'writeln':
        if codi[ii+1] == 'text:':
            print(codi[ii+2])
        else:
            print(per[codi[ii+1]])
        labelText = tkinter.Label(text=f'napechatali peremenu {codi[ii+1]} s perenosa stroki')
        labelText.pack()

    # if / esli
    elif codi[ii] == 'if':
        if codi[ii+2] == '==':
            if per[codi[ii+1]] != codi[ii+3]:
                codi[ii:findSplit(codi, '}')] = ''
            print(codi)

    ii += 1

if mods["TKconsol"]:
    root.geometry('400x400')
    root.title('codi')
    root.mainloop()
