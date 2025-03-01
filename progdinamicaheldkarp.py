import random
import itertools
import time

def gerar_matriz_distancias(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distancia = random.randint(1, 100) 
            matriz[i][j] = distancia
            matriz[j][i] = distancia 
    return matriz

def tsp_held_karp(matriz_distancias):
    n = len(matriz_distancias)
    todas_cidades = set(range(1, n))
    
    dp = {}
    predecessores = {}
    for i in range(1, n):
        dp[(frozenset([i]), i)] = matriz_distancias[0][i]
        predecessores[(frozenset([i]), i)] = 0 
    for tamanho_subconjunto in range(2, n):
        for subconjunto in itertools.combinations(todas_cidades, tamanho_subconjunto):
            subconjunto_frozen = frozenset(subconjunto)
            for k in subconjunto:
                subconjunto_sem_k = subconjunto_frozen - {k}
                dp[(subconjunto_frozen, k)], predecessores[(subconjunto_frozen, k)] = min(
                    (
                        dp[(subconjunto_sem_k, m)] + matriz_distancias[m][k],
                        m
                    )
                    for m in subconjunto_sem_k
                )
    custo_minimo, ultima_cidade = min(
        (
            dp[(frozenset(todas_cidades), k)] + matriz_distancias[k][0],
            k
        )
        for k in range(1, n)
    )
    melhor_rota = []
    subconjunto_atual = frozenset(todas_cidades)
    cidade_atual = ultima_cidade
    while subconjunto_atual:
        melhor_rota.append(cidade_atual)
        predecessor = predecessores[(subconjunto_atual, cidade_atual)]
        subconjunto_atual = subconjunto_atual - {cidade_atual}
        cidade_atual = predecessor
    melhor_rota.append(0)  
    melhor_rota.reverse()  
    return custo_minimo, melhor_rota

if __name__ == "__main__":
    quantidades_cidades = [4, 6, 8, 10, 12, 14, 16, 18, 20]
    nome_arquivo = "resultadosprogdinamicaheldkarp.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("| Valor de Entrada | Tempo Gasto |\n")
        arquivo.write("| ---------------- | ----------- |\n")

    for n in quantidades_cidades:
        matriz_distancias = gerar_matriz_distancias(n)
        
        inicio = time.time()
        custo_minimo, melhor_rota = tsp_held_karp(matriz_distancias)
        fim = time.time()
        
        tempo_gasto = fim - inicio

        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(f"| {n} | {tempo_gasto:.8f} |\n")