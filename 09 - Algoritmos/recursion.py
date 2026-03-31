"""
ALGORITMO DE RECURSÃO
====================

Recursão é quando uma função chama ela mesma para resolver um problema menor.

COMPONENTES ESSENCIAIS:
1. Caso Base: Condição que para a recursão (evita loop infinito)
2. Caso Recursivo: A função chama ela mesma com um problema menor
3. Progresso: Cada chamada deve se aproximar do caso base


EXEMPLO 1: FATORIAL
===================
Fatorial de n (n!) = n × (n-1) × (n-2) × ... × 1

Explicação:
- Caso Base: fatorial(1) = 1
- Caso Recursivo: fatorial(n) = n × fatorial(n-1)

Exemplo: fatorial(5)
- fatorial(5) = 5 × fatorial(4)
- fatorial(4) = 4 × fatorial(3)
- fatorial(3) = 3 × fatorial(2)
- fatorial(2) = 2 × fatorial(1)
- fatorial(1) = 1  ← CASO BASE (para aqui!)

Voltando (backtracking):
- fatorial(2) = 2 × 1 = 2
- fatorial(3) = 3 × 2 = 6
- fatorial(4) = 4 × 6 = 24
- fatorial(5) = 5 × 24 = 120
"""

def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão.
    
    Args:
        n: Um número inteiro positivo
        
    Returns:
        O fatorial de n
    """
    # PASSO 1: Definir o CASO BASE (quando parar)
    if n <= 1:
        print(f"  → Caso base atingido: fatorial({n}) = 1")
        return 1
    
    # PASSO 2: Caso recursivo - chamar a função com n-1
    print(f"  → Calculando fatorial({n}) = {n} × fatorial({n-1})")
    resultado = n * fatorial(n - 1)
    print(f"  → Voltando: fatorial({n}) = {resultado}")
    return resultado


print("=" * 60)
print("EXEMPLO 1: FATORIAL")
print("=" * 60)
print("\nCalculando fatorial(5):")
resultado = fatorial(5)
print(f"\n✓ Resultado: 5! = {resultado}\n")


"""
EXEMPLO 2: FIBONACCI
====================
Sequência Fibonacci: cada número é a soma dos dois anteriores
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Explicação:
- Caso Base: fibonacci(0) = 0 E fibonacci(1) = 1
- Caso Recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

Exemplo: fibonacci(5)
- fibonacci(5) = fibonacci(4) + fibonacci(3)
- fibonacci(4) = fibonacci(3) + fibonacci(2)
- fibonacci(3) = fibonacci(2) + fibonacci(1)
- fibonacci(2) = fibonacci(1) + fibonacci(0)
- fibonacci(1) = 1 (caso base)
- fibonacci(0) = 0 (caso base)
"""

def fibonacci(n, profundidade=0):
    """
    Calcula o n-ésimo número de Fibonacci.
    
    Args:
        n: Posição na sequência Fibonacci
        profundidade: Para rastreamento visual da recursão
        
    Returns:
        O n-ésimo número de Fibonacci
    """
    indentacao = "  " * profundidade
    
    # PASSO 1: Definir CASOS BASE
    if n == 0:
        print(f"{indentacao}→ Caso base: fibonacci(0) = 0")
        return 0
    
    if n == 1:
        print(f"{indentacao}→ Caso base: fibonacci(1) = 1")
        return 1
    
    # PASSO 2: Caso recursivo - chamar a função duas vezes
    print(f"{indentacao}→ fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2})")
    
    resultado = fibonacci(n - 1, profundidade + 1) + fibonacci(n - 2, profundidade + 1)
    
    print(f"{indentacao}→ Voltando: fibonacci({n}) = {resultado}")
    return resultado


print("=" * 60)
print("EXEMPLO 2: FIBONACCI")
print("=" * 60)
print("\nCalculando fibonacci(5):")
resultado = fibonacci(5)
print(f"\n✓ Resultado: fibonacci(5) = {resultado}\n")


"""
EXEMPLO 3: BUSCA BINÁRIA RECURSIVA
===================================
Encontra um alvo em uma lista ordenada dividindo pela metade.

Explicação:
- Caso Base: elemento encontrado OU lista vazia
- Caso Recursivo: buscar na metade esquerda OU direita

Exemplo: buscar(target=7, lista=[1, 3, 5, 7, 9, 11])
- Meio = 7 (posição 3)
- Encontrado! Retorna posição
"""

def busca_binaria_recursiva(lista, alvo, esquerda=0, direita=None, profundidade=0):
    """
    Busca um alvo em uma lista ordenada usando recursão.
    
    Args:
        lista: Lista de números ORDENADA
        alvo: Número a procurar
        esquerda: Índice inicial (padrão: 0)
        direita: Índice final (padrão: último elemento)
        profundidade: Para rastreamento visual
        
    Returns:
        Índice do alvo ou -1 se não encontrado
    """
    if direita is None:
        direita = len(lista) - 1
    
    indentacao = "  " * profundidade
    
    # PASSO 1: Verificar o CASO BASE (não encontrado)
    if esquerda > direita:
        print(f"{indentacao}→ Elemento não encontrado!")
        return -1
    
    # PASSO 2: Calcular o meio
    meio = (esquerda + direita) // 2
    valor_meio = lista[meio]
    
    print(f"{indentacao}→ Buscando em [{esquerda}:{direita}], meio={meio}, valor={valor_meio}")
    
    # PASSO 3: Verificar se encontrou
    if valor_meio == alvo:
        print(f"{indentacao}✓ ENCONTRADO em índice {meio}!")
        return meio
    
    # PASSO 4: Recursar na metade apropriada
    if valor_meio > alvo:
        print(f"{indentacao}→ {alvo} < {valor_meio}, buscando na esquerda...")
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1, profundidade + 1)
    else:
        print(f"{indentacao}→ {alvo} > {valor_meio}, buscando na direita...")
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita, profundidade + 1)


print("=" * 60)
print("EXEMPLO 3: BUSCA BINÁRIA RECURSIVA")
print("=" * 60)
lista = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"\nLista: {lista}")
print(f"\nBuscando o número 7:")
resultado = busca_binaria_recursiva(lista, 7)
print(f"✓ Posição encontrada: {resultado}\n")

print(f"Buscando o número 13:")
resultado = busca_binaria_recursiva(lista, 13)
print(f"✓ Posição encontrada: {resultado}\n")


"""
EXEMPLO 4: SOMA DE LISTA
=========================
Soma todos os elementos de uma lista recursivamente.

Explicação:
- Caso Base: lista vazia = 0
- Caso Recursivo: primeiro elemento + soma(resto da lista)
"""

def soma_recursiva(lista):
    """
    Calcula a soma de uma lista recursivamente.
    
    Args:
        lista: Lista de números
        
    Returns:
        Soma de todos os elementos
    """
    # PASSO 1: CASO BASE - lista vazia
    if len(lista) == 0:
        print(f"  → Caso base: lista vazia, retorna 0")
        return 0
    
    # PASSO 2: CASO RECURSIVO - pegar primeiro + somar resto
    primeiro = lista[0]
    resto = lista[1:]
    
    print(f"  → soma({lista}) = {primeiro} + soma({resto})")
    resultado = primeiro + soma_recursiva(resto)
    print(f"  → Voltando: {primeiro} + soma({resto}) = {resultado}")
    
    return resultado


print("=" * 60)
print("EXEMPLO 4: SOMA DE LISTA")
print("=" * 60)
lista = [2, 4, 6, 8]
print(f"\nLista: {lista}")
print(f"Calculando soma recursivamente:")
resultado = soma_recursiva(lista)
print(f"\n✓ Resultado: Soma = {resultado}\n")


"""
EXEMPLO 5: CONTAGEM REGRESSIVA (SIMPLES)
==========================================
Conta de n até 0 utilizando recursão.
"""

def contagem_regressiva(n):
    """
    Faz uma contagem regressiva de n até 0.
    
    Args:
        n: Número inicial
    """
    # PASSO 1: CASO BASE - quando n for 0
    if n == 0:
        print("  → 0 (Caso base atingido!)")
        return
    
    # PASSO 2: Imprimir e chamar recursivamente com n-1
    print(f"  → {n}")
    contagem_regressiva(n - 1)


print("=" * 60)
print("EXEMPLO 5: CONTAGEM REGRESSIVA")
print("=" * 60)
print(f"\nContagem regressiva de 5:")
contagem_regressiva(5)
print()


print("=" * 60)
print("RESUMO: PONTOS IMPORTANTES SOBRE RECURSÃO")
print("=" * 60)
print("""
✓ CASO BASE é essencial (evita infinito)
✓ CADA chamada deve se aproximar do caso base
✓ A função chama VERSÃO MENOR do mesmo problema
✓ Python tem limite de profundidade (limita recursão profunda)
✓ Recursão usa PILHA (stack) na memória

QUANDO USAR RECURSÃO:
• Problemas que se dividem naturalmente (árvores, grafos)
• Quando a solução é elegante e fácil de entender
• Backtracking (explorar todas as possibilidades)

QUANDO NÃO USAR:
• Loops simples (use for/while)
• Problemas muito profundos (risco de stack overflow)
• Performance crítica (recursão é mais lenta)
""")
