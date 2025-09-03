"""
Resolucao gulosa para o problema de cobertura de conjuntos (set cover).

Ideia: enquanto ainda houver elementos descobertos, escolha o conjunto
que cobre a maior quantidade de elementos restantes.

Isso fornece uma aproximacao boa na pratica, embora nao seja sempre otimo.
"""

from typing import Dict, Set, List


def cobertura_gulosa(universo: Set[str], conjuntos: Dict[str, Set[str]]) -> List[str]:
    escolhidos: List[str] = []
    nao_coberto = set(universo)

    while nao_coberto:
        melhor_conjunto = None
        elementos_cobertos = set()

        for nome, elementos in conjuntos.items():
            cobertos = nao_coberto & elementos
            if len(cobertos) > len(elementos_cobertos):
                melhor_conjunto = nome
                elementos_cobertos = cobertos

        if not melhor_conjunto:
            # Nao ha como cobrir mais elementos
            break

        escolhidos.append(melhor_conjunto)
        nao_coberto -= elementos_cobertos

    return escolhidos


if __name__ == "__main__":
    # Exemplo classico
    estados_necessarios = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    estacoes: Dict[str, Set[str]] = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"},
    }

    resultado = cobertura_gulosa(estados_necessarios, estacoes)
    print("Estacoes escolhidas (aprox. gulosa):", resultado)

