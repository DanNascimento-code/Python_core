
# Uma lista é uma sequência indexada e ordenada de elementos mutáveis

numbers = [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 17, 19]
print(numbers)

# Listas podem guardar qualquer tipo de dados (inclusive objetos complexos):

data = [10, "hello", True, 3,14]
print(data)

"""
Exemplo de uma lista de objetos complexos:

data2 = [user_object, database_connection, file_handler]

"""

# ÍNDICES NEGATIVOS

"""
Python permite acessar uma lista de trás para frente:
index:   -4  -3  -2  -1
value:   10  20  30  40

"""

print(f"índice negativo: {numbers[-1]}")


# INTERAÇÃO

for number in numbers:
    print(number)


# Iterando com índice

# Às vezes precisamos da posição/index
for i in range(len(numbers)):
    print(i, numbers[i])


# PRINCIPAIS MÉTODS DE LISTAS    

# append() - Adiciona um elemento no final da lista
print(f"metodo append(): {numbers.append(4)}")

# extend() - Adiciona múltiplos elementos de outra coleção (append adiciona 1 objeto
#extend adiciona vários elementos)
print(f"metodo extend(): {numbers.extend([3, 4, 5])}")

# insert - Insere elemento em posição específica
print(f"metodo insert(): {numbers.insert(1, 99)}")

# remove() - Remove o primeiro valor encontrado
print(f"metodo remove(): {numbers.remove(2)}")

# pop() - Remove pelo índice e retorna o valor removido
print(f"metodo pop(): {numbers.pop(2)}")

# clear() - Remove todos os elementos da lista
print(f"metodo clear(): {numbers.clear()}")

# index() - Retorna o índice do elemento
numbers = [1, 2, 2, 3, 4, 7, 9, 11, 12, 12, 13, 14, 17, 19]
print(f"metodo index(): {numbers.index(4)}")

# count() - Conta quantas vezes aparece
print(f"metodo count{numbers.count(12)}")

# sort() - Ordena a lista
numbers = [11, 2, 3, 6, 4]
print(f"metodo sort: {numbers.sort()}")

# reverse() - Inverte a ordem
print(f"metodo reverse: {numbers.reverse()}")

# copy() - Cria uma cópia da lista
new_list = numbers.copy()
print(f"metodo copy(): {new_list}")



# SLICING (FATIAMENTO DE LISTAS) - lista[inicio:fim:passo]

# slicing básico
numbers = [10, 20, 30, 40, 50]
numbers[1:4]  # resultado: [20, 30, 40]

# início omitido
numbers[:3]  # resultado: [10, 20, 30]

# fim omitido
numbers[2:]  # resultado: [30, 40, 50]

# copiar lista
copy_numbers = numbers[:]  # Isso é muito usado para evitar modificar a lista original.

# passo (step)
numbers[0:5:2]   # [10, 30, 50]

# inverter lista
numbers[::-1]   # [50, 40, 30, 20, 10]


# LIST COMPREHENSION - [expressão for elemento in iterável]
n_squared = [n*n for n in numbers]   # resultado: [1,4,9,16]

x_multiplied = [x*2 for x in (1, 2, 3)]  # resultado [2,4,6]

# com if:
evens = [n for n in numbers if n % 2 == 0]   # resultado [2,4]





