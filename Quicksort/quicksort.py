# O Algoritmo quicksort é muito mais rápido que o algoritmo de ordenação por seleção
# Arrays vazios e de um elemento são o caso base.

# Quicksort é O(n log n) em média, mas pode ser O(n²) no pior caso.

# Passo a passo do quicksort

# 1. Escolha um pivô (geralmente o último elemento).
# 2. Particione o array em dois subarrays:
#    - Elementos menores que o pivô.
#    - Elementos maiores que o pivô.
# 3. Recursivamente aplique o quicksort nos subarrays.
# 4. Junte os subarrays e o pivô para formar o array ordenado.

def quicksort(array):
    if len(array) <= 1:
        return array # Arrays vazios e de um elemento são o caso base.
    pivo = array[0] # Caso Recursivo
    menores = [i for i in array[1:] if i <= pivo] # Subarray com elementos menores ou iguais ao pivô
    maiores = [i for i in array[1:] if i > pivo] # Subarray com elementos maiores que o pivô
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10, 5, 2, 3]))