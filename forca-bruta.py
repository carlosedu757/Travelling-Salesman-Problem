import itertools
import random
import time

def gerar_matriz_distancias(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distancia = random.randint(1, 100)  
            matriz[i][j] = distancia
            matriz[j][i] = distancia  
    return matriz

def calcular_custo_rota(rota, matriz_distancias):
    custo = 0
    for i in range(len(rota) - 1):
        custo += matriz_distancias[rota[i]][rota[i + 1]]
    custo += matriz_distancias[rota[-1]][rota[0]] 
    return custo

def caixeiro_viajante_forca_bruta(matriz_distancias):
    n = len(matriz_distancias)
    cidades = list(range(n))
    menor_custo = float('inf')
    melhor_rota = None

    for permutacao in itertools.permutations(cidades):
        custo_atual = calcular_custo_rota(permutacao, matriz_distancias)
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            melhor_rota = permutacao

    return melhor_rota, menor_custo

if __name__ == "__main__":
    quantidades_cidades = [4, 6, 8, 10, 12]

    # ALGORITMO TEM COMPLEXIDADE FATORIAL, LOGO SE TORNA IMPRATICÁVEL PARA ENTRADA > 14

    for n in quantidades_cidades:
        print(f"\n=== Instância com {n} cidades ===")
        matriz_distancias = gerar_matriz_distancias(n)
        
        print("Matriz de distâncias:")
        for linha in matriz_distancias:
            print(linha)
        
        inicio = time.time()
        melhor_rota, menor_custo = caixeiro_viajante_forca_bruta(matriz_distancias)
        fim = time.time()  
        
        print(f"Melhor rota: {melhor_rota}")
        print(f"Custo mínimo: {menor_custo}")
        print(f"Tempo gasto: {fim - inicio:.6f} segundos")