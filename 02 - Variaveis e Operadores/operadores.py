

# OPERADORES ARITMÉTICOS
a = 10
b = 3

print(f"soma: {a + b}")
print(f"subtração: {a - b}")
print(f"multiplicação: {a * b}")
print(f"divisão: {a / b}")
print(f"divisão inteira: {a // b}")
print(f"resto da divisão: {a % b}")
print(f"potênciação: {a ** b}")


# OPERADORES DE COMPARAÇÃO

x = 10
y = 5

print(f"igualdade: {x == y}")
print(f"diferença: {x != y}")
print(f"maior: {x > y}")
print(f"menor: {x < y}")
print(f"maior ou igual: {x >= y}")
print(f"menor ou igual: {x <= y}")


# OPERADORES LÓGICOS

"""
| Operador | Significado |
| -------- | ----------- |
| `and`    | E           |
| `or`     | OU          |
| `not`    | NÃO         |

"""


# OPERADORES DE ATRIBUIÇÃO

z = 10

z += 2
print(f"atribuição de soma: {z}")

z -= 2
print(f"atribuição de subtração: {z}")

z *= 2
print(f"atribuição de multiplicação: {z}")

z /= 2
print(f"atribuição de divisão: {z}")


# OPERADORES DE IDENTIDADE

n = [1, 2, 3]
n2 = n

print(f"operador de identidade: {n is n2}")


# OPERADORES DE PERTENCIMENTO

lista = [1, 2, 3]
print(f"operador de pertencimento: {2 in lista}")


# COMPORTAMENTO ESPECIAL EM PYTHON

"""
Alguns operadores funcionam com tipos diferentes

Exemplo:
SOMA DE STRINGS
"Hello " + "World" 
resultado: Hello World

MULTIPLICAÇÃO DE STRINGS
"ha" * 3
resultado: hahaha

"""