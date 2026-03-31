"""
QUICK SORT - Algoritmo de Ordenação Eficiente

Explicação:
-----------
Quick Sort é um algoritmo de ordenação que utiliza a estratégia DIVIDE E CONQUISTA.
Ele funciona escolhendo um elemento como "pivô" e particionando o array em dois 
subarrays: elementos menores que o pivô e elementos maiores que o pivô.
Depois recursivamente ordena esses subarrays.

Complexidade:
- Melhor caso: O(n log n)
- Caso médio: O(n log n)
- Pior caso: O(n²) - quando o pivô escolhido é sempre o menor ou maior elemento

Vantagens:**
- Muito eficiente na prática
- Usa pouca memória extra (ordenação in-place)
- Fácil de implementar

Desvantagens:
- Pode ser lento com dados muito grandes se o pivô for mal escolhido
- Ordenação não é estável (não mantém a ordem relativa de elementos iguais)
"""


def quick_sort(arr):
    """
    Função principal do Quick Sort.
    
    Parâmetros:
    -----------
    arr : list - Lista de números a serem ordenados
    
    Retorno:
    --------
    list - Lista ordenada em ordem crescente
    """
    # Caso base: se a lista tem 0 ou 1 elemento, já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Escolher o pivô (neste caso, o elemento do meio)
    pivot = arr[len(arr) // 2]
    
    # Partição: dividir em três listas
    # 1. Elementos menores que o pivô
    left = [x for x in arr if x < pivot]
    
    # 2. Elementos iguais ao pivô
    middle = [x for x in arr if x == pivot]
    
    # 3. Elementos maiores que o pivô
    right = [x for x in arr if x > pivot]
    
    # Recursivamente ordenar os subarrays e combinar os resultados
    # A ordem é: elementos menores + pivô + elementos maiores
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    Versão in-place do Quick Sort (mais eficiente em memória).
    Ordena a lista modificando-a diretamente.
    
    Parâmetros:
    -----------
    arr : list - Lista de números a serem ordenados
    low : int - Índice inicial (padrão: 0)
    high : int - Índice final (padrão: len(arr) - 1)
    
    Retorno:
    --------
    list - A mesma lista passada como parâmetro, agora ordenada
    """
    if high is None:
        high = len(arr) - 1
    
    # Caso base: se low >= high, a partição está ordenada
    if low < high:
        # Encontrar a posição do pivô após particionamento
        pivot_index = _partition(arr, low, high)
        
        # Recursivamente ordenar a esquerda do pivô
        quick_sort_inplace(arr, low, pivot_index - 1)
        
        # Recursivamente ordenar a direita do pivô
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def _partition(arr, low, high):
    """
    Função auxiliar que particiona o array.
    Move o pivô para sua posição correta e coloca elementos menores à esquerda
    e elementos maiores à direita.
    
    Parâmetros:
    -----------
    arr : list - Lista sendo particionada
    low : int - Índice inicial
    high : int - Índice final
    
    Retorno:
    --------
    int - Índice da posição final do pivô
    """
    # Usar o último elemento como pivô
    pivot = arr[high]
    
    # i será a posição onde elementos menores terminarão
    i = low - 1
    
    # Percorrer do início até antes do pivô
    for j in range(low, high):
        # Se o elemento atual é menor que o pivô
        if arr[j] < pivot:
            # Incrementar i
            i += 1
            # Trocar arr[i] com arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Colocar o pivô em sua posição final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


# ============================================================================
# EXEMPLOS DE USO
# ============================================================================

print("=" * 70)
print("DEMONSTRAÇÃO DO ALGORITMO QUICK SORT")
print("=" * 70)

# Exemplo 1: Lista Simples
print("\n--- Exemplo 1: Quick Sort Simples (versão com listas) ---")
lista1 = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original:  {lista1}")
lista1_ordenada = quick_sort(lista1)
print(f"Lista ordenada:  {lista1_ordenada}")

# Exemplo 2: Lista com números negativos
print("\n--- Exemplo 2: Quick Sort com números negativos ---")
lista2 = [5, -3, 8, -1, 0, 2, -7, 4]
print(f"Lista original:  {lista2}")
lista2_ordenada = quick_sort(lista2)
print(f"Lista ordenada:  {lista2_ordenada}")

# Exemplo 3: Lista com duplicatas
print("\n--- Exemplo 3: Quick Sort com elementos duplicados ---")
lista3 = [5, 2, 5, 1, 9, 5, 3]
print(f"Lista original:  {lista3}")
lista3_ordenada = quick_sort(lista3)
print(f"Lista ordenada:  {lista3_ordenada}")

# Exemplo 4: Versão in-place (modifica a lista original)
print("\n--- Exemplo 4: Quick Sort In-Place (versão otimizada) ---")
lista4 = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original:     {lista4}")
quick_sort_inplace(lista4)
print(f"Lista ordenada:     {lista4}")

# Exemplo 5: Lista grande (demonstração de desempenho)
print("\n--- Exemplo 5: Quick Sort com 20 números aleatórios ---")
import random
lista5 = [random.randint(1, 100) for _ in range(20)]
print(f"Lista original: {lista5}")
lista5_ordenada = quick_sort(lista5)
print(f"Lista ordenada: {lista5_ordenada}")

# Exemplo 6: Comparação entre as duas versões
print("\n--- Exemplo 6: Comparação entre versões ---")
lista_teste = [42, 17, 93, 5, 28, 61, 39]
print(f"Lista original:              {lista_teste}")

# Versão simples
resultado_simples = quick_sort(lista_teste)
print(f"Quick Sort simples:          {resultado_simples}")

# Versão in-place
lista_teste2 = [42, 17, 93, 5, 28, 61, 39]
quick_sort_inplace(lista_teste2)
print(f"Quick Sort in-place:         {lista_teste2}")

print("\n" + "=" * 70)
print("FIM DA DEMONSTRAÇÃO")
print("=" * 70)
