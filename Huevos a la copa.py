import math
TH = float(input("Temperatura inicial del huevo: "))
T = 20
TE = 100
M = 47
D = 1.038
C = 3.7
K = 0.0054

dividendo = (math.pow(M, (2/3)) * ( C * math.pow(D,(1/3))))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
resultado = dividendo/divisor
resultado2 = math.log(0.76*((TH - TE)/(70 - TE)))
segundos = resultado * resultado2
minutos = round(segundos/60)

print(f"El tiempo máximo para prepararlo a la copa {segundos} seg")
print(f"El tiempo máximo para prepararlo a la copa {minutos} min")


# Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.