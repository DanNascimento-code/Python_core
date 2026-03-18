

# 1. DEFINIÇÃO BÁSICA
# A palavra-chave 'def' é usada para definir uma função.

def saudacao():
    """
    Esta é uma docstring. É uma boa prática documentar o que a função faz.
    Esta função simplesmente imprime uma saudação.

    Acessando docstrings:
    
    help(minha_funcao)  # Exibe documentação formatada no console
    help(print)         # Funciona com funções built-in
    help(list.append)   # Funciona com métodos
    """
    print("Olá, mundo!")

# Para executar a função, nós a "chamamos" pelo nome:
saudacao()


# =============================================================================
# 2. PARÂMETROS E ARGUMENTOS
# =============================================================================
# Parâmetros: São as variáveis listadas dentro dos parênteses na definição da função.
# Argumentos: São os valores enviados para a função quando ela é chamada.

# -----------------------------------------------------------------------------
# a) Argumentos Posicionais
# -----------------------------------------------------------------------------
# Os argumentos são passados para os parâmetros na ordem em que são definidos.

def saudacao_personalizada(nome):  # 'nome' é um parâmetro
    """Saúda uma pessoa pelo nome."""
    print(f"Olá, {nome}!")

saudacao_personalizada("Maria")  # "Maria" é um argumento posicional


# -----------------------------------------------------------------------------
# b) Argumentos Nomeados (Keyword Arguments)
# -----------------------------------------------------------------------------
# Podemos especificar o nome do parâmetro ao passar o argumento.
# A ordem não importa quando usamos argumentos nomeados.

def descrever_pet(tipo_animal, nome_animal):
    """Mostra informações sobre um animal de estimação."""
    print(f"Eu tenho um {tipo_animal} chamado {nome_animal}.")

descrever_pet(tipo_animal="cachorro", nome_animal="Rex")
descrever_pet(nome_animal="Miau", tipo_animal="gato") # A ordem pode ser trocada


# -----------------------------------------------------------------------------
# c) Parâmetros com Valores Padrão (Default Arguments)
# -----------------------------------------------------------------------------
# Podemos definir um valor padrão para um parâmetro. Se o argumento não for passado,
# o valor padrão será usado. Parâmetros com valor padrão devem vir DEPOIS dos
# parâmetros sem valor padrão.

def descrever_pet_padrao(nome_animal, tipo_animal="cachorro"):
    """Mostra informações com um tipo de animal padrão."""
    print(f"Eu tenho um {tipo_animal} chamado {nome_animal}.")

descrever_pet_padrao("Rex") # Usa o valor padrão "cachorro"
descrever_pet_padrao("Miau", "gato") # O valor padrão é sobrescrito


# -----------------------------------------------------------------------------
# d) Argumentos de Comprimento Variável (*args)
# -----------------------------------------------------------------------------
# Para passar um número variável de argumentos posicionais para uma função.
# O nome 'args' é uma convenção, poderia ser qualquer nome (ex: *numeros).
# A função recebe esses argumentos como uma TUPLA.

def somar_todos(*numeros):
    """Soma todos os números passados como argumentos."""
    print(f"Recebendo os argumentos como a tupla: {numeros}")
    return sum(numeros)

resultado = somar_todos(1, 2, 3, 4, 5)
print(f"A soma é: {resultado}")

resultado_2 = somar_todos(10, 20)
print(f"A soma é: {resultado_2}")


# -----------------------------------------------------------------------------
# e) Argumentos de Palavra-chave de Comprimento Variável (**kwargs)
# -----------------------------------------------------------------------------
# Para passar um número variável de argumentos nomeados para uma função.
# O nome 'kwargs' (keyword args) é uma convenção.
# A função recebe esses argumentos como um DICIONÁRIO.

def montar_perfil(nome, **info_adicional):
    """Monta um perfil de usuário."""
    perfil = {'nome': nome}
    perfil.update(info_adicional)
    return perfil

perfil_usuario = montar_perfil("Ana", idade=30, cidade="São Paulo", profissao="Engenheira")
print(perfil_usuario)


# -----------------------------------------------------------------------------
# f) Parâmetros Apenas por Posição (Positional-Only /) e Apenas Nomeados (Keyword-Only *)
# -----------------------------------------------------------------------------
# A partir do Python 3.8, podemos forçar que certos parâmetros sejam apenas
# posicionais ou apenas nomeados.

# - Tudo antes da / deve ser passado por posição.
# - Tudo depois da * deve ser passado por nome.
# - O que está entre / e * pode ser passado de ambas as formas.

def funcao_hibrida(pos_arg1, pos_arg2, /, pos_ou_kw, *, kw_arg1, kw_arg2):
    """
    Função que demonstra parâmetros positional-only e keyword-only.
    - pos_arg1, pos_arg2: Apenas posicionais
    - pos_ou_kw: Posicional ou nomeado
    - kw_arg1, kw_arg2: Apenas nomeados (keyword-only)
    """
    print(f"pos_arg1: {pos_arg1}")
    print(f"pos_arg2: {pos_arg2}")
    print(f"pos_ou_kw: {pos_ou_kw}")
    print(f"kw_arg1: {kw_arg1}")
    print(f"kw_arg2: {kw_arg2}")

# Chamada válida
funcao_hibrida(1, 2, 3, kw_arg1="a", kw_arg2="b")
funcao_hibrida(1, 2, pos_ou_kw=3, kw_arg1="a", kw_arg2="b")

# Chamada inválida (TypeError)
# funcao_hibrida(pos_arg1=1, pos_arg2=2, pos_ou_kw=3, kw_arg1="a", kw_arg2="b") # pos_arg1 não pode ser nomeado
# funcao_hibrida(1, 2, 3, "a", "b") # kw_arg1 e kw_arg2 devem ser nomeados


# =============================================================================
# 3. O COMANDO 'return'
# =============================================================================
# 'return' é usado para sair de uma função e retornar um valor.
# Uma função pode retornar qualquer tipo de objeto (números, strings, listas, etc.).
# Se 'return' não for especificado, a função retorna 'None' implicitamente.

def calcular_area_quadrado(lado):
    """Calcula e retorna a área de um quadrado."""
    if lado <= 0:
        print("O lado deve ser um número positivo.")
        return  # Retorna None implicitamente
    return lado * lado

area = calcular_area_quadrado(5)
print(f"A área é {area}")

# -----------------------------------------------------------------------------
# a) Retornando Múltiplos Valores
# -----------------------------------------------------------------------------
# Em Python, uma função pode retornar múltiplos valores. Isso é feito
# retornando uma tupla (os parênteses são opcionais).

def obter_coordenadas():
    """Retorna uma tupla de coordenadas."""
    return 10, 20  # Retorna a tupla (10, 20)

x, y = obter_coordenadas()  # "Desempacotamento" da tupla
print(f"Coordenadas: x={x}, y={y}")

coordenadas = obter_coordenadas()
print(f"Coordenadas como uma tupla: {coordenadas}")


# =============================================================================
# 4. ESCOPO DE VARIÁVEIS (LEGB Rule)
# =============================================================================
# Python busca por variáveis na seguinte ordem:
# L (Local): Dentro da função.
# E (Enclosing): Em funções aninhadas (funções dentro de funções).
# G (Global): No escopo principal do script.
# B (Built-in): Nomes pré-definidos do Python (ex: print, len).

variavel_global = "Eu sou global"

def minha_funcao():
    variavel_local = "Eu sou local"
    print(variavel_local)   # Acessa a variável local
    print(variavel_global)  # Acessa a variável global

minha_funcao()

# print(variavel_local) # Isso daria um NameError, pois a variável é local à função.

# -----------------------------------------------------------------------------
# a) Palavras-chave 'global' e 'nonlocal'
# -----------------------------------------------------------------------------
# Para modificar uma variável global dentro de uma função, usa-se 'global'.
# Para modificar uma variável de uma função "enclosing" (de fora), usa-se 'nonlocal'.

contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador dentro da função: {contador}")

incrementar()
incrementar()
print(f"Contador fora da função: {contador}")


def funcao_externa():
    x = "externo"
    def funcao_interna():
        nonlocal x
        x = "interno"
        print(f"Dentro da interna: {x}")
    funcao_interna()
    print(f"Fora da interna: {x}")

funcao_externa()


# =============================================================================
# 5. TÉCNICAS E USOS AVANÇADOS
# =============================================================================

# -----------------------------------------------------------------------------
# a) Funções como Cidadãos de Primeira Classe
# -----------------------------------------------------------------------------
# Em Python, funções são objetos. Isso significa que você pode:
# - Atribuí-las a variáveis.
# - Armazená-las em estruturas de dados (listas, dicionários).
# - Passá-las como argumentos para outras funções (Higher-Order Functions).
# - Retorná-las de outras funções.

def somar(a, b):
    return a + b

operacao = somar  # Atribuindo a função a uma variável
print(f"Resultado usando a variável 'operacao': {operacao(4, 5)}")

def calcular(func, a, b):
    """Esta é uma Higher-Order Function, pois recebe uma função como argumento."""
    return func(a, b)

resultado_calculo = calcular(somar, 10, 5)
print(f"Resultado do cálculo: {resultado_calculo}")

# -----------------------------------------------------------------------------
# b) Funções Anônimas (Lambda)
# -----------------------------------------------------------------------------
# São pequenas funções, de uma única linha, definidas com a palavra-chave 'lambda'.
# Sintaxe: lambda argumentos: expressao

# Função normal
def quadrado(x):
    return x ** 2

# Função lambda equivalente
quadrado_lambda = lambda x: x ** 2

print(f"Quadrado (normal): {quadrado(5)}")
print(f"Quadrado (lambda): {quadrado_lambda(5)}")

# Uso comum: com funções como map(), filter() e sorted()
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares encontrados com filter e lambda: {pares}")

# -----------------------------------------------------------------------------
# c) Type Hinting (Anotações de Tipo)
# -----------------------------------------------------------------------------
# A partir do Python 3.5, podemos adicionar "dicas" de tipo para os parâmetros
# e o valor de retorno. Isso não é obrigatório e não afeta a execução, mas
# melhora a legibilidade e é usado por ferramentas de análise de código estático.

def saudacao_com_tipos(nome: str, idade: int) -> str:
    """Função com anotações de tipo."""
    return f"Olá, {nome}. Você tem {idade} anos."

mensagem = saudacao_com_tipos("Carlos", 40)
print(mensagem)


# -----------------------------------------------------------------------------
# d) Recursão
# -----------------------------------------------------------------------------
# Uma função é recursiva se ela chama a si mesma. É uma técnica poderosa para
# resolver problemas que podem ser divididos em subproblemas menores e idênticos.
# É crucial ter um "caso base" para evitar um loop infinito.

def fatorial(n: int) -> int:
    """Calcula o fatorial de um número usando recursão."""
    # Caso base: fatorial de 0 ou 1 é 1
    if n <= 1:
        return 1
    # Caso recursivo: n * fatorial(n-1)
    else:
        return n * fatorial(n - 1)

resultado_fatorial = fatorial(5) # 5 * 4 * 3 * 2 * 1
print(f"Fatorial de 5 é: {resultado_fatorial}")
