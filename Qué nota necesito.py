c1 = int(input("Ingrese nota certamen 1: "))
c2 = int(input("Ingrese nota certamen 2: "))
nl = int(input("Ingrese nota laboratorio: "))

nc = (59.5 - 0.3 * nl) / 0.7 
c3 = 3 * nc - (c1 + c2) + 1 

print("Necesita nota", int(round(c3)), "en el certamen 3")

# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.