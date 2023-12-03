import random
import time
import copy
inicio = time.time()

data = []

# LECTURA DEL ARCHIVO
try:
    with open('nuevo.txt', 'r') as fichero:
        for i in fichero:
            sub_array = list(map(int, i.split()))
            data.append(sub_array)
except Exception as e:
    print(f'algo salio mal. ERROR: {e}')


# soluciones formuladas
soluciones_memoria = []

num_soluciones = 3
longitud = len(data[0])
arreglo_indices = [num for num in range(longitud)]


for _ in range(num_soluciones):
    lista_aleatoria = random.sample(arreglo_indices, longitud)
    soluciones_memoria.append(lista_aleatoria)


men = 0
numIteracion = 5
# mejor_lista = []

listaTabu = []

solucion_actual = soluciones_memoria[0]

for i in range(len(soluciones_memoria[0])-1):
    men += data[solucion_actual[i]][solucion_actual[i+1]]
men += data[solucion_actual[longitud-1]][solucion_actual[0]]
print('menor: ', men)

listaTabu = []
a1, a2, b1, b2 = 0, 0, 0, 0

for solucion_actual in soluciones_memoria:

    print('SOLUCIÓN TRABAJADA ACTUALMENTE: ', solucion_actual)
    suma = 0

    for i in range(len(solucion_actual)-1):
        # print(data[solucion_actual[i]][solucion_actual[i+1]], end=' ')

        suma += data[solucion_actual[i]][solucion_actual[i+1]]

        if i == len(solucion_actual)-2:
            suma += data[solucion_actual[longitud-1]][solucion_actual[0]]
            # print(data[solucion_actual[longitud-1]][solucion_actual[0]])
            if suma < men:
                men = suma
                # mejor_lista.append(copy.copy(solucion_actual))
                print('------------------------------------------')
                print('el menor : ', men)
                print('------------------------------------------')

    for _ in range(numIteracion):

        # print(suma)

        print(men)

        a = random.randint(0, longitud-1)
        b = random.randint(0, longitud-1)

        while a == b:  # verificamos que a y b no esten repetidos
            b = random.randint(0, longitud-1)

        # verificamos que la combinacion del array no se encuentre en la lista tabu
        while [a, b] in listaTabu or [b, a] in listaTabu:
            a = random.randint(0, longitud-1)
            b = random.randint(0, longitud-1)
            # de nuevo verificamos que no esten repetidos
            while a == b:
                b = random.randint(0, longitud-1)

        listaTabu.insert(0, [a, b])

        if len(listaTabu) > 3:
            listaTabu.pop()

        print()
        print([a, b])
        print('Lista tabu: ', listaTabu)
        s = 0
        s1 = 0

        if a == 0:
            a2 = a+1
            b1 == b-1
            if b != longitud-1:
                b2 == b+1
                s =  data[solucion_actual[a]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[b2]]

                s1 =  data[solucion_actual[b]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[a]] +  data[solucion_actual[a]][solucion_actual[b2]]
            else:
                s =  data[solucion_actual[a]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[b]] + data[solucion_actual[longitud-1]][solucion_actual[0]]

                s1 =  data[solucion_actual[b]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[a]] + data[solucion_actual[longitud-1]][solucion_actual[0]]

        elif b == 0:
            a1 = a-1
            b2 == b+1
            if a != longitud-1:
                a2 == a+1
                s = data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[a2]] +  data[solucion_actual[b]][solucion_actual[b2]]

                s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[a2]] +  data[solucion_actual[a]][solucion_actual[b2]]
            else:
                s =  data[solucion_actual[a1]][solucion_actual[a]] +  data[solucion_actual[b]][solucion_actual[b2]] + data[solucion_actual[longitud-1]][solucion_actual[0]]

                s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[a]][solucion_actual[b2]] + data[solucion_actual[longitud-1]][solucion_actual[0]]

        elif a ==longitud-1:

            a1 = a-1
            b2 == b+1

            b1 == b-1

            s = data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[b1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[b2]]

            s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[b1]][solucion_actual[a]] +  data[solucion_actual[a]][solucion_actual[b2]]


        elif b == longitud-1:

            
            a1 = a-1
            a2 == a+1

            b1 == b-1

            s = data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[b]]

            s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[a]]


        elif a+1 == b:
            a1 = a-1
            b2 == b2+1

            b1 == b-1

            s = data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[b1]] +  data[solucion_actual[b1]][solucion_actual[b]] + data[solucion_actual[b]][solucion_actual[b2]]

            s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[b1]] +  data[solucion_actual[b1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[b2]]

        elif b+1 == a:
            a1 = a-1
            a2 == a+1

            b1 == b-1

            s = data[solucion_actual[b1]][solucion_actual[b]] + data[solucion_actual[b]][solucion_actual[a1]] +  data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[a2]]

            s1 = data[solucion_actual[b1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[a1]] +  data[solucion_actual[a1]][solucion_actual[b]] + data[solucion_actual[b]][solucion_actual[a2]]
 
        else:
            a1 = a-1
            b2 == b2+1
            a2 = a+1

            b1 == b-1

            s = data[solucion_actual[a1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[b]] + data[solucion_actual[b]][solucion_actual[b2]]

            s1 =  data[solucion_actual[a1]][solucion_actual[b]] +  data[solucion_actual[b]][solucion_actual[a2]] +  data[solucion_actual[b1]][solucion_actual[a]] + data[solucion_actual[a]][solucion_actual[b2]]

        print('valor actual: ',s)
        print('intercambio: ',s1)

        if s1 < s:
            solucion_actual[a], solucion_actual[b] = solucion_actual[b], solucion_actual[a]
            suma -= s
            print(suma)
            suma += s1
            print(suma)

            if suma < men:
                men = suma
                # mejor_lista.append(copy.copy(solucion_actual))
                print('------------------------------------------')
                print('el menor : ', men)
                print('------------------------------------------')


        print(solucion_actual)

    # print()

print()
print('Vamos: ', men)


final = time.time()

print(final-inicio)
