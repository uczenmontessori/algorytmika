import random

szukana_liczba = 100


a = []
for _ in range(100):
    a.append(random.randint(1,150))
#a.append(szukana_liczba)
a = sorted(a)


def divide(l):
    ix = len(l) // 2
    return l[:ix], l[ix:]

def wyszukiwanie_binarne(a):
    l1, l2 = divide(a)
    for x in range(len(a)):

        if l2[0]==szukana_liczba:
            print("liczba",szukana_liczba,"jest w liście a")
            break
        else:
            if l2[0]<szukana_liczba:
                l1,l2 = divide(l2)
            else:
                l1,l2 = divide(l1)

wyszukiwanie_binarne(a)
