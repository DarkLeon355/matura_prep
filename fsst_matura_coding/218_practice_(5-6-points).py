'''
Matura Übungsaufgabe_018 (4 Punkte)

Angabe:
Visualisieren Sie mit Hilfe von Matplotlib eine kubische Gleichung der Form:
y=ax³+bx²+cx+d
Der User soll die ganzzahligen Parameter a,b,c und d eingeben, sowie die Start- und Stopppunkte
auf der x-Achse und die Anzahl der Punkte auf der x-Achse.

Achtung: Alle Texte innerhalb des Programms sollen in Englisch sein!

### Beispielhafte Eingabe:
Welcome to the cubic visualizer!
Form of the equation: ax³+bx²+cx+d=0
Enter the parameter a=1
Enter the parameter b=3
Enter the parameter c=0
Enter the parameter d=-2
Enter start point on the x-axis ->-4
Enter end point on the x-axis ->3
Enter number of points on the x-axis ->20


##### Beispielcode für Matplotlib #####
import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

#calculate values for a sine function
for deg in range (0,361,10):
    y = math.sin(math.radians(deg))
    y_values.append(y)
    x_values.append(deg)

plt.plot(x_values, y_values)
plt.title("The sine function")
plt.ylabel("f(x)=sin(x)")
plt.xlabel("Degrees")
plt.show()
########################################

Erreichbare Punkte: 4
Aufteilung der Punkte:  
1 Punkt für die User-Eingabe 
2 Punkt für die korrekte Berechung der y-Werte
1 Punkt für die korrekte Erstellung des Diagramms inklusive Beschriftungen
'''

import matplotlib.pyplot as plt
import math

print("Welcome to the cubic visualizer!\nForm of the equation: ax³+bx²+cx+d=0")
a = int(input("Enter the parameter a="))
b = int(input("Enter the parameter b="))
c = int(input("Enter the parameter c="))
d = int(input("Enter the parameter d="))

startx = int(input("Enter start point on the x-axis ->"))
stopx = int(input("Enter end point on the x-axis ->"))
points = int(input("Enter number of points on the x-axis ->"))

step_size = (stopx-startx)/(points-1)

y_vals = []
x_vals = []

for i in range(points):
    x = startx + i * step_size
    x_vals.append(x)
    y = a*x**3+b*x**2+c*x+d
    y_vals.append(y)

plt.plot(x_vals, y_vals)
plt.title("The cubic function")
plt.ylabel("y")
plt.xlabel("x")
plt.show()