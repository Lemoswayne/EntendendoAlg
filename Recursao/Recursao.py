# Recursão é quando uma função chama a si mesma para resolver um problema.
# Não há nenhum benefício em performance usando recursão.
# Porem a recursão torna o código mais legível e mais fácil de entender.
# Melhorando a performance do programador
# Toda função recursiva deve ter uma condição de parada.

def recursiva(i):
  if i <= 100:
    print(i)
    recursiva(i+1)
  else:
    print("Fim da recursão")

recursiva(1)