Algoritmo huevoalacopa
	Escribir "ingrese la temperatura inicial del huevo:"
	Leer TH
	T = 20
	TE = 100
	M = 47
	D = 1.038
	C = 3.7
	K = 0.0054
	dividendo = 2^(M * (2/3)) * ( C * 2^(D*(1/3)))
	divisor = (K * 2^(PI* 2)) * 2^((4*PI) / 3* (2/3))
	resultado = dividendo/divisor
	resultado2 = ln(0.76*((TH - TE)/(70 - TE)))
	segundos = resultado * resultado2
	minutos = (segundos/60)
	Escribir "el tiempo maximo para prepararlo a la copa es ", segundoss, " seg"
	Escribir "el tiempo maximo para prepararlo a la copa es ", minutos, " min"
FinAlgoritmo
