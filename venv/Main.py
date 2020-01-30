from Person import *

name = "root"
pwd = ""
host = "localhost"
db = "Baza"

vrati = Person(name, pwd, host, db)
vrati.persistPersons("Marko", "Markovic", "28")
print(vrati.fetchPersons())