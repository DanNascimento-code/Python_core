
"""
As tuplas são estruturas de dados imutáveis e ordenadas/com índices que podem armazenar uma coleção de elementos.
Uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos.
"""

# Criando uma tupla
minha_tupla = (1, 2, 2, 3, 4, 5, "python", True)

# Acessando elementos por índice
print(f"Elemento no índice 0: {minha_tupla[0]}")
print(f"Último elemento: {minha_tupla[-1]}")

# Fatiando a tupla (slicing)
print(f"Elementos do índice 2 ao 5: {minha_tupla[2:6]}")

# Desempacotamento de tupla
a, b, c, d, e, f, g, h = minha_tupla
print(f"Desempacotamento: a={a}, b={b}")



# MÉTODOS DE TUPLAS

# 1. count(): Retorna o número de vezes que um elemento aparece na tupla.
contagem_do_numero_2 = minha_tupla.count(2)
print(f"O número 2 aparece {contagem_do_numero_2} vezes na tupla.")

# 2. index(): Retorna o índice da primeira ocorrência de um elemento.
indice_python = minha_tupla.index("python")
print(f"O elemento 'python' está no índice {indice_python}.")

# Tentando encontrar o índice de um elemento que não existe (gera um ValueError)
try:
    minha_tupla.index(99)
except ValueError as e:
    print(f"Tentativa de encontrar o índice de 99: {e}")


# Imutabilidade da tupla: Tentativa de alterar um elemento (gera um TypeError)
try:
    minha_tupla[0] = 100
except TypeError as e:
    print(f"Tentativa de alterar o primeiro elemento: {e}")
