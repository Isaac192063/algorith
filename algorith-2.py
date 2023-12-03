import random
import time

inicio = time.time()
data = []

# LECTURA DEL ARCHIVO
try:
    with open('Datos42.txt', 'r') as fichero:
        for i in fichero:
            sub_array = list(map(int, i.split()))
            data.append(sub_array)

except Exception as e:
    print(f'algo salio mal. ERROR: {e}')

# Algoritmo




num_soluciones = 30
soluciones_memoria = []
longitud = len(data[0])

for i in range(num_soluciones):
    # lista donde se comprueba que ele elemento ya salio y que no se repita
    lista_repet = []

    for j in range(longitud):
        num = random.randint(0, longitud-1)

        while num in lista_repet:
            num = random.randint(0, longitud-1)

        lista_repet.append(num)

    soluciones_memoria.append(lista_repet)


men = 0
numIteracion = 1000

f = 0
listaTabu = []
for index, solucion_actual in enumerate(soluciones_memoria):
    print('SOLUCIÓN TRABAJADA ACTUALMENTE: ', solucion_actual)
    if index == 0:
        for i in range(len(solucion_actual)-1):
            men += data[solucion_actual[i]][solucion_actual[i+1]] 
            f = i
        men += data[solucion_actual[f+1]][solucion_actual[0]]
    
    # print(men)
    


    for i in range(numIteracion):
        suma = 0
        
        a = random.randint(0, longitud-1)
        b = random.randint(0, longitud-1)

        while a == b:
            b = random.randint(0, longitud-1)

        while listaTabu.count([a,b]) > 0 or listaTabu.count([b,a]) > 0:
            a = random.randint(0, longitud-1)
            b = random.randint(0,longitud-1)

            while a == b:
                b = random.randint(0, longitud-1)

        listaTabu.insert(0,[a,b])


        if len(listaTabu) >= 10:
            listaTabu.pop()

        print('Lista tabu: ',listaTabu)
        print()

        print([a,b])

        print(solucion_actual)

        salir = True

        for i in range(len(solucion_actual)-1):
            # print(data[solucion_actual[i]][solucion_actual[i+1]], end=' ')
            suma += data[solucion_actual[i]][solucion_actual[i+1]]
            if suma>men:
                salir = False
                break
            f = i
        if salir:
            suma += data[solucion_actual[f+1]][solucion_actual[0]]
            # print(data[solucion_actual[f+1]][solucion_actual[0]])

            if suma < men:
                men = suma
                print('------------------------------------------')
                print('el menor : ', men)
                print('------------------------------------------')
            print(suma)

        solucion_actual[a], solucion_actual[b] = solucion_actual[b], solucion_actual[a]

        suma = 0
        salir = True
        for i in range(len(solucion_actual)-1):
            # print(data[solucion_actual[i]][solucion_actual[i+1]], end=' ')
            suma += data[solucion_actual[i]][solucion_actual[i+1]]
            if suma > men:
                salir = False
                break
            f = i

        if salir:
            suma += data[solucion_actual[f+1]][solucion_actual[0]]
            # print(data[solucion_actual[f+1]][solucion_actual[0]])

            if suma < men:
                men = suma
                print('------------------------------------------')
                print('el menor : ', men)
                print('------------------------------------------')
            print(suma)

    print()
    print()
    print()
    
print()
print(men)

final = time.time()

print(final-inicio)

