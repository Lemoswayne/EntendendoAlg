# Utilizando Pesquisa binária eu posso encontrar um valor em uma lista ordenada dividindo o intervalo ao meio repetidamente, descartando metade a cada passo.

# A pesquisa binária precisa de O(log n) para retornar o valor certo
# A pesquisa simples precisa de O(n) etapas

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto: # Tenta até achar um unico elemento
        meio = (baixo + alto) // 2 # Verifica o elemento do meio
        chute = lista[meio]
        if chute == item: # Acha o item
            return meio
        elif chute > item: # O chute foi muito alto
            alto = meio - 1
        else: # O chute foi muito baixo
            baixo = meio + 1
    return None # O item não existe

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))  # Deve retornar o índice 1
print(pesquisa_binaria(minha_lista, -1))  # Deve retornar None