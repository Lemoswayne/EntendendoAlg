import heapq
from typing import Dict, List, Tuple, Any, Optional

Graph = Dict[Any, List[Tuple[Any, float]]]

def dijkstra(graph: Graph, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
  
    """
    Calcula as menores distâncias a partir de 'source' usando Dijkstra.

    Parâmetros:
        graph: dict onde cada nó mapeia para uma lista de (vizinho, peso)
               Ex.: {"A": [("B", 2), ("C", 5)], "B": [("C", 1)], ...}
        source: nó de origem

    Retorna:
        dist: menor distância da origem até cada nó
        parent: pai de cada nó no caminho mínimo (para reconstrução de caminho)
    """
    # Distâncias começam como infinito; origem = 0
    dist: Dict[Any, float] = {v: float('inf') for v in graph}
    dist[source] = 0.0

    # Para nós possivelmente não listados como chaves (apenas como vizinhos)
    for u in list(graph.keys()):
        for v, _w in graph[u]:
            if v not in dist:
                dist[v] = float('inf')

    parent: Dict[Any, Optional[Any]] = {v: None for v in dist}

    # Fila de prioridade (distância acumulada, nó)
    pq: List[Tuple[float, Any]] = [(0.0, source)]
    visited = set()

    while pq:
        d_u, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        # Se a distância no heap estiver desatualizada, ignore
        if d_u > dist[u]:
            continue

        # Itera vizinhos de u (grafo pode ser esparso)
        for v, w in graph.get(u, []):
            if w < 0:
                raise ValueError("Dijkstra não suporta pesos negativos.")
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


def reconstruir_caminho(parent: Dict[Any, Optional[Any]], target: Any) -> List[Any]:
    """
    Reconstrói o caminho da origem até 'target' usando o mapa de pais.
    """
    if target not in parent:
        return []
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


# ------------------ EXEMPLO DE USO ------------------
if __name__ == "__main__":
    # Grafo dirigido com pesos não-negativos (lista de adjacência)
    # A --2--> B --1--> C
    # A --5--> C
    # B --2--> D
    # C --3--> D
    graph: Graph = {
        "A": [("B", 2), ("C", 5)],
        "B": [("C", 1), ("D", 2)],
        "C": [("D", 3)],
        "D": []
    }

    source = "A"
    dist, parent = dijkstra(graph, source)

    print("Menores distâncias a partir de", source)
    for v in sorted(dist):
        print(f"  {source} -> {v}: {dist[v]}")

    destino = "D"
    caminho = reconstruir_caminho(parent, destino)
    print(f"\nCaminho mínimo de {source} até {destino}: {caminho} (custo {dist[destino]})")
