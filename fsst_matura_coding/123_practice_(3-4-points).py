'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_03 (4 Punkte)
Angabe:
Schreiben Sie eine Funktion, welche den Benutzer zur Eingabe einer
positiven Kommazahl auffordert.
Übergabe-Parameter: Ein Fragestring, der dem User bei der Eingabe angezeigt wird
Return-Wert: Die korrekt eingegebene Zahl soll ans Hauptprogramm zurückgegeben werden.

Absicherung:
Die Eingabe soll gegen falsche Eingaben abgesichert sein z.B. negative Zahlen
oder Buchstaben. 
Bei falschen Eingaben soll der User erneut zur Eingabe aufgefordert werden.
Einzige Ausnahme: Wenn der User den String 'stop' eingibt, soll die Funktion None 
ans Hauptprogramm zurückgeben.

Erstellen Sie weiters ein Commandline-Programm, welches zuerst den Namen eines Produktes erfragt.
Dann soll Mithilfe obiger Funktion der Benutzer zur Eingabe einer 
Stückanzahl des Produktes und eines Preises aller Stücke in Euro aufgefordert werden. Anschließend 
ist der Einzelpreis zu berechnen und auf 2 Kommastellen genau auszugeben.
Sollte die Funktion allerdings None zurückgeben, soll das Programm sofort mit exit() beendet werden. 

Ausführungsbeispiel:
Please enter the name of the product: sock
Enter the quantity of the product: -10
This is not a valid value. Please enter a positive number.
Enter the quantity of the product: No
This is not a valid value. Please enter a positive number.
Enter the quantity of the product: 10
Enter the price of all products in Euro: 15
One sock costs 1.50 Euro.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für prinzipielle Funktionalität des Programms (User-Eingabe, 
  Berechnung und -Ausgabe) 
1 Punkt für die korrekte Definition und Verwendung der Funktion
1 Punkte für die Fehlerbehandlung der User-Eingabe 
1 Punkt für die Abbruchoption mittels eingabe von 'end'

'''
# Lösung bitte ab hier!

def user_input(prompt):
    while True:
        try:
            i = input(prompt)
            if i == "stop":
                return None
            else:
                i = float(i)
            if i < 0:
                raise ValueError
            else:
                return i
        except:
            print("This is not a valid value. Please enter a positive number.")
            continue



def main():
    name = str(input("Please enter the name of the product: "))
    quantity = user_input("Enter the quantity of the product: ")
    if quantity == None:
      exit()
    total_cost = user_input("Enter the price of all products in Euro: ")
    if total_cost == None:
      exit()
    print(f"One {name} costs {(total_cost/quantity):.2F} Euro")
    
if __name__ == "__main__":
  main()