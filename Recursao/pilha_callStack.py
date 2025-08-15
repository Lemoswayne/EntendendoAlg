# Uma lista tem apenas 2 opções push/pop

# Call Stack com recursão

def fat(x):
    if x == 1: # X vai reduzindo até chegar em 1
        return 1
    else:
        return x * fat(x-1) # Chamada Recursiva

print(fat(5))

# Vai se criando uma pilha de chamadas até chegar em 1 (fim da recursão)
# A pilha é desempilhada na ordem inversa das chamadas, multiplicando tudo.
