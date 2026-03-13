
nome = "Ana"
idade = 25
altura = 1.70

"""
Python é uma linguagem dinamicamente tipada.

Ou seja:

você não declara o tipo

Python descobre o tipo automaticamente

"Ana"   → str
25      → int
1.70    → float

Em muitas linguagens:
variável = caixa com valor

Em Python funciona diferente:
variável = referência para objeto

"""

a = [1, 2, 3]
b = a

"""
Agora, tanto a quanto b apontam para o mesmo objeto:
a ───► [1,2,3]
b ───►
"""

b.append(4)

"""
resultado:
a = [1,2,3,4]
b = [1,2,3,4]
Porque ambos apontam para o mesmo objeto
"""

x = 10
y = x
x = 20

print(y)

"""
Python cria um novo objeto, Porque y ainda aponta para o objeto 10.
x ───► [20]

y ───► [10]

"""