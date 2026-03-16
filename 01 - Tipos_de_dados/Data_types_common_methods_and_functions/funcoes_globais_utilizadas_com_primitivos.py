
# len()
# Tamanho de uma sequência (lista, tupla, dicionários e etc)
text = "python"
print(f"função len(): {len(text)}")

# min() e max()
# usadas para encontrar os valores mínimo e máximo em um conjunto de dados
print(f"função min(): {min(10, 5, 8)}")
print(f"função max(): {max(10, 5, 8)}")

# sum()
# usada para somar os elementos de uma iterável (lista, tupla, set e etc)
numbers = [1, 2, 3]
print(f"função sum(): {sum(numbers)}")

# Type casting | int(), float(), str() e bool()
# Usadas para converter explicitamente uma variável de um tipo de dado para outro (ex: string para inteiro), garantindo a compatibilidade em operações e evitando erros de tipo
print(f"função int(): {int("10")}")
print(f"função float(): {float("10")}")
print(f"função str(): {str(10)}")
print(f"função bool(): {bool("")}")  # " " é sempre false

# type()
# Retorna o tipo do objeto (ex: <class 'int'>)
print(f"função type(): {type(10)}")
print(f"função type(): {type("10")}")
print(f"função type(): {type(10.5)}")
print(f"função type(): {type(True)}")

# isinstance() | params(obj, class)
# Verifica se um objeto pertence a uma classe específica. É a forma recomendada de validar tipos
print(f"função isinstance(): {isinstance(10, int)}")
print(f"função isinstance(): {isinstance(10, str)}")
print(f"função isinstance(): {isinstance(10.5, float)}")
print(f"função isinstance(): {isinstance(False, bool)}")

# range() | params(start, stop, step)
# gera uma sequência imutável de números inteiros, sendo amplamente usada em loops for para repetir tarefas um número específico de vezes
for i in range(1, 4, 1):
    print(i)





