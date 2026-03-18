# Controle de Fluxo em Python

"""
O controle de fluxo é a ordem em que as instruções, funções e chamadas de um programa são executadas ou avaliadas.
Em Python, isso é gerenciado principalmente por meio de condicionais, loops e chamadas de função.
"""

# 1. Estruturas Condicionais (if, elif, else)
# -----------------------------------------------
"""
As estruturas condicionais permitem que o programa execute diferentes blocos de código com base em certas condições
serem verdadeiras ou falsas.
"""

# Exemplo 1: if-else
idade = 18
print("Exemplo 1: Verificação de maioridade")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
print("-" * 20)

# Exemplo 2: if-elif-else
nota = 75
print("Exemplo 2: Avaliação de nota")
if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
else:
    print("Conceito D ou F")
print("-" * 20)

# Exemplo 3: Condicionais aninhadas
temperatura = 25
chovendo = False
print("Exemplo 3: Condicionais aninhadas")
if temperatura > 20:
    if not chovendo:
        print("Ótimo dia para um passeio no parque.")
    else:
        print("Está quente, mas chovendo. Melhor ficar em casa.")
else:
    print("Está um pouco frio para passear.")
print("-" * 20)

# Operador Ternário (uma forma concisa de if-else)
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Exemplo 4: Operador Ternário - Status: {status}")
print("-" * 20)


# 2. Estruturas de Repetição (Loops)
# ------------------------------------
"""
Loops são usados para executar um bloco de código repetidamente.
"""

# a) Loop 'for'
# Usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto/set ou string).

# Exemplo 5: Iterando sobre uma lista
print("Exemplo 5: Loop 'for' em uma lista de frutas")
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
print("-" * 20)

# Exemplo 6: Usando a função range()
# A função range() gera uma sequência de números.
print("Exemplo 6: Loop 'for' com range()")
for i in range(5):  # Gera números de 0 a 4
    print(f"Número: {i}")
print("-" * 20)

# Exemplo 7: Loop 'for' com 'else'
# O bloco 'else' em um loop 'for' é executado quando o loop termina normalmente (sem ser interrompido por um 'break').
print("Exemplo 7: Loop 'for' com 'else'")
for i in range(3):
    print(f"Contagem: {i}")
else:
    print("Loop concluído sem interrupções.")
print("-" * 20)


# b) Loop 'while'
# Executa um bloco de código enquanto uma condição for verdadeira.

# Exemplo 8: Loop 'while' simples
print("Exemplo 8: Loop 'while' simples")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # É crucial atualizar a variável de controle para evitar um loop infinito.
print("-" * 20)

# Exemplo 9: Loop 'while' com 'else'
# O 'else' é executado quando a condição do 'while' se torna falsa.
print("Exemplo 9: Loop 'while' com 'else'")
contador = 0
while contador < 3:
    print(f"Contagem (while): {contador}")
    contador += 1
else:
    print("Condição do 'while' tornou-se falsa.")
print("-" * 20)


# 3. Comandos de Controle de Loop (break, continue, pass)
# ---------------------------------------------------------

# a) 'break'
# O comando 'break' interrompe a execução do loop mais interno imediatamente.

# Exemplo 10: Usando 'break' para encontrar um item
print("Exemplo 10: Usando 'break'")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado! Interrompendo o loop.")
        break  # Sai do loop
    print(f"Verificando: {numero}")
print("-" * 20)

# b) 'continue'
# O comando 'continue' pula o restante do código dentro do loop para a iteração atual
# e continua com a próxima iteração.

# Exemplo 11: Usando 'continue' para pular números pares
print("Exemplo 11: Usando 'continue' para pular números pares")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Pula para a próxima iteração se i for par
    print(f"Número ímpar: {i}")
print("-" * 20)

# c) 'pass'
# A instrução 'pass' é uma operação nula. Nada acontece quando ela é executada.
# É útil como um marcador de posição em blocos de código onde a sintaxe exige uma instrução,
# mas nenhuma ação é necessária.

# Exemplo 12: Usando 'pass' como placeholder
print("Exemplo 12: Usando 'pass'")
def minha_funcao_incompleta():
    pass  # Evita um erro de sintaxe até a função ser implementada

class MinhaClasseVazia:
    pass  # Evita um erro de sintaxe

if idade > 18:
    pass  # TODO: Implementar lógica futura aqui
print("O comando 'pass' foi usado para estruturas incompletas.")
print("-" * 20)

# Técnicas Comuns com Loops

# 1. enumerate() - Para obter o índice e o valor ao iterar
print("Técnica 1: enumerate()")
cores = ["vermelho", "verde", "azul"]
for indice, cor in enumerate(cores):
    print(f"Índice {indice}: {cor}")
print("-" * 20)

# 2. zip() - Para iterar sobre múltiplas sequências ao mesmo tempo
print("Técnica 2: zip()")
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
for nome, idade_pessoa in zip(nomes, idades):
    print(f"{nome} tem {idade_pessoa} anos.")
print("-" * 20)

# 3. List Comprehensions - Uma forma concisa de criar listas a partir de iteráveis
print("Técnica 3: List Comprehension")
quadrados = [x**2 for x in range(10) if x % 2 == 0]  # Quadrado dos pares de 0 a 9
print(f"Quadrados dos números pares de 0 a 9: {quadrados}")
print("-" * 20)
