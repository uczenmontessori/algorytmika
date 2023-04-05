Ćwiczenie: Napisz funkcję w Pythonie, która odwraca podany ciąg znaków

Zadanie dla studenta:

Celem tego ćwiczenia jest napisanie funkcji w języku Python, która przyjmuje ciąg znaków jako argument i zwraca ten ciąg w odwrotnej kolejności. Funkcja powinna być zaimplementowana zgodnie z poniższymi wytycznymi:

Nazwa funkcji: odwroc_ciag
Argumenty wejściowe: tekst (typ: str) - ciąg znaków do odwrócenia
Wartość zwracana: ciąg znaków tekst odwrócony (typ: str)
Przykłady użycia funkcji:

python
Copy code
odwrocony_tekst = odwroc_ciag("Python")
print(odwrocony_tekst)  # Wynik: nohtyP

odwrocony_tekst = odwroc_ciag("Witaj świecie!")
print(odwrocony_tekst)  # Wynik: !eiceiws jatiW
Wskazówki:

Aby odwrócić ciąg znaków, można skorzystać z indeksowania wstecznego. W Pythonie można użyć składni tekst[::-1].
Można również spróbować rozwiązania iteracyjnego, iterując przez ciąg znaków i dodając kolejne znaki do nowego ciągu w odwrotnej kolejności.
Upewnij się, że twoja funkcja działa poprawnie dla różnych przypadków testowych, takich jak puste ciągi znaków, ciągi o długości 1, a także dłuższe ciągi.
