"""
MERGE SORT - Algoritmo de Ordenação

Conceito: Merge Sort é um algoritmo de ordenação que utiliza a estratégia de 
"Divisão e Conquista". Ele divide o array em duas metades até chegar a elementos
individuais, depois mescla essas metades de forma ordenada.

Como funciona:
1. DIVIDIR: Divide o array no meio recursivamente
2. CONQUISTAR: Ordena as metades
3. COMBINAR: Mescla as duas metades ordenadas em um único array ordenado

Complexidade: O(n log n) em todos os casos
Espaço: O(n) - precisa de espaço auxiliar para as cópias do array
Estável: SIM (mantém ordem relativa de elementos iguais)
"""

def merge(esquerda, direita):
    """
    Função auxiliar que mescla dois arrays ordenados em um único array ordenado.
    
    Args:
        esquerda (list): Primeira metade ordenada
        direita (list): Segunda metade ordenada
    
    Returns:
        list: Array mesclado e ordenado
    """
    # Passo 1: Criar um array vazio para armazenar o resultado
    resultado = []
    # Passo 2: Inicializar indígenas para percorrer ambos os arrays
    i = 0  # Índice para o array esquerdo
    j = 0  # Índice para o array direito
    
    # Passo 3: Comparar elementos de ambos os arrays enquanto houver elementos em ambos
    while i < len(esquerda) and j < len(direita):
        # Passo 4: Se elemento da esquerda é menor ou igual, adicionar na resultado
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1  # Avançar índice da esquerda
        # Passo 5: Caso contrário, adicionar elemento da direita
        else:
            resultado.append(direita[j])
            j += 1  # Avançar índice da direita
    
    # Passo 6: Adicionar elementos restantes da esquerda (se houver)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Passo 7: Adicionar elementos restantes da direita (se houver)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado


def merge_sort(array):
    """
    Função principal do Merge Sort - ordena um array recursivamente.
    
    Args:
        array (list): Array a ser ordenado
    
    Returns:
        list: Array ordenado
    """
    # Passo 1: Caso base - se o array tem 1 ou 0 elemento, já está "ordenado"
    if len(array) <= 1:
        return array
    
    # Passo 2: Encontrar o ponto do meio do array
    meio = len(array) // 2
    
    # Passo 3: DIVIDIR - Separar o array em duas metades
    esquerda = array[:meio]      # Elementos de 0 até meio-1
    direita = array[meio:]        # Elementos de meio até o final
    
    # Passo 4: CONQUISTAR - Recursivamente ordenar cada metade
    print(f"  Dividindo: {esquerda} e {direita}")
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)
    
    # Passo 5: COMBINAR - Mesclar as duas metades ordenadas
    resultado = merge(esquerda_ordenada, direita_ordenada)
    print(f"  Mesclando: {esquerda_ordenada} + {direita_ordenada} = {resultado}")
    
    return resultado


# ============================================================================
# EXEMPLOS DE USO
# ============================================================================

print("=" * 70)
print("EXEMPLO 1: Ordenando um array simples")
print("=" * 70)

array1 = [38, 27, 43, 3, 9, 82, 10]
print(f"\nArray original: {array1}")
print(f"\nProcesso de divisão e mesclagem:")
array1_ordenado = merge_sort(array1)
print(f"\nArray ordenado: {array1_ordenado}")

print("\n" + "=" * 70)
print("EXEMPLO 2: Ordenando números negativos e positivos")
print("=" * 70)

array2 = [-5, 4, -1, 3, -2, 8, 0]
print(f"\nArray original: {array2}")
print(f"\nProcesso de divisão e mesclagem:")
array2_ordenado = merge_sort(array2)
print(f"\nArray ordenado: {array2_ordenado}")

print("\n" + "=" * 70)
print("EXEMPLO 3: Ordenando array com números duplicados (testa estabilidade)")
print("=" * 70)

array3 = [64, 34, 25, 12, 22, 11, 90, 12, 25]
print(f"\nArray original: {array3}")
print(f"\nProcesso de divisão e mesclagem:")
array3_ordenado = merge_sort(array3)
print(f"\nArray ordenado: {array3_ordenado}")

print("\n" + "=" * 70)
print("EXEMPLO 4: Cases especiais")
print("=" * 70)

# Array vazio
array4 = []
print(f"\nArray vazio: {array4}")
print(f"Resultado: {merge_sort(array4)}")

# Array com 1 elemento
array5 = [42]
print(f"\nArray com 1 elemento: {array5}")
print(f"Resultado: {merge_sort(array5)}")

# Array já ordenado
array6 = [1, 2, 3, 4, 5]
print(f"\nArray já ordenado: {array6}")
array6_result = merge_sort(array6)
print(f"Resultado: {array6_result}")

print("\n" + "=" * 70)
print("RESUMO DO ALGORITMO MERGE SORT")
print("=" * 70)
print("""
✓ Estratégia: Divisão e Conquista
✓ Complexidade de Tempo: O(n log n) - MELHOR, PIOR e MÉDIO caso
✓ Complexidade de Espaço: O(n) - precisa de espaço extra
✓ Estável: SIM - mantém ordem relativa de elementos iguais
✓ Adaptativo: NÃO - mesmo array ordenado leva O(n log n)
✓ In-Place: NÃO - precisa de espaço auxiliar
✓ Melhor uso: Datasets grandes, dados em memória externa, quando estabilidade é importnate
""")
