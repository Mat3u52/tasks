
Poniżej moje subiektywne oceny:

1. znajomość python (7/10)
- jak długo pracuje z językiem (3 lata)
- jakie zna wersje (obecnie pracuje na 3.11)
- jakie implementacje (CPython)
- znajomość async (nie stosowalem jeszcze pakietu asynco)
- generatory list comprehension (tak stosowalem)
- socket-y i programowanie sieciowe (tak, ale niewielkie. Tylko podczas pracy z książką: "Black Hat Python, 2nd Edition: Python Programming for Hackers and Pentesters)

2. znajomość postgresql (7/10)
- znajomość zaawansowanych zagadnień (np. windowing functions, replikacje czy load balancing) (nie)
- znajomość innych rdbms/database engine/big data (RDBMS - MySQL, PostgreSQL, SQLite, SQL Server, mongoDB.)

3. znajomość linuxa (6/10)
- jak długo zna/używa (3 lata)
- jako użytkownik czy administrator (root)
- jakie dystrybucje (wcześniej Ubuntu obecnie Kali)

4. znajomość git (kontrola wersji) (5/10)
- znajomość innych systemów (git, svn, csv, inne) (tylko teoretyczne)

5. znajomość IDE do programowania (6/10)
- jakie IDE (PyCharm, IDLE, Visual Studio Code, Notepad++, Code::Blocks dla C++)

6. znajomość programowania webserwisów (klient i serwer) (6/10)
- jakie (REST, SOAP, XMLRPC, g, itp.) (REST API w Django)

7. znajomość XML, XPath, XSLT (6/10)

8. znajomość protokołów komunikacyjnych (4/10)
- HTTP, websocket i innych (określić wszystkie które się zna)

10. tworzenie HTML (8/10)

11. używanie CSS (7/10)
- czy używa meta-języków SCSS, SASS, LESS itp. (nie)

12. czy zna JavaScript (4/10)
- które wersje (JavaScript 1.4)
- jakie frameworki (nie, troche słyszałem o Node)
- TS (nie)

12. znajomość rozwiązań chmurowych (docker, kubernetes i usług providerów AWS, Microsoft Azure, Google Cloud - i inne.) (2/10)
- jakie (obecnie chce się zapoznać z tym tematem)
- jak długo zna/używa (obecnie chce się zapoznać z tym tematem)

#Zadanie 1:

mając klasę:

class Processor:

def process(self, dta: Optional[dict]) -> tuple:
return tuple(dta.items() or {})

napisz rozszerzenie tej klasy (nowa klasa), która rozszerza działanie metody process tak, że w wyniku pojawi się dodatkowo krotka ('extension', True)

#rozwiązanie:
https://github.com/Mat3u52/tasks/tree/main/task01

#Zadanie 2:

mając kod:

>>> print(0.1 * 0.1)

co zwróci? dlaczego tak a nie inaczej?

jak zrobić by było dobrze, dla tego przypadku i dla innych

pytanie bonusowe: jak powinno się poprawnie operować na liczbach zmiennoprzecinkowych w księgowości i jakie są sposoby zaokrągleń


#rozwiązanie:

Wynikiem operacji print(0.1 * 0.1) jest liczba 0.010000000000000002 błąd zaokrąglenia liczb zmiennoprzecinkowych w Python'nie..
Jest związane z przechowywanie liczb zmiennoprzecinkowych w pamięci komputera. Różnica wynika z niedokładności reprezentacji liczby w systemie binarnym.

https://github.com/Mat3u52/tasks/tree/main/task02

pytanie bonusowe:
w Python używać metod round(), ceil() i floor() do zaokrąglania liczb zmiennoprzecinkowych.

pomocne mogą również okazać moduły math, decimal, numpy i pandas

#Zadanie 3:

Określ, na przykładach, czym się różnią i jakie jest zastosowanie bytes i string

opcjonalnie: czym jest kodowanie znaków

#rozwiązanie:

bytes - typ niemutowane / operowanie na danych binarnych przy pracy z plikami, protokołami sieciowymi, itp
string - typ niemutowane / operowanie na ciągach tekstowych i jego wyświetleniem.

https://github.com/Mat3u52/tasks/tree/main/task03

opcjonalnie: 
Jest to przyporządkowanie liczb do znaków.

poniżej moje proste wykorzystanie tablicy ASCII w dwóch projektach:

w C++ https://github.com/Mat3u52/BarcodeReader.git
w Pytchon https://github.com/Mat3u52/BarcodeReaderPythonVer.git

#Zadanie 4:

napisz program (cli) który wywoływany z opcjonalnym parametrem daty, pobiera cenę złota na daną datę (lub dzisiejszą) z endpoint REST http://api.nbp.pl/

można użyć dowolnych bibliotek

#rozwiązanie:
https://github.com/Mat3u52/tasks/tree/main/task04