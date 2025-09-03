"""
Troco de moedas com abordagem gulosa.

Funciona de forma otima para sistemas de moedas canonicos
(ex.: 1, 5, 10, 25; ou 1, 5, 10, 25, 50, 100), mas pode falhar
em sistemas arbitrarios de moedas.
"""

from typing import List, Dict


def troco_guloso(valor: int, moedas: List[int]) -> Dict[int, int]:
    """
    Retorna um dicionario {moeda: quantidade} usando o menor numero
    de moedas por estrategia gulosa (maior moeda primeiro).
    """
    resultado: Dict[int, int] = {}
    restante = valor
    for m in sorted(moedas, reverse=True):
        if m <= 0:
            continue
        qtd = restante // m
        if qtd > 0:
            resultado[m] = qtd
            restante -= qtd * m
    return resultado


if __name__ == "__main__":
    # Valor em centavos; moedas canonicas
    moedas = [100, 50, 25, 10, 5, 1]
    valor = 289
    print(f"Valor: {valor} centavos")
    print("Troco guloso:", troco_guloso(valor, moedas))

