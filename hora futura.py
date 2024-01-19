t = float(input("ingrese las horas actuales\n:"))
h = float(input("ingrese las horas futuras\n:"))    
hour = 0
for i in range(1, 24):
    hour = (t+h)%24
print(round(hour,2))

# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas: