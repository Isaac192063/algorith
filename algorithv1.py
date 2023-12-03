# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Leemos los datos del archivo
data = np.loadtxt('Datos42.txt')

# Definimos el número de ciudades
n = len(data)

# Definimos el tamaño de la lista tabú
tabu_size = 3

# Definimos el número máximo de iteraciones
max_iter = 5000

# Creamos una lista tabú vacía
tabu_list = []

start_time = time.time()



solution = list(range(n))
random.shuffle(solution)


# print(solution)
best_solution = solution.copy()
current_cost = 0

for i in range(n-1):
    current_cost += data[solution[i], solution[i+1]]
current_cost += data[solution[n-1], solution[0]]

best_cost = current_cost


num_iter = 0

while num_iter < max_iter:

    current_solution = solution.copy()
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    while a == b:
        b = random.randint(0, n-1)
    current_solution[a], current_solution[b] = current_solution[b], current_solution[a]


    total = 0
    for i in range(n-1):
        total += data[current_solution[i], current_solution[i+1]]
    total += data[current_solution[n-1], current_solution[0]]

    estaTabu = False

    for tabu in tabu_list:
        if current_solution == tabu:
            estaTabu = True
            break

    if total < current_cost and not estaTabu:
        solution = current_solution.copy()

        current_cost = total
        tabu_list.append(solution.copy())

        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        if current_cost < best_cost:

            # Actualizamos la mejor solución y su costo
            best_solution = solution.copy()
            best_cost = current_cost

    num_iter += 1

end_time = time.time()
print('Costo de la mejor solución: ', best_cost)
print('Tiempo de ejecución: ', end_time - start_time)
print(best_solution)