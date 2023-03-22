# programa para simular el juego piedra papel y tijera

import random

print("Piedra = 1")
print("Papel = 2")
print("Tijera = 3")

# input

# processing

j = int(input("Piedra, papel o tijeras: "))
pc = random.randint(1,3)


if (pc==1):
    if (j==1):
        rta= "Empate"
    elif (j==2):
        rta= "Pierdes"
    elif (j==3):
        rta="Ganaste"
elif (pc==2):
    if(j==1):
        rta="Pierdes"
    elif(j==2):
        rta="empate"
    elif(j==3):
        rta="Ganaste"
elif(pc==3):
    if(j==1):
        rta= "Ganaste"
    elif (j==2):
        rta="Pierdes"
    elif (j==3):
        rta="Empate"

#output        

if j>3:
    print("no es un numero valido")
else: 
    print(rta)