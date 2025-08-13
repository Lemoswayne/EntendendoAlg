# Ordenação por Seleção pega o menor/maior elemento e coloca no início de um novo Array

# Função para encotrar o menor elemento em um Array

def buscaMenor(array):
    menor = array[0] # Armazena o valor
    menor_index = 0 # Armazena o índice
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_index = i
    return menor_index

# Função para ordenar o Array

def ordenacao_por_selecao(array): # Ordenação
    novoArray = []
    for i in range(len(array)):
        menor_index = buscaMenor(array) # Encontra o menor e add em um novo array
        novoArray.append(array.pop(menor_index))
    return novoArray

print(ordenacao_por_selecao([5, 3, 6, 2, 10]))