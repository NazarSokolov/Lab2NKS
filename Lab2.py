import copy

Elements = [
    [1, 2], # Початкова точка
    [3, 4],  # 1
    [3, 5, 7],  # 2
    [4, 5, 7],  # 3
    [5, 6],  # 4
    [6, 7],  # 5
    [],  # 6
    [],  # 7
]

p = [ 1,#Початкова точка
      0.91,# 1
      0.16,# 2
      0.03,# 3
      0.91,# 4
      0.06,# 5
      0.44,# 6
      0.08] # 7


def findway(r):
    global c
    if len(r) != 0:
        for i in r:
            ways.append(i)
            findway(Elements[i])
        if len(ways) != 0:
            ways.pop(-1)
    else:
        waysEnd.append(copy.deepcopy(ways))
        ways.pop(-1)

def maketabl():
    k = []
    for c in range(2**len(p)):
        b = ''
        while c > 0:
           b = str(c%2)+b
           c = c//2
        while len(b) < len(p):
            b = '0'+b
        k.append(b)
    return k

def MCorrect(list, ins):
    for i in range(len(list)):
        if ins:
            waysEnd[i].insert(0, 0)
    return list

def findW(b):
    c = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    a = []
    for i in range(len(b)):
        a.append([])
        for j in range(len(b[i])):
            if int(b[i][j]) == 1:
                a[i].append(c[j])
    return a

def getStat(a, b):
    stat = []
    stat2 = []
    for i in a:
        for j in b:
            stat.append(j in i)
        k = False
        for j in stat:
            if j:
                k = True
        stat2.append(k)
        stat.clear()
    k = False
    for i in stat2:
        if not i:
            k = True
    return k

def pop_lust(a):
    i = 2
    while i < len(a):
        if a[i] in Elements[a[i-2]]:
            a.pop(i-1)
        i += 1
    return a


ways = []
waysEnd = []
c = 1
findway(Elements[0])
for i in waysEnd:
    pop_lust(i)
c = 0
while c < len(waysEnd):
    k = 0
    while k < len(waysEnd):
        if c != k and waysEnd[c] == waysEnd[k]:
            waysEnd.pop(k)
        k += 1
    c += 1
waysC = copy.deepcopy(waysEnd)
waysC = MCorrect(waysC, True)
print("Можливі шляхи:")
for i in waysC:
    print("             ",str(i)[1:-1])

comstat = maketabl()
compAll = findW(comstat)
Psum = 0
tbl = []
Ptbl= []
for i in range(len(compAll)):
    if getStat(waysEnd, compAll[i]):
        Ptmp = 1
        tbl.append(comstat[i])
        for j in range(len(comstat[i])):
            if comstat[i][j] == '1':
                Ptmp *= 1 - p[j]
            else:
                Ptmp *= p[j]
        Ptbl.append(Ptmp)
        Psum += Ptmp

print('Psystem =', Psum)
print('Таблиця працездатних станів системи')
print(' ПТ  E1  E2  E3  E4  E5  E6  E7    P')
for i in range(len(tbl)):
    for j in tbl[i]:
        if j == '0':
            print('  + ', end='')
        else:
            print('  - ', end='')
    print('',Ptbl[i])
