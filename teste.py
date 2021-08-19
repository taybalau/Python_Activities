import numpy as np
from itertools import permutations


def gera_sol_rand(sol):
    for i in range(len(sol)):
        x = np.random.randint(0, 2)
        sol[i] = x
    return sol


def calcula_fo(n, sol, cap, b, p):
    fo = 0  # Valor da Função Objetivo
    c = 0  # Peso atual da mochila
    for i in range(n):
        fo = fo + sol[i]*b[i]
        c = c + sol[i]*p[i]
    if c > cap:
        fo = -1*c
    return fo


def movimento(sol):
    """movimento(sol): função criada para fazer os movimentos de 1 bit e criar uma lista com a vizinhança da solução S em questão, utilizando como
    parâmetro a solução(sol). Ela retorna uma lista com todas as soluções vizinhas."""
    perm = permutations(sol)
    vizinhos = []
    for i in list(perm):
        vizinhos.append(i)
    vizinhos = remove_repetidos(vizinhos)
    return vizinhos


def remove_repetidos(vizinhos):
    """remove_repetidos(vizinhos): função criada para otimizar a busca local por meio da remoção de elementos repetidos da lista de vizinhos.
    Ela retorna a lista sem repetição de vizinhos"""
    l = []
    for i in vizinhos:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def busca(n, vizinhos, cap, b, p):
    """busca(n, vizinhos, cap, b, p): função criada para realizar a busca do ótimo local dentro da lista de vizinhos de uma solução S. Ela retorna a
    solução considerada o melhor vizinho e o resultado da função objetivo da mesma."""
    melhor_fo = calcula_fo(n, vizinhos[0], cap, b, p)
    melhor_vizinho = vizinhos[0]
    for vizinho in vizinhos:
        atual_fo = calcula_fo(n, vizinho, cap, b, p)
        if atual_fo > melhor_fo:
            melhor_fo = atual_fo
            melhor_vizinho = vizinho
    return melhor_vizinho, melhor_fo


n = 8  # Quantidade de Objetos
beneficio = [4, 3, 2, 6, 2, 3, 5, 4]
peso = [5, 4, 3, 9, 4, 2, 6, 7]
cap = 20  # Capacidade da Mochila


# Inicializa os Vetores de Soluções
sol = [0]*n


# Parâmetros
semente = 8365
np.random.randint(semente)


# Decisão inicial
sol = gera_sol_rand(sol)
fo = calcula_fo(n, sol, cap, beneficio, peso)
print(f'Solução Inicial: {sol}')
print(f'Função Objetivo Inicial: {fo}')


# Decisão final
sol = movimento(sol)
sol, fo = busca(n, sol, cap, beneficio, peso)

sol = list(sol)

# Restrições
while True:
    if fo > 0:
        g = sol.index(0)
        sol[g] = 1
        sol = movimento(sol)
        sol, fo = busca(n, sol, cap, beneficio, peso)
        sol = list(sol)
    else:
        while fo < 0:
            g = sol.index(1)
            sol[g] = 0
            sol = movimento(sol)
            sol, fo = busca(n, sol, cap, beneficio, peso)
            sol = list(sol)
        break

print(f'Solução Final: {sol}')
print(f'Função Objetivo Final: {fo}')
