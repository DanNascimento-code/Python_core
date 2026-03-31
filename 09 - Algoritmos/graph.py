# =====================================================
# ALGORITMO DE GRAFO - EXPLICAÇÃO E IMPLEMENTAÇÃO
# =====================================================
#
# Um GRAFO é uma estrutura de dados composta por:
# - VÉRTICES (nodes): representam entidades
# - ARESTAS (edges): conexões entre vértices
#
# Tipos de Grafos:
# 1. Grafo Direcionado: as arestas têm direção (A -> B ≠ B -> A)
# 2. Grafo Não-Direcionado: as arestas não têm direção (A <-> B)
# 3. Grafo Ponderado: as arestas têm pesos (custos)
#
# Representações comuns:
# - Lista de Adjacência: cada vértice armazena lista de vizinhos
# - Matriz de Adjacência: matriz onde M[i][j] = 1 se existe aresta
#
# =====================================================


# =====================================================
# CLASSE: Grafo usando Lista de Adjacência
# =====================================================

class Grafo:
    """
    Classe para representar um grafo usando lista de adjacência.
    Suporta grafos não-direcionados e ponderados.
    """
    
    def __init__(self):
        """
        Inicializa um grafo vazio.
        Usa um dicionário para armazenar a lista de adjacência.
        """
        self.grafo = {}  # {vértice: [vizinhos]}
    
    def adicionar_vertice(self, vertice):
        """
        Adiciona um vértice isolado ao grafo.
        
        Args:
            vertice: identificador do vértice
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            print(f"✓ Vértice '{vertice}' adicionado ao grafo")
    
    def adicionar_aresta(self, u, v, peso=1):
        """
        Adiciona uma aresta entre dois vértices (não-direcionada).
        
        Args:
            u: primeiro vértice
            v: segundo vértice
            peso: peso da aresta (padrão: 1)
        """
        # Garante que ambos os vértices existem
        if u not in self.grafo:
            self.adicionar_vertice(u)
        if v not in self.grafo:
            self.adicionar_vertice(v)
        
        # Adiciona a aresta nos dois sentidos (grafo não-direcionado)
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))
        print(f"✓ Aresta '{u}' <-> '{v}' (peso: {peso}) adicionada")
    
    def exibir_grafo(self):
        """Exibe a representação do grafo em lista de adjacência."""
        print("\n📊 Estrutura do Grafo (Lista de Adjacência):")
        print("-" * 50)
        for vertice, vizinhos in sorted(self.grafo.items()):
            if vizinhos:
                vizinhos_str = ", ".join([f"{v}(peso:{p})" for v, p in vizinhos])
                print(f"  {vertice}: [{vizinhos_str}]")
            else:
                print(f"  {vertice}: []")
        print("-" * 50)


# =====================================================
# ALGORITMO 1: BFS (Breadth-First Search)
# =====================================================

def bfs(grafo_dict, inicio):
    """
    BFS - Busca em Largura
    
    Estratégia: Explora os vértices nível por nível, começando pela raiz.
    
    Passo a passo:
    1. Inicia com o vértice de início numa fila
    2. Marca o vértice como visitado
    3. Enquanto há vértices na fila:
       - Remove o primeiro vértice da fila
       - Para cada vizinho não visitado:
         * Marca como visitado
         * Adiciona à fila
    4. Retorna a ordem de visitação
    
    Complexidade: O(V + E) onde V = vértices, E = arestas
    Uso: Encontrar caminho mais curto, exploração em níveis
    
    Args:
        grafo_dict: dicionário representando o grafo
        inicio: vértice inicial
    
    Returns:
        Lista com ordem de visitação dos vértices
    """
    print(f"\n🔍 BFS iniciado do vértice '{inicio}'")
    print("=" * 60)
    
    visitados = set()           # Controla vértices visitados
    fila = [inicio]             # Fila para armazenar próximos a explorar
    ordem_visitacao = []        # Ordem de visitação
    
    print(f"Passo 1: Inicia fila com '{inicio}'")
    
    passo = 1
    while fila:
        # Remove o primeiro elemento da fila (FIFO)
        vertice_atual = fila.pop(0)
        
        # Verifica se já foi visitado
        if vertice_atual not in visitados:
            passo += 1
            visitados.add(vertice_atual)
            ordem_visitacao.append(vertice_atual)
            
            print(f"\nPasso {passo}: Visitando vértice '{vertice_atual}'")
            print(f"  - Vizinhos: {[v for v, _ in grafo_dict[vertice_atual]]}")
            
            # Adiciona todos os vizinhos não visitados à fila
            novos_vizinhos = []
            for vizinho, _ in grafo_dict[vertice_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    novos_vizinhos.append(vizinho)
            
            print(f"  - Vizinhos não visitados adicionados à fila: {novos_vizinhos}")
            print(f"  - Fila atual: {fila}")
    
    print(f"\n✓ BFS Concluído!")
    print(f"Ordem de visitação: {ordem_visitacao}")
    print("=" * 60)
    return ordem_visitacao


# =====================================================
# ALGORITMO 2: DFS (Depth-First Search)
# =====================================================

def dfs(grafo_dict, inicio, visitados=None, ordem_visitacao=None, passo_ref=None):
    """
    DFS - Busca em Profundidade
    
    Estratégia: Explora o máximo possível em cada ramo antes de voltar.
    
    Passo a passo:
    1. Marca o vértice atual como visitado
    2. Para cada vizinho não visitado:
       - Faz chamada recursiva para o vizinho (vai ao máximo de profundidade)
    3. Quando retorna de um ramo, explora outros ramos
    
    Complexidade: O(V + E)
    Uso: Detectar ciclos, ordenação topológica, componentes conexas
    
    Args:
        grafo_dict: dicionário representando o grafo
        inicio: vértice inicial
        visitados: conjunto de vértices visitados
        ordem_visitacao: lista para armazenar ordem
        passo_ref: referência de iteração (para prints)
    
    Returns:
        Lista com ordem de visitação em profundidade
    """
    if visitados is None:
        visitados = set()
        ordem_visitacao = []
        passo_ref = [0]  # Variável para contar passos
        print(f"\n🔍 DFS iniciado do vértice '{inicio}'")
        print("=" * 60)
    
    passo_ref[0] += 1
    visitados.add(inicio)
    ordem_visitacao.append(inicio)
    profundidade = len(visitados) - 1
    espacos = "  " * profundidade
    
    print(f"Passo {passo_ref[0]}: Visitando vértice '{inicio}' {espacos}(profundidade: {profundidade})")
    
    # Explora cada vizinho em profundidade
    for vizinho, _ in grafo_dict[inicio]:
        if vizinho not in visitados:
            print(f"{espacos}↓ Descendo para vizinho '{vizinho}'")
            dfs(grafo_dict, vizinho, visitados, ordem_visitacao, passo_ref)
        else:
            print(f"{espacos}⊘ Vizinho '{vizinho}' já visitado (pulando)")
    
    # Se é a chamada inicial, exibe o resultado final
    if passo_ref[0] == len(ordem_visitacao):
        print(f"\n✓ DFS Concluído!")
        print(f"Ordem de visitação: {ordem_visitacao}")
        print("=" * 60)
    
    return ordem_visitacao


# =====================================================
# EXEMPLO DE USO
# =====================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("EXEMPLO 1: Grafo Simples com BFS")
    print("=" * 60)
    
    # Cria um novo grafo
    g1 = Grafo()
    
    # Adiciona vértices e arestas
    print("\n📝 Construindo o grafo:")
    g1.adicionar_aresta('A', 'B')
    g1.adicionar_aresta('A', 'C')
    g1.adicionar_aresta('B', 'D')
    g1.adicionar_aresta('C', 'D')
    g1.adicionar_aresta('D', 'E')
    
    # Exibe a estrutura
    g1.exibir_grafo()
    
    # Executa BFS
    resultado_bfs = bfs(g1.grafo, 'A')
    
    
    print("\n" + "=" * 60)
    print("EXEMPLO 2: Grafo com Pesos (rede de cidades) - BFS")
    print("=" * 60)
    
    g2 = Grafo()
    
    print("\n📝 Construindo rede de cidades:")
    g2.adicionar_aresta('São Paulo', 'Rio de Janeiro', peso=400)
    g2.adicionar_aresta('São Paulo', 'Brasília', peso=1000)
    g2.adicionar_aresta('Rio de Janeiro', 'Brasília', peso=1200)
    g2.adicionar_aresta('Rio de Janeiro', 'Salvador', peso=1600)
    g2.adicionar_aresta('Brasília', 'Salvador', peso=1500)
    
    g2.exibir_grafo()
    
    resultado_bfs2 = bfs(g2.grafo, 'São Paulo')
    
    
    print("\n" + "=" * 60)
    print("EXEMPLO 3: Mesmo Grafo com DFS")
    print("=" * 60)
    
    resultado_dfs = dfs(g2.grafo, 'São Paulo')
    
    
    print("\n" + "=" * 60)
    print("EXEMPLO 4: Grafo Maior - Comparando BFS vs DFS")
    print("=" * 60)
    
    g3 = Grafo()
    
    print("\n📝 Construindo rede social (seguidores):")
    g3.adicionar_aresta('Alice', 'Bob')
    g3.adicionar_aresta('Alice', 'Charlie')
    g3.adicionar_aresta('Bob', 'Diana')
    g3.adicionar_aresta('Bob', 'Eve')
    g3.adicionar_aresta('Charlie', 'Frank')
    g3.adicionar_aresta('Diana', 'George')
    g3.adicionar_aresta('Eve', 'George')
    g3.adicionar_aresta('Frank', 'Henry')
    
    g3.exibir_grafo()
    
    print("\n" + "=" * 60)
    print("COMPARAÇÃO: BFS vs DFS da mesma origem")
    print("=" * 60)
    
    print("\n--- Executando BFS ---")
    resultado_bfs3 = bfs(g3.grafo, 'Alice')
    
    print("\n--- Executando DFS ---")
    resultado_dfs3 = dfs(g3.grafo, 'Alice')
    
    
    print("\n" + "=" * 60)
    print("📊 RESUMO E DIFERENÇAS")
    print("=" * 60)
    print("""
BFS (Breadth-First Search):
  • Explora vértices por NÍVEIS (camada por camada)
  • Resultado: Alice -> Bob -> Charlie -> Diana -> Eve -> Frank -> George -> Henry
  • Melhor para: encontrar caminho mais curto, exploração em níveis
  • Estrutura: usa FILA (queue)

DFS (Depth-First Search):
  • Explora vértices em PROFUNDIDADE (vai fundo em cada ramo)
  • Resultado: Alice -> Bob -> Diana -> George -> Eve -> Charlie -> Frank -> Henry
  • Melhor para: detectar ciclos, componentes conexas, ordenação topológica
  • Estrutura: usa PILHA (stack) ou recursão

    Grafo visual:
           Alice
          /     \\
        Bob    Charlie
       /   \\        |
      Diana Eve    Frank
       |     |       |
       Geo  Geo    Henry
    """)
    
    print("\n" + "=" * 60)
    print("✓ Exemplos concluídos com sucesso!")
    print("=" * 60)
