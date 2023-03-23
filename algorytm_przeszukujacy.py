import random
a = []
for _ in range(100):
    a.append(random.randint(1,150))
a.append(100)
a = sorted(a)
# print(a)
def wyszukiwanie():
    for element in a:
        licznik_1 = licznik_1 + 1
        if element == 100:
            print("W liście a jest", element)
            break
    else:
        print('nie ma 100')
    print('licznik_1', licznik_1)


def divide(l):
    ix = len(l) // 2
    return l[:ix], l[ix:]


licznik_1 = 0
l1, l2 = divide(a)
for x in range(len(a)):
    n = x
    if l1[0] == 100 or l2[0] == 100:
        print("odnaleziono")
        break
    licznik_1 =+ 1
    if l1[-1] >= 100:
        l1, l2 = divide(l1)
        break
    else:
        l1, l2 = divide(l2)
        break

#Nadal nie działa nie wiem co jeszcze zrobić
print(licznik_1)
print(a)

