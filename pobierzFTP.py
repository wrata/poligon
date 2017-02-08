import ftplib

# otwieramy połączenie
ftp = ftplib.FTP("ftp.serwer.jakiś")
ftp.login("login", "haslo")

# przejście do katalogu
ftp.cwd('public_html')

#pobranie pliku (binarnego)
f = open("nazwapliku", "wb")
ftp.retrbinary("RETR nazwapliku_na_serwerze", f.write)
f.close()

# zakończenie połączenia
ftp.quit()
