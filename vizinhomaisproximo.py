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

def tsp_vizinho_mais_proximo(matriz_distancias, cidade_inicial=0):
    n = len(matriz_distancias)
    visitadas = set()  
    rota = []          
    custo_total = 0    

    cidade_atual = cidade_inicial
    visitadas.add(cidade_atual)
    rota.append(cidade_atual)

    for _ in range(n - 1):  
        proxima_cidade = None
        menor_distancia = float('inf')
        for proxima in range(n):
            if proxima not in visitadas and matriz_distancias[cidade_atual][proxima] < menor_distancia:
                menor_distancia = matriz_distancias[cidade_atual][proxima]
                proxima_cidade = proxima
        visitadas.add(proxima_cidade)
        rota.append(proxima_cidade)
        custo_total += menor_distancia
        cidade_atual = proxima_cidade

    custo_total += matriz_distancias[cidade_atual][cidade_inicial]
    rota.append(cidade_inicial)

    return rota, custo_total

if __name__ == "__main__":
    quantidades_cidades = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    for n in quantidades_cidades:
        print(f"\n=== Instância com {n} cidades ===")
        matriz_distancias = gerar_matriz_distancias(n)
        
        print("Matriz de distâncias:")
        for linha in matriz_distancias:
            print(linha)
        
        inicio = time.time()
        melhor_rota, custo_minimo = tsp_vizinho_mais_proximo(matriz_distancias)
        fim = time.time()
        
        print(f"Melhor rota: {melhor_rota}")
        print(f"Custo mínimo: {custo_minimo}")
        print(f"Tempo gasto: {fim - inicio:.6f} segundos")