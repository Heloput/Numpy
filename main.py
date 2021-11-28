from tkinter import *
import numpy as np

masArg = np.random.randint(-9, 10, 10)
startMassive = np.random.randint(-9, 10, 10)
matrix = np.random.randint(-9, 10, (3, 3))


def update():
    sizeLbl.configure(text="Размер массива: {}".format(startMassive.size))
    nonzeroLabel1.configure(text="{}".format(np.nonzero(startMassive)))


def extract(string):
    a = np.fromstring(string.strip(), dtype=int, sep=' ')
    if a.size == 0 or a.size == 1 and len(str(a[0])) != len(string.strip()):
        raise Exception('No numbers found')
    return a


def index():
    buffer = int(indexEntry.get())
    if buffer >= startMassive.size:
        buffer = startMassive.size - 1

    indexLabel3.configure(text=startMassive[buffer])
    print(buffer)


def indexer():
    buffer = extract(indexArrEntry.get())
    print(buffer)
    print(startMassive[buffer])
    indexArrLabel3.configure(text=startMassive[buffer])


def srz():
    buffer = extract(indexSrzEntry.get())
    print(buffer)
    if buffer[0] == 0 and buffer[1] == 0 and buffer[2] == -1:
        indexSrzLabel3.configure(text=startMassive[::-1])
    else:
        indexSrzLabel3.configure(text=startMassive[buffer[0]:buffer[1]:buffer[2]])


def generate():
    global startMassive
    startMassive = np.random.randint(-9, 10, 10)
    print(startMassive)
    massiveLabel.configure(text=startMassive)
    update()


def generatematrix():
    global matrix
    matrix = np.random.randint(-9, 10, (3, 3))
    print(matrix)
    matrixLbl.configure(text=matrix)


def empty():
    global startMassive
    startMassive = np.empty(10, int)
    print(startMassive)
    massiveLabel.configure(text=startMassive)
    update()


def zeroes():
    global startMassive
    startMassive = np.zeros(10, int)
    print(startMassive)
    massiveLabel.configure(text=startMassive)
    update()


def ones():
    global startMassive
    startMassive = np.ones(10, int)
    print(startMassive)
    massiveLabel.configure(text=startMassive)
    update()


def entry():
    global startMassive
    startMassive = extract(startEntry.get())
    # startMassive = np.array(list(map(int, startEntry.get())))
    print(startMassive)
    massiveLabel.configure(text=startMassive)
    update()


def size():
    global startMassive
    print(startMassive.size)


def sort():
    global startMassive
    print(startMassive)
    SortLbl.configure(text="Отсортированный массив:")
    SortLbl2.configure(text=np.sort(startMassive))


def argsort():
    ArgsortLbl.configure(text="Массив индексов:")
    ArgsortLbl2.configure(text=np.argsort(startMassive))
    mas_arg = np.argsort(startMassive)
    print(mas_arg)


def lexsort():
    mas_arg = np.random.randint(0, 10, startMassive.size)
    LexsortLbl.configure(text="Второй массив:")
    LexsortLbl2.configure(text=mas_arg)
    LexsortLbl3.configure(text="Массив индексов:")
    lex_arg = np.lexsort((startMassive, mas_arg))
    LexsortLbl4.configure(text=lex_arg)
    c = 0
    buffer_key = "Пара-ключ: \n"
    for i in lex_arg:
        c += 1
        print(mas_arg[i], startMassive[i])
        buffer_key += str((str(mas_arg[i]) + " " + str(startMassive[i])))
        if c != lex_arg.size:
            buffer_key += ", "
        else:
            buffer_key += ". "
        if c == lex_arg.size / 2:
            buffer_key += "\n"
    print(lex_arg.size)
    LexsortLbl5.configure(text=buffer_key)


def clicked():
    res = "Привет {}".format(startEntry.get())
    startLbl.configure(text=res)
    startEntry.delete(0, END)
    startEntry.insert(0, "Generated")


window = Tk()
window.title("Numpy")
window.geometry('1000x600')

# 1 row
startLbl = Label(window, text="Начальный массив:")
startLbl.grid(column=0, row=0)
massiveLabel = Label(window, text="Massive")
massiveLabel.grid(column=1, row=0, columnspan=3)

# 2 row
entryLabel = Label(window, text="Ввести массив: ")
entryLabel.grid(column=0, row=1)
startEntry = Entry(window, width=50)
startEntry.grid(column=1, row=1)
enterBtn = Button(window, text="Ввод", command=entry)
enterBtn.grid(column=2, row=1, columnspan=1)
sizeLbl = Label(window, text="Размер массива: {}".format(startMassive.size))
sizeLbl.grid(column=3, row=1)

# 3 row
emptyBtn = Button(window, text="numpy.empty()", command=empty)
emptyBtn.grid(column=0, row=2)
generateBtn = Button(window, text="np.random.randint", command=generate)
generateBtn.grid(column=1, row=2)
zeroesBtn = Button(window, text="np.zeroes()", command=zeroes)
zeroesBtn.grid(column=2, row=2)
onesBtn = Button(window, text="np.ones()", command=ones)
onesBtn.grid(column=3, row=2)

# 4 row
indexLabel = Label(window, text="arr[i]")
indexLabel.grid(column=0, row=3)
indexEntry = Entry(window, width=5)
indexEntry.grid(column=1, row=3)
indexButton = Button(window, text=" = ", command=index)
indexButton.grid(column=2, row=3)
indexLabel3 = Label(window, text="")
indexLabel3.grid(column=3, row=3)

# 5 row
indexArrLabel = Label(window, text="arr[array]")
indexArrLabel.grid(column=0, row=4)
indexArrEntry = Entry(window, width=20)
indexArrEntry.grid(column=1, row=4)
indexArrButton = Button(window, text=" = ", command=indexer)
indexArrButton.grid(column=2, row=4)
indexArrLabel3 = Label(window, text="")
indexArrLabel3.grid(column=3, row=4)

# 6 row
indexSrzLabel = Label(window, text="arr[i:j:k]")
indexSrzLabel.grid(column=0, row=5)
indexSrzEntry = Entry(window, width=20)
indexSrzEntry.grid(column=1, row=5)
indexSrzButton = Button(window, text=" = ", command=srz)
indexSrzButton.grid(column=2, row=5)
indexSrzLabel3 = Label(window, text="")
indexSrzLabel3.grid(column=3, row=5)

# 7 row
nonzeroLabel = Label(window, text="nonzero(arr): ")
nonzeroLabel.grid(column=0, row=6)
nonzeroLabel1 = Label(window, text="{}".format(np.nonzero(startMassive)))
nonzeroLabel1.grid(column=1, row=6)

# 8 row
sortLbl = Label(window, text="Выберите сортировку:")
sortLbl.grid(column=0, row=7)

# 9 row
infoLbl = Label(window, text="Обычная сортировка")
infoLbl.grid(column=0, row=8)
infoLbl2 = Label(window, text="Возвращает массив индексов")
infoLbl2.grid(column=1, row=8)
infoLbl3 = Label(window, text="Возвращает массив индексов")
infoLbl3.grid(column=2, row=8)

# 10 row
sortBtn = Button(window, text="Sort()", command=sort)
sortBtn.grid(column=0, row=9)
argsortBtn = Button(window, text="Argsort()", command=argsort)
argsortBtn.grid(column=1, row=9)
lexsortBtn = Button(window, text="Lexsort()", command=lexsort)
lexsortBtn.grid(column=2, row=9)

# 11-12 row
SortLbl = Label(window, text="")
SortLbl.grid(column=0, row=10)
SortLbl2 = Label(window, text="")
SortLbl2.grid(column=0, row=11)

# 11-12 row
ArgsortLbl = Label(window, text="")
ArgsortLbl.grid(column=1, row=10)
ArgsortLbl2 = Label(window, text="")
ArgsortLbl2.grid(column=1, row=11)

# 11 - 15 row
LexsortLbl = Label(window, text="")
LexsortLbl.grid(column=2, row=10)
LexsortLbl2 = Label(window, text="")
LexsortLbl2.grid(column=2, row=11)
LexsortLbl3 = Label(window, text="")
LexsortLbl3.grid(column=2, row=12)
LexsortLbl4 = Label(window, text="")
LexsortLbl4.grid(column=2, row=13)
LexsortLbl5 = Label(window, text="")
LexsortLbl5.grid(column=2, row=14)



# 16 row
matrixInfo = Label(window, text="Двумерный массив:")
matrixInfo.grid(column=0, row=15)
matrixLbl = Label(window, text=matrix)
matrixLbl.grid(column=1, row=15)
matrixBtn = Button(window, text='np.random.randint()', command=generatematrix)
matrixBtn.grid(column=2, row=15)

# 17 row


generate()
window.mainloop()
