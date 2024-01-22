Algoritmo queNotaNecesito
	Escribir "nota del certamen 1"
	Leer c1
	
	Escribir "nota del certamen 2"
	Leer c2
	
	Escribir "nota del Laboratorio"
	Leer nl
	
	cn<-(59.5 - (0.3 * nl))/0.7
	c3<-3 * cn - (c1+c2) +1
	
	Escribir "nececita esta nota", c3, "en el certamen 3"
FinAlgoritmo
