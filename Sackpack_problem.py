import numpy as np


def gera_sol_rand(sol):
    for i in range(len(sol)):
        x = np.random.randint(0, 2)
        sol[i] = x
    return sol


def calcula_fo(n, sol, cap, b, p):
    fo = 0
    c = 0
    for i in range(n):
        fo = fo + sol[i]*b[i]
        c = c + sol[i]*p[i]
    if c > cap:
        fo = -1*c
    return fo


def movimento(sol):
    vizinhos = []
    for i in range(len(sol)):
        for w in range(i + 1, len(sol)):
            vizinho = sol.copy()
            vizinho[i] = sol[w]
            vizinho[w] = sol[i]
            vizinhos.append(vizinho)
    vizinhos = remove_repetidos(vizinhos)
    return vizinhos


def remove_repetidos(sol):
    l = []
    for i in sol:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def busca(n, vizinhos, cap, b, p):
    melhor_fo = calcula_fo(n, vizinhos[0], cap, b, p)
    melhor_vizinho = vizinhos[0]
    for vizinho in vizinhos:
        atual_fo = calcula_fo(n, vizinho, cap, b, p)
        if atual_fo > melhor_fo:
            melhor_fo = atual_fo
            melhor_vizinho = vizinho
    return melhor_vizinho, melhor_fo


n = 8
beneficio = [4, 3, 2, 6, 2, 3, 5, 4]
peso = [5, 4, 3, 9, 4, 2, 6, 7]
cap = 20

sol = [0]*n
sol_star = [0]*n

semente = 8365
np.random.seed(semente)

sol = gera_sol_rand(sol)
print(sol)
sol = movimento(sol)
a = busca(n, sol, cap, beneficio, peso)

print(a)