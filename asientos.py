import numpy as np

precio_normal = 78900
precio_vip = 240000

asientos = np.empty((7,6))

n=0

for f in range(7):
    for c in range(6):
        n+=1
        asientos[f][c] = int(n)
        
asientos_ocupados = asientos

def ver_asientos():
    
    for f in range(7):
        print(f"|{round(asientos[f][0])}\t{round(asientos[f][1])}\t{round(asientos[f][2])}\t\t{round(asientos[f][3])}\t{round(asientos[f][4])}\t{round(asientos[f][5])}|")
        if f==4:
            print(f"|------------------------------------------------|\n|\t\t\t\t\t\t|\n|------------------------------------------------|")

def compra_asientos(n_asiento):
    for f in range(7):
        for c in range(6):
            if asientos_ocupados[f][c] == n_asiento:
                asientos_ocupados[f][c] == 'X'


ver_asientos()
