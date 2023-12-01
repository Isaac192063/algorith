matriz = [
    [0,3,4,7,8],
    [2,0,5,6,7],
    [4,6,0,4,6],
    [5,7,3,0,5],
    [6,7,5,6,0],
]

propuesta = [1,0,4,2,3,1]

sum = 0
for i in range(len(propuesta)-1):
    sum += matriz[propuesta[i]][propuesta[i+1]]

print(sum)