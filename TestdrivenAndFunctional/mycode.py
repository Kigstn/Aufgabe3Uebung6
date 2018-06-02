import matplotlib.pyplot as plt
import numpy as np


#Test damit Obere Grenze < Untere Grenze nicht vorkommt
def grenzen_test(a, b) :
    return max(a, b)   

#Formen von einem Array mit genau 99 Stellen -> später genauere Berechnung von der Funktion
def array_uebergabe(a, b) :
    return np.arange(a, b, (b - a) / 99)
 

#Festlegen des darzustellenden Bereiches mit Fehlern falls kein Integer / falls Obere Grenze < Untere Grenze
try:
    x_axis_low  = int(input('Unteres Ende der darzustellenden X-Achse: '))
    x_axis_high = int(input('Oberes Ende der darzustellenden X-Achse: '))
except:
    raise Exception('Bitte nur Integers')
if grenzen_test(x_axis_low, x_axis_high) == x_axis_low :
    raise Exception('Obere Grenze < Untere Grenze')

try:
    y_axis_low  = int(input('Unteres Ende der darzustellenden Y-Achse: '))
    y_axis_high = int(input('Oberes Ende der darzustellenden Y-Achse: '))
except:
    raise Exception('Bitte nur Integers')
if grenzen_test(y_axis_low, y_axis_high) == y_axis_low :
    raise Exception('Obere Grenze < Untere Grenze')


#Übergabe der x_Achsenwerte an die Array Funktion
x_axis = array_uebergabe(x_axis_low, x_axis_high)


#Funktion wird ausgelesen
user_function = input('Bitte Funktion eíngeben (mit "x" als Variable): ')   #Es sollten nur einfach arithmetische Funktionen funktionieren, für sin(x) oder ähnlches fehlen Bibliotheken und ich glaube dann wäre es auch so nicht mehr machbar.


#Y-Werte zu den X-Werten berechnen und in ein Array eintragen
y_axis = []
i = 0
while i < 99 :
    x = x_axis[i]
    y_axis.append(eval(user_function)) #Mit Eval wird der user input als Python Code ausgelesen -> Gefahr: jemand nutzt dies aus um ungewollte Befehle ins Programm einzuschleusen. Gleiches Prinzip wie bei SQL-Incejtion
    i = i + 1


#Anlegen des Koordinatensystemes mit den eingebenen Variablen
plt.axis([x_axis_low, x_axis_high, y_axis_low, y_axis_high])


#Berechnete Werte als Punkte darstellen und verbinden
plt.plot(x_axis, y_axis)


#Anzeigen des Graph
plt.title('Dein Graph:')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.show()