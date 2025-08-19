# As tabelas hash são usadas para pesquisas em uma escala muito grande
# A resolução DNS utiliza tabelas hash

voted = {} # -> Tabela Hash em Python

def verifica_voto(nome):
  if voted.get(nome):
    print("Você já votou!")
  else:
    voted[nome] = True
    print("Voto registrado com sucesso!")

verifica_voto("João")
verifica_voto("Ana")
verifica_voto("João")
verifica_voto("Ana")

# Tabela Hash pode ser usada para cache (caching) também

cache = {}

def pega_pagina(url):
  if cache.get(url):
    return cache[url] # Pega dados do cache
  else:
    dados = dados_do_servidor(url) # type: ignore
    cache[url] = dados # Salva os dados no seu cache
    return dados

# Colisões são tratadas automaticamente pelo dicionário