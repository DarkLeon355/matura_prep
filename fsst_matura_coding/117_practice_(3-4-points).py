'''
Matura Übungsaufgabe_017 (4 Punkte)

Schreiben Sie eine Python Klasse, welche ein Konto beschreibt!
Die Klasse Konto soll folgende Attribute haben:
# Bank
# Typ
# Inhaber
# Bindung (in Jahren)
# Kontostand (in EUR)
Bindung und Kontostand sollen optionale Parameter in der init-Methode sein. Wenn sie beim Erzeugen 
des Objekts nicht übergeben werden, sollen sie einen default Wert von 0 haben! Implementieren Sie 
eine Methode 'withdraw()' welche abhängig von Kontostand unterschiedliche print-statements liefert. z.B.:
Kontostand 0 -> Ausgabe: "Nope:-("
Kontostand 1-999 -> Ausgabe: "not too much"
Kontostand >= 1000 Ausgabe: "you're welcome:-)"
Implementieren Sie auch eine __str__(self) Methode, welche die String Repräsentation eines
Objekts darstellt. Alle Attribute sollen in einer Formatierung Ihrer Wahl dargestellt
werden.
Erstellen Sie dann ein paar Konto Objekte (mindestens drei mit unterschiedlichen Kontostand)
Speichern Sie diese in einer Liste. Iterieren Sie über die Liste und rufen Sie jeweils
die withdraw() Methode auf und nutzen Sie die print() Funktion, um die Eigenschaften
der Objekte auszugeben.
Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Ausführungsbeispiel:
Hypo, Sparbuch, Alice, 3 year(s), balance: 0EUR.
Nope:-(
Volksbank, Girokonto, Bob, 0 year(s), balance: 200EUR.
not too much
Post, Onlinekonto, Eve, 1 year(s), balance: 10,000EUR.
you're welcome:-)

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die Definition der Klasse inklusive 'Konstruktor'
1 Punkt für die korrekte Implementierung der __str__() und withdraw() Methoden
1 Punkt für die Erstellung und Speicherung der Objekte
1 Punkt für die korrekte Darstellung der Objekte und der Methodenaufrufe
'''

class Account:
    def __init__(self, bank, type, owner, bind=0, balance=0):
        self.__bank = bank
        self.__type = type
        self.__owner = owner
        self.__bind = bind
        self.__balance = balance

    def withdraw(self):
        if self.__balance == 0:
            print("Nope:-(")
        elif self.__balance < 1000:
            print("not too much")
        else:
            print("you're welcome:-)")

    def __str__(self):
        return (f"{self.__bank}, {self.__type}, {self.__owner}, {self.__bind} year(s), balance: {self.__balance}EUR.")

acc1 = Account("Hypo", "Sparbuch", "Alice", 3)
acc2 = Account("Volksbank", "Giro", "Bob", 0, 200)
acc3 = Account("Post", "Online", "Eve", 1, 10000)
accounts = [acc1, acc2, acc3]

for account in accounts:
    print(account)
    account.withdraw()

