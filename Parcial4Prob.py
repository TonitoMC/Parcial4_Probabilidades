import numpy as np
import random

def matriz_transicion(niveles):
    columnas = 0
    for i in range(niveles + 2):
        columnas += i
    matriz_transicion = np.zeros((columnas, columnas))
    nivel_actual = 1
    ultimo_clavo = 0
    while (nivel_actual <= niveles):
        for i in range(ultimo_clavo, ultimo_clavo + nivel_actual):
            matriz_transicion[i, i + nivel_actual] = 0.5
            matriz_transicion[i, i + nivel_actual + 1] = 0.5
        ultimo_clavo = factorial_suma(nivel_actual)
        nivel_actual +=1
    while (ultimo_clavo < columnas):
        matriz_transicion[ultimo_clavo, ultimo_clavo] = 1
        ultimo_clavo += 1
    return matriz_transicion

def factorial_suma(i):
    toreturn = 0
    for j in range (i+1):
        toreturn += j
    return toreturn

def casillero_random():
    casillero_actual = 0
    for i in range(1, 7):
        random_sum = random.choice([i, i + 1])
        casillero_actual += random_sum
    return casillero_actual

attemps = 1000000
win = 0
lose = 0
casillero_21 = 0
casillero_22 = 0
casillero_23 = 0
casillero_24 = 0
casillero_25 = 0
casillero_26 = 0
casillero_27 = 0

for i in range(attemps):
    casillero_aleatorio = casillero_random()
    if (casillero_aleatorio == 21):
        casillero_21 += 1
    elif (casillero_aleatorio == 22):
        casillero_22 += 1
    elif (casillero_aleatorio == 23):
        casillero_23 += 1
    elif (casillero_aleatorio == 24):
        casillero_24 += 1
    elif (casillero_aleatorio == 25):
        casillero_25 += 1
    elif (casillero_aleatorio == 26):
        casillero_26 += 1
    elif (casillero_aleatorio == 27):
        casillero_27 += 1

print("Ley de Grandes Numeros")
print(f"Intentos: {attemps}")
print(f"Casillero 21: {casillero_21}")
print(f"Casillero 22: {casillero_22}")
print(f"Casillero 23: {casillero_23}")
print(f"Casillero 24: {casillero_24}")
print(f"Casillero 25: {casillero_25}")
print(f"Casillero 26: {casillero_26}")
print(f"Casillero 27: {casillero_27}")

casillero_21p = casillero_21 / attemps
casillero_22p = casillero_22 / attemps
casillero_23p = casillero_23 / attemps
casillero_24p = casillero_24 / attemps
casillero_25p = casillero_25 / attemps
casillero_26p = casillero_26 / attemps
casillero_27p = casillero_27 / attemps

print(f"% Casillero 21: {casillero_21p}")
print(f"% Casillero 22: {casillero_22p}")
print(f"% Casillero 23: {casillero_23p}")
print(f"% Casillero 24: {casillero_24p}")
print(f"% Casillero 25: {casillero_25p}")
print(f"% Casillero 26: {casillero_26p}")
print(f"% Casillero 27: {casillero_27p}")

def prob_markov(niveles):
    mat = matriz_transicion(niveles)
    #print(mat)
    matprob = np.linalg.matrix_power(mat, niveles)
    valor_esperado = 0
    for i in range (factorial_suma(niveles), factorial_suma(niveles + 1)):
        valor_esperado += matprob[0,i] * i
        print(f"Casillero {i}: {matprob[0,i]}")
    print(f"Valor Esperado: {valor_esperado}")


print("Cadenas de Markov")
prob_markov(6)