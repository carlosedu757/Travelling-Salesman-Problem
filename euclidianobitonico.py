import random
import math
import time

def gerar_pontos_aleatorios(n, limite_x=100, limite_y=100):
    return [(random.uniform(0, limite_x), random.uniform(0, limite_y)) for _ in range(n)]

def calcular_distancia_euclidiana(ponto1, ponto2):
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def calcular_matriz_custos(pontos):
    n = len(pontos)
    matriz_custos = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distancia = calcular_distancia_euclidiana(pontos[i], pontos[j])
            matriz_custos[i][j] = distancia
            matriz_custos[j][i] = distancia  # A matriz é simétrica
    return matriz_custos

def encontrar_caminho_bitonico(pontos):
    pontos_ordenados = sorted(pontos, key=lambda p: p[0])
    caminho = list(range(len(pontos_ordenados))) + list(range(len(pontos_ordenados) - 1, -1, -1))
    return caminho

def salvar_resultados_em_arquivo(nome_arquivo, resultados):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("| Quantidade de pontos | Tempo Gasto |\n")
        arquivo.write("| --------------------- | ----------- |\n")
        for n, tempo in resultados:
            arquivo.write(f"| {n:<21} | {tempo:.8f} |\n")

NUM_PONTOS = [4, 6, 8, 10, 12, 14, 16, 18, 20]  
LIMITE_X = 100  
LIMITE_Y = 100  

resultados = []

for n in NUM_PONTOS:
    inicio = time.time() 
    
    pontos = gerar_pontos_aleatorios(n, LIMITE_X, LIMITE_Y)
    matriz_custos = calcular_matriz_custos(pontos)
    caminho = encontrar_caminho_bitonico(pontos)
    
    fim = time.time() 
    tempo_execucao = fim - inicio 
    
    resultados.append((n, tempo_execucao))
    
    print(f"\n=== Instância com {n} pontos ===\n")
    print("Pontos gerados:")
    for idx, ponto in enumerate(pontos):
        print(f"Ponto {idx}: {ponto}")
    
    print("\nCaminho percorrido (índices dos pontos):")
    print(caminho)

salvar_resultados_em_arquivo("resultadoseuclidianobitonico.txt", resultados)
print("\nResultados salvos no arquivo 'resultadoseuclidianobitonico.txt'.")