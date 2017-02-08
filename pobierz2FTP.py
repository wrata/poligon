import urllib
# Otwarcie URLa
input = urllib.urlopen('http://strona.pl/plik.html')
# wczytanie danych jako łańcuch
data = input.read()
#zamknięcie połączenia
input.close()

print data
