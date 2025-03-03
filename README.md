# Travelling Salesman Problem
Este projeto implementa variadas soluções para o Problema do Caixeiro-Viajante (TSP). Os resultados são salvos em um arquivo de texto e alguns dos algoritmos tem saídas no console para mostrar caminhos tomados.

## Requisitos
Para executar este projeto, você precisará de:

**Python 3.x** : Certifique-se de que o Python está instalado em sua máquina. Você pode verificar a versão executando:
```bash
python --version
```
**Bibliotecas Padrão** : Este projeto usa apenas bibliotecas padrão do Python (random, math, time), então não é necessário instalar dependências adicionais.

## Estrutura do Projeto
O projeto consiste nos seguintes arquivos:
```
Travelling-Salesman-Problem/
├── .gitattributes
├── .gitignore
├── euclidianobitonico.py
├── forca-bruta.py
├── progdinamicaheldkarp.py
├── README.md
├── resultadoseuclidianobitonico.txt
├── resultadosforcabruta.txt
├── resultadosprogdinamicaheldkarp.txt               
├── resultadosvizinhomaisproximo.txt
└── vizinhomaisproximo.py           
```

## Como Executar o Projeto
**Passo 1: Clonar ou Baixar o Projeto**
Se você clonou este repositório, navegue até o diretório do projeto:
```bash
cd caminho/para/projeto-bitonico
```
Se você baixou o projeto como um arquivo ZIP, extraia-o e abra o diretório resultante.

**Passo 2: Executar o Código**
Execute o script principal usando o Python:
```bash
python nomedoalgoritmo.py
```
No lugar de 'nomedoalgoritmo.py' insira o algoritmo que você deseja executar, por exemplo: forca-bruta.py.

**Passo 3: Verificar os Resultados**
Após a execução:
- Os pontos ou a matriz gerada e o caminho percorrido serão exibidos no console.
- Um arquivo chamado 'resultadosnomedoalgoritmo.txt' será criado no mesmo diretório, contendo uma tabela com os tempos de execução para diferentes números de pontos ou quantidade de 'vértices'.
- No lugar de 'resultadosnomedoalgoritmo.txt' será o algoritmo que você executou, por exemplo: resultadosforcabruta.txt.


# Resultados

## Força Bruta

Resultado 1

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00100000 |
| 8 | 0.02999666 |
| 10 | 3.26668943 |
| 12 | 502.22026734 |

Resultado 2

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00099921 |
| 6 | 0.00099993 |
| 8 | 0.02699614 |
| 10 | 2.96284938 |
| 12 | 456.44491816 |

Resultado 3

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02726150 |
| 10 | 2.93703413 |
| 12 | 457.01182985 

Resultado 4

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02800322 |
| 10 | 2.99525619 |
| 12 | 455.34606314 |

Resultado 5

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02899623 |
| 10 | 3.06465030 |
| 12 | 467.81789565 |

Resultado 6

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02799296 |
| 10 | 3.03628373 |
| 12 | 450.10159922 |

Resultado 7

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02699566 |
| 10 | 2.91373897 |
| 12 | 443.05231285 |

Resultado 8

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00100493 |
| 8 | 0.02727556 |
| 10 | 2.91017914 |
| 12 | 452.43288612 |

Resultado 9

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.02733231 |
| 10 | 2.89646769 |
| 12 | 456.43570781 |

Resultado 10

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00100136 |
| 8 | 0.02939343 |
| 10 | 3.03891993 |
| 12 | 457.56751800 |



## Programação Dinâmica (Held-Karp)

Resultado 1

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00099850 |
| 10 | 0.00499558 |
| 12 | 0.02699804 |
| 14 | 0.15999770 |
| 16 | 0.97589517 |
| 18 | 5.57927251 |
| 20 | 28.92573857 |

Resultado 2

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00099969 |
| 6 | 0.00000000 |
| 8 | 0.00099301 |
| 10 | 0.00499725 |
| 12 | 0.02899981 |
| 14 | 0.16899967 |
| 16 | 0.98487353 |
| 18 | 5.66005826 |
| 20 | 29.19749784 |

Resultado 3

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00099754 |
| 10 | 0.00499868 |
| 12 | 0.02800322 |
| 14 | 0.16309619 |
| 16 | 0.98554015 |
| 18 | 5.51755261 |
| 20 | 28.69134283 |

Resultado 4

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00100565 |
| 10 | 0.00599742 |
| 12 | 0.02800059 |
| 14 | 0.16450119 |
| 16 | 1.00999427 |
| 18 | 5.72833395 |
| 20 | 30.45861530 |

Resultado 5

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00099826 |
| 10 | 0.00599885 |
| 12 | 0.02900147 |
| 14 | 0.17904758 |
| 16 | 1.03208947 |
| 18 | 5.78523970 |
| 20 | 30.07365465 |

Resultado 6

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00099945 |
| 10 | 0.00600648 |
| 12 | 0.02928686 |
| 14 | 0.17874432 |
| 16 | 1.04231787 |
| 18 | 5.95126677 |
| 20 | 30.06010771 |

Resultado 7

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00099921 |
| 8 | 0.00108075 |
| 10 | 0.00499487 |
| 12 | 0.02967548 |
| 14 | 0.17944121 |
| 16 | 1.09156895 |
| 18 | 5.95704055 |
| 20 | 30.06746697 |

Resultado 8

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00100541 |
| 8 | 0.00100088 |
| 10 | 0.00599337 |
| 12 | 0.02901435 |
| 14 | 0.17600656 |
| 16 | 1.05504227 |
| 18 | 5.88680649 |
| 20 | 30.02699113 |

Resultado 9

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00499463 |
| 12 | 0.02818871 |
| 14 | 0.17055798 |
| 16 | 1.02965713 |
| 18 | 5.95477366 |
| 20 | 29.94501209 |

Resultado 10

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00513053 |
| 12 | 0.03010297 |
| 14 | 0.18610525 |
| 16 | 1.07891083 |
| 18 | 5.99826145 |
| 20 | 29.99116516 |



## Algoritmo Guloso (Vizinho mais próximo)

Resultado 1

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 2

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 3

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 4

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 5

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 6

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 7

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 8

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 9

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |

Resultado 10

| Valor de Entrada | Tempo Gasto |
| ---------------- | ----------- |
| 4 | 0.00000000 |
| 6 | 0.00000000 |
| 8 | 0.00000000 |
| 10 | 0.00000000 |
| 12 | 0.00000000 |
| 14 | 0.00000000 |
| 16 | 0.00000000 |
| 18 | 0.00000000 |
| 20 | 0.00000000 |



## Programação Dinâmica (Euclidiano Bitônico)

Resultado 1



Resultado 2



Resultado 3



Resultado 4



Resultado 5



Resultado 6



Resultado 7



Resultado 8



Resultado 9



Resultado 10



