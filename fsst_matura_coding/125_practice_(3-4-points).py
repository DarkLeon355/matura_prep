'''
Name:

Übungsbeispiel für Matura 2025 Aufgabe_05 (4 Punkte)

Angabe:
Thread-Beispiel:
Erstellen Sie ein Programm, welches vier Threads erzeugt. Jeder dieser Threads bekommt
aufsteigend eine Zahl zugewiesen und zusätzlich eine zufällige Zahl zwischen 5 und 15 zugewiesen.
Der Thread soll von seiner Thread-Nummer bis zur zufälligen Zahl zählen, 
z.B. Thread 3 mit Zahl 11 soll von 3 bis 11 zählen.
Zwischen jedem Zählschritt soll eine Pause von 10ms liegen. Jede Zahl ist auszugeben im Format:
* 9 * (Thread 3)
Zusätzlich ist für jeden Thread das Produkt der ausgegebenen Zahlen zu berechnen. Also im
Beispiel oben 3*4*5*..*11

Erstellen Sie eine globale Variable overall_result und initialisieren Sie diese mit dem Wert 0.
Am Ende eines jeden Threads soll in dieser Variable die Produkte der Zahlen hinzuaddiert werden.
Gewährleisten Sie, dass der Zugriff auf diese Variable geschützt ist (Lock/Mutex).

Beispielausgabe:
* 1 * (Thread 1)
* 2 * (Thread 2)
* 3 * (Thread 3)
* 4 * (Thread 4)
* 2 * (Thread 1)
* 3 * (Thread 2)
.
.
.
* 10 * (Thread 1)
* 12 * (Thread 3)
Sum of all threads: 103783680


Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

Erreichbare Punkte: 4
Aufteilung der Punkte:
1 Punkt für die korrekte Erzeugung der Threads
1 Punkt für die korrekte Funktionalität (Zählen, Produkt/Summe bilden und Ausgabe)
1 Punkt für die richtige Absicherung der overall_result Variable
1 Punkt für das Abwarten auf alle Threads
'''
# Lösung bitte ab hier!

import threading
import time
import random as r

lock = threading.Lock()
overall_result = 0

def worker(t_num, r_num):
    global overall_result, lock
    count = []
    for n in range(t_num, r_num+1, 1):
        print(f"* {n} * (Thread {t_num})")
        count.append(n)
        time.sleep(0.01)
    
    x = 0
    sum = 1
    while x < len(count):
        sum = sum * count[x]
        x = x + 1
    with lock:
        overall_result = overall_result + sum

num_of_threads = 4
threads = []

while len(threads) < num_of_threads:
    t = threading.Thread(target=worker, args=((len(threads)+1), r.randint(5,15)))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() 

print(overall_result)

