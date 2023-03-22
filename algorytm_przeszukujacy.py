import random
a=[]
for _ in range(200):
    a.append(random.randint(1,200))
a.append(100)
a = sorted(a)
# print(a)
licznik_1 = 0
def wyszukiwanie():
    for element in a:
        licznik_1 +=1 
        if element == 100:
            print("W liście a jest", element)
            break
    else:
        print('nie ma 100')
    print('licznik_1', licznik_1)


def divide(l):
    ix = len(l) // 2
    return l[:ix], l[ix:]


l1, l2 = divide(a)
for x in range(len(a)):
    licznik =+ 1
    if l2[0] > 100:
        l1, l2 = divide(l2)
        break
    if l1[len(l1)] > 100:
        l1, l2 = divide(l1)
        break
print(licznik_1)

