"""
Mochila fracionaria (fractional knapsack) com estrategia gulosa.

Ordena itens por valor/peso (densidade) e pega o maximo possivel de cada
um nessa ordem. E otimo para a versao fracionaria do problema.
"""

from typing import List, Tuple


def mochila_fracionaria(capacidade: float, itens: List[Tuple[float, float]]) -> Tuple[float, List[Tuple[int, float]]]:
    """
    Calcula o valor maximo possivel colocando fracoes de itens.

    itens: lista de tuplas (valor, peso)
    retorna: (valor_total, lista_de_partes) onde lista_de_partes = [(indice_item, fracao)]
    """
    # Ordena por densidade (valor/peso) desc
    ordenados = sorted(enumerate(itens), key=lambda x: x[1][0] / x[1][1], reverse=True)

    valor_total = 0.0
    partes: List[Tuple[int, float]] = []
    restante = capacidade

    for idx, (valor, peso) in ordenados:
        if restante <= 0:
            break
        if peso <= restante:
            # pega o item inteiro
            valor_total += valor
            partes.append((idx, 1.0))
            restante -= peso
        else:
            # pega apenas uma fracao
            fracao = restante / peso
            valor_total += valor * fracao
            partes.append((idx, fracao))
            restante = 0

    return valor_total, partes


if __name__ == "__main__":
    # (valor, peso)
    itens = [
        (60, 10),
        (100, 20),
        (120, 30),
    ]
    cap = 50
    total, partes = mochila_fracionaria(cap, itens)
    print(f"Valor maximo: {total}")
    print("Partes escolhidas (indice, fracao):", partes)

