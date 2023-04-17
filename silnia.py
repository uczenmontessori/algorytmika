# Napisz program w Pythonie, który oblicza silnię liczby, używając rekurencji
#
# Rekurencja to sposób rozwiązania problemu, polegający na wywoływaniu funkcji przez samą siebie. Wyobraź sobie rosyjską lalkę matryoshkę, która składa się z kilku mniejszych lalek umieszczonych jedna w drugiej. Aby dostać się do najmniejszej lalki w środku, musisz wyjąć każdą z kolejnych większych lalek. Proces ten można opisać za pomocą rekurencji, gdzie każde wyjęcie lalki prowadzi do odkrycia kolejnej mniejszej lalki, aż do dotarcia do ostatniej, najmniejszej.
# Teraz przejdźmy do przykładu z rekurencją:
# Przykład: Obliczenie n-tej liczby ciągu Fibonacciego
# Ciąg Fibonacciego to sekwencja liczb, w której każda liczba (za wyjątkiem pierwszych dwóch) jest sumą dwóch poprzednich liczb. Ciąg zaczyna się od 0, 1 i kontynuuje się: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Kod w Pythonie wygląda następująco:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Podaj, którą liczbę ciągu Fibonacciego chcesz obliczyć: "))
print("n-ta liczba ciągu Fibonacciego to:", fibonacci(n))

# Dobrze, teraz, gdy już wiesz, jak używać rekurencji do obliczania liczb ciągu Fibonacciego, spróbujmy inny prosty przykład, który pomoże Ci utrwalić to, czego się nauczyłeś.
# Obliczenie silni liczby
# Silnia to iloczyn wszystkich liczb całkowitych od 1 do n (oznaczana jako n!). Na przykład:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Napisz program w Pythonie, który oblicza silnię liczby, używając rekurencji. Pamiętaj, że w przypadku rekurencji musisz określić przypadek bazowy. Dla silni przypadek bazowy to 0! = 1.
