import random

szukana_liczba = 100


a = []
for _ in range(100):
    a.append(random.randint(1,150))
a.append(szukana_liczba)
a = sorted(a)

# print(a)
# def wyszukiwanie():
#     for element in a:
#         licznik_1 = licznik_1 + 1
#         if element == szukana_liczba:
#             print("W liście a jest", element)
#             break
#     else:
#         print('nie ma szukana_liczba')
#     print('licznik_1', licznik_1)


def divide(l):
    ix = len(l) // 2
    return l[:ix], l[ix:]


licznik_1 = 0
l1, l2 = divide(a)
for x in range(len(a)):
    n = x
    if len(l1) == 0 or len(l2) == 0:
        print("nie ma szukanej liczby")
        break

    if l1[0] == szukana_liczba or l2[0] == szukana_liczba:
        print("odnaleziono")
        break
    licznik_1 += 1
    if l1[-1] == szukana_liczba:
        l1, l2 = divide(l1)
        break
    else:
        l1, l2 = divide(l2)

else:
    print("nie ma szukanej liczby")


print(licznik_1)
print(a)
