'''
Matura Übungsaufgabe_019 (4 Punkte)

Angabe:
Schreiben Sie ein Python Commandline Programm, welches
den User den Inhalt einer Maria-DB Datenbank anzeigt und ihn
damit interagieren lässt.
Erweiteren Sie den unten stehenden Code um folgende Punkte:
-> Zeigen Sie dem User den Inhalt der Tabelle 'schueler' in der DB 'matura' an.
-> Fragen sie den User nach welcher Spalte und welchem Wert der die Daten 
   filtern will. Geben Sie dann die entsprechenden Daten aus.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

##### Ausführungsbeispiel #########:
('vorname', 'nachname', 'geschlecht', 'klasse', 'abteilung', 'geburtstag')
('Martin', 'Hauser', 'M', '2BHEL', 'Elektronik', datetime.date(2008, 4, 30))
('Martin', 'Baum', 'M', '3BHEL', 'Elektronik', datetime.date(2007, 5, 11))
('Maria', 'Wasser', 'W', '1AHET', 'Elektrotechnik', datetime.date(2009, 1, 3))
('Franz', 'Fichtner', 'M', '2AHET', 'Elektrotechnik', datetime.date(2008, 7, 17))
('Lisa', 'Luft', 'W', '4AHEL', 'Elektronik', datetime.date(2007, 1, 22))

which column do you want to use for filtering? ->vorname
for which value do you want to filter? ->Martin
### RESULT of your search QUERY ###
('Martin', 'Hauser', 'M', '2BHEL', 'Elektronik', datetime.date(2008, 4, 30))
('Martin', 'Baum', 'M', '3BHEL', 'Elektronik', datetime.date(2007, 5, 11))
##### Ende des Ausführungsbeispiel #########


Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für die erfolgreiche Herstellung der DB-Verbindung
1 Punkt für die korrekte Anzeige des Inhalts der Tabelle 'schueler'
1 Punkt für die korrekte Filterung und Anzeige aller Schüler bezogen auf 
  die Auswahl des Users
1 Punkt für korrektes Schliessen des Cursors und der DB-Connection


###### gegebener code zur Interaktion mit der Datenbank #########
import mysql.connector as mariadb
def database_connection():
    db = mariadb.connect(
        host="localhost",
        user='root',
        password='htl'
    )
    return db

mydb = database_connection()
# create cursor for interaction with the db
mycursor = mydb.cursor()
# list all data bases currently running
mycursor.execute("SHOW DATABASES")
print("these are the local databases:")
for dbs in mycursor:
    print(dbs)

# connect to the matura data base
mycursor.execute("USE matura")

# show all table in the matura DB
print("these are the tables in the 'matura' DB:")
mycursor.execute("SHOW TABLES")
print(mycursor.column_names)
for table in mycursor:
    print(table)

print("this is the description of table schueler")
mycursor.execute("DESCRIBE schueler")
print(mycursor.column_names)
for info in mycursor:
    print(info)


mycursor.close()
mydb.close()
########## ende gegebener code ##########
'''


import mysql.connector as mariadb
def database_connection():
    db = mariadb.connect(
        host="localhost",
        user='root',
        password='htl'
    )
    return db

mydb = database_connection()
# create cursor for interaction with the db
mycursor = mydb.cursor()
# list all data bases currently running
mycursor.execute("SHOW DATABASES")
print("these are the local databases:")
for dbs in mycursor:
    print(dbs)

# connect to the matura data base
mycursor.execute("USE matura")

# show all table in the matura DB
print("these are the tables in the 'matura' DB:")
mycursor.execute("SHOW TABLES")
print(mycursor.column_names)
for table in mycursor:
    print(table)

print("this is the description of table schueler")
mycursor.execute("DESCRIBE schueler")
print(mycursor.column_names)
for info in mycursor:
    print(info)

print("All data from schueler")
mycursor.execute("SELECT * FROM schueler")
for data in mycursor:
    print(data)


col = str(input("which column do you want to use for filtering? -> "))
val = str(input("for which value do you want to filter? -> "))

mycursor.execute(f"SELECT * FROM schueler WHERE {col} = '{val}'")
for data in mycursor:
    print(data)

mycursor.close()
mydb.close()


