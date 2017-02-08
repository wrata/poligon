import ftplib

# otwieramy połączenie
ftp = ftplib.FTP("ftp.serwer")
ftp.login("login", "haslo")

# przejście do katalogu
ftp.cwd('public_html')

# otwarcie pliku
f = open("nazwa_pliku", "r")
ftp.storlines("STOR nazwa_pliku_jaka_ma_byc_na_serwerze", f)
f.close()

#binarny plik:
f = open("footprint.jpg", "rb")
ftp.storbinary("STOR footprint-1.jpg", f, 1024)
f.close()

# zakończenie połączenia
ftp.quit()
