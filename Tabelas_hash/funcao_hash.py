# Uma Função Hash é uma função em que você insere uma string e ela retorna um número
# Cada palavra deve ter um valor hash único

# Quando você combina uma função hash com um array, você cria uma tabela hash
# A tabela hash é O(1) para inserção e busca!!

caderno = dict() # -> Tabela Hash em Python
caderno['maçã'] = 1.2 # Uma maçã custa 1.2
caderno['banana'] = 0.8 # Uma banana custa 0.8
caderno['laranja'] = 2.7 # Uma laranja custa 2.7

print(caderno['banana'])