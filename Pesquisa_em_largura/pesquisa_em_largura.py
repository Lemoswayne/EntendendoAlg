# A pesquisa em largura (BFS) é um algoritmo para percorrer ou buscar em estruturas de dados em forma de grafo ou árvore.
# Ele começa em um nó raiz e explora todos os seus vizinhos antes de passar para o próximo nível de nós.

# Primeiro deve ser feito duas perguntas:
# 1. Existe um caminho possivel?
# 2. Qual o caminho minimo?

# Implementação em Python (Caso você queira achar um vendedor de manga no facebook)
# 1. Crie uma fila com seus amigos do facebook
# 2. Retire a primeira pessoa da fila
# 3. Verifique se essa pessoa é o vendedor de manga
# 4. Se sim, retorne o caminho até ela
# 5. Se não, adicione todos os 'vizinhos' dessa pessoa à fila
# 6. Repita até encontrar o vendedor de manga ou a fila estar vazia

grafo = {}

from collections import deque

def pesquisa(nome):
    fila_de_pesquisa = deque() # Cria uma nova lista
    fila_de_pesquisa += grafo["voce"] # Add os vizinhos
    verificados = [] # Registro de pessoas já verificadas
    while fila_de_pesquisa:
        pessoa_atual = fila_de_pesquisa.popleft() # Remove a primeira pessoa da fila
        if pessoa_atual == "vendedor de manga":
            print("Caminho encontrado!")
            break
        elif pessoa_atual not in verificados:
            verificados.append(pessoa_atual)
            fila_de_pesquisa += grafo.get(pessoa_atual, [])

pesquisa("voce")