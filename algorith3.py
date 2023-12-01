import random
import time
import copy
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


# soluciones formuladas
soluciones_memoria = []

num_soluciones = 30
longitud = len(data[0])
arreglo_indices = [num for num in range(longitud)]


for _ in range(num_soluciones):
    lista_aleatoria = random.sample(arreglo_indices, longitud)
    soluciones_memoria.append(lista_aleatoria)

# soluciones_memoria.append(arreglo_indices)
# for d in soluciones_memoria:
#     print(d)


men = 0
numIteracion = 500
# mejor_lista = []
listaTabu = []

solucion_actual = soluciones_memoria[0]

for i in range(len(soluciones_memoria[0])-1):
    men += data[solucion_actual[i]][solucion_actual[i+1]] 
men += data[solucion_actual[longitud-1]][solucion_actual[0]]
print('menor<: ',men)

listaTabu = []

for solucion_actual in soluciones_memoria:

    print('SOLUCIÓN TRABAJADA ACTUALMENTE: ', solucion_actual)

    for _ in range(numIteracion):
                
        suma = 0

        for i in range(len(solucion_actual)-1):
            # print(data[solucion_actual[i]][solucion_actual[i+1]], end=' ')
            
            suma += data[solucion_actual[i]][solucion_actual[i+1]]
            if suma <= men:
                if i == len(solucion_actual)-2:
                    suma += data[solucion_actual[longitud-1]][solucion_actual[0]]    
                    # print(data[solucion_actual[longitud-1]][solucion_actual[0]])
                    if suma < men:
                        men = suma
                        # mejor_lista.append(copy.copy(solucion_actual))
                        print('------------------------------------------')
                        print('el menor : ', men)
                        print('------------------------------------------')
            else:
                # print(f'\n{suma}')
                # print(suma)
                suma = 0
                break

        # print(suma)

        print(men)

        a = random.randint(0, longitud-1)
        b = random.randint(0, longitud-1)

        while a == b: #verificamos que a y b no esten repetidos
            b = random.randint(0, longitud-1)

        # verificamos que la combinacion del array no se encuentre en la lista tabu
        while [a,b] in listaTabu or [b,a] in listaTabu:
            a = random.randint(0, longitud-1)
            b = random.randint(0,longitud-1)
            # de nuevo verificamos que no esten repetidos
            while a == b:
                b = random.randint(0, longitud-1)

        listaTabu.insert(0,[a,b])


        if len(listaTabu) > 3:
            listaTabu.pop()

        print()
        print([a,b])
        print('Lista tabu: ',listaTabu)

        solucion_actual[a], solucion_actual[b] = solucion_actual[b], solucion_actual[a]

        print(solucion_actual)


    # print()
    
print()
print('Vamos: ',men)



final = time.time()

print(final-inicio)
