Algoritmo horafutura 
	i=0
	Escribir "ingrese la hora actual"
	Leer Hactual
	
	Escribir "ingrese la hora futura"
	Leer hfutura
	
	si i <=24
		hour = (Hactual+hfutura) MOD 24
		Escribir "dentro de " , hfutura , " seran las " , hour
	FinSi
	
FinAlgoritmo
