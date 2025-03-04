import random
import math
import time
from typing import List, Tuple

def gerar_pontos_aleatorios(n:int, limite_x:int=100, limite_y:int=100) -> List[Tuple[float, float]]:
    """Gera uma lista de n pontos aleatórios com coordenadas x e y dentro dos limites especificados.

    Args:
        n (int): Número de pontos a serem gerados
        limite_x (int, optional): Limite máximo para a coordenada x. Defaults to 100.
        limite_y (int, optional): Limite máximo para a coordenada y. Defaults to 100.

    Returns:
        List[Tuple[float, float]]: Lista de pontos gerados
    """
    return [(random.uniform(0, limite_x), random.uniform(0, limite_y)) for _ in range(n)]

def calcular_distancia_euclidiana(ponto1: Tuple[float, float], ponto2: Tuple[float, float]) -> float:
    """
    Calcula a distância euclidiana entre dois pontos no plano cartesiano.
    
    :param ponto1: Primeiro ponto (x, y)
    :param ponto2: Segundo ponto (x, y)
    :return: Distância euclidiana entre os dois pontos
    """
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def calcular_matriz_custos(pontos: List[Tuple[float, float]]) -> List[List[float]]:
    """
    Cria uma matriz de distâncias euclidianas entre os pontos.
    
    :param pontos: Lista de pontos (x, y)
    :return: Matriz de custos simétrica onde cada elemento (i, j) representa a distância entre os pontos i e j
    """
    n = len(pontos)
    matriz_custos = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distancia = calcular_distancia_euclidiana(pontos[i], pontos[j])
            matriz_custos[i][j] = distancia
            matriz_custos[j][i] = distancia  # A matriz é simétrica
    return matriz_custos

def encontrar_caminho_bitonico(pontos: List[Tuple[float, float]]) -> List[int]:
    """
    Gera um caminho bitônico baseado na ordenação dos pontos pelo eixo X.
    
    :param pontos: Lista de pontos (x, y)
    :return: Lista de índices representando o caminho bitônico
    """
    pontos_ordenados = sorted(pontos, key=lambda p: p[0])
    caminho = list(range(len(pontos_ordenados))) + list(range(len(pontos_ordenados) - 1, -1, -1))
    return caminho

def salvar_resultados_em_arquivo(nome_arquivo: str, resultados: List[Tuple[int, float]]) -> None:
    """
    Salva os tempos de execução em um arquivo de saída formatado.
    
    :param nome_arquivo: Nome do arquivo de saída
    :param resultados: Lista de tuplas contendo (número de pontos, tempo de execução)
    """
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