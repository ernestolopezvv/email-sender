import smtplib

server = smtplib.SMTP_SSL("smtp.office365.com", 587)

server.login("A01552124@itesm.mx", "Olasoyneto1*")
server.sendmail("A01552124@itesm.mx",
                "natlovi.98@gmail.com"
                "random email")


server.quit()