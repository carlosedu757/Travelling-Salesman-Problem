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

    for i in range(1, n):
        dp[(frozenset([i]), i)] = matriz_distancias[0][i]

    for tamanho_subconjunto in range(2, n):
        for subconjunto in itertools.combinations(todas_cidades, tamanho_subconjunto):
            subconjunto_frozen = frozenset(subconjunto)
            for k in subconjunto:
                subconjunto_sem_k = subconjunto_frozen - {k}
                dp[(subconjunto_frozen, k)] = min(
                    dp[(subconjunto_sem_k, m)] + matriz_distancias[m][k]
                    for m in subconjunto_sem_k
                )

    custo_minimo = min(
        dp[(frozenset(todas_cidades), k)] + matriz_distancias[k][0]
        for k in range(1, n)
    )

    return custo_minimo

if __name__ == "__main__":
    quantidades_cidades = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    for n in quantidades_cidades:
        print(f"\n=== Instância com {n} cidades ===")
        matriz_distancias = gerar_matriz_distancias(n)
        
        print("Matriz de distâncias:")
        for linha in matriz_distancias:
            print(linha)
        
        inicio = time.time()
        custo_minimo = tsp_held_karp(matriz_distancias)
        fim = time.time()
        
        print(f"Custo mínimo: {custo_minimo}")
        print(f"Tempo gasto: {fim - inicio:.6f} segundos")