# Sets (conjuntos) em Python

# 1. O que é um set?
# Um set é uma coleção desordenada de elementos únicos e imutáveis.
# "Desordenada" significa que os itens não têm uma ordem definida.
# "Únicos" significa que não pode haver elementos duplicados.
# "Imutáveis" refere-se aos próprios elementos; o set em si é mutável (podemos adicionar/remover itens).

# Criando um set:
# Usando chaves {}
meu_set = {1, 2, 3, 4, 5}
print(f"Set inicial: {meu_set}")
print(f"Tipo da variável 'meu_set': {type(meu_set)}")

# Tentando adicionar elementos duplicados (serão ignorados)
set_com_duplicatas = {1, 2, 2, 3, 3, 3, 4}
print(f"Set criado com elementos duplicados: {set_com_duplicatas}")

# Criando um set a partir de uma lista (útil para remover duplicatas)
lista = [10, 20, 20, 30, 30, 30]
set_a_partir_de_lista = set(lista)
print(f"Lista original: {lista}")
print(f"Set criado a partir da lista (remove duplicatas): {set_a_partir_de_lista}")

# Criando um set vazio (ATENÇÃO: {} cria um dicionário vazio)
set_vazio = set()
print(f"Criando um set vazio: {set_vazio}")
print("-" * 30)


# 2. Adicionando elementos
# .add(): Adiciona um único elemento ao set. Se o elemento já existir, nada acontece.
print("### Adicionando Elementos ###")
meu_set.add(6)
print(f"Set após adicionar o 6: {meu_set}")
meu_set.add(1) # Tentando adicionar um elemento que já existe
print(f"Set após tentar adicionar o 1 novamente: {meu_set}")
print("-" * 30)

# .update(): Adiciona múltiplos elementos de um iterável (lista, tupla, outro set).
meu_set.update([7, 8, 9])
print(f"Set após usar update com a lista [7, 8, 9]: {meu_set}")

meu_set.update({9, 10, 11}) # Usando outro set (o 9 já existe)
print(f"Set após usar update com o set {{9, 10, 11}}: {meu_set}")
print("-" * 30)


# 3. Removendo elementos
print("### Removendo Elementos ###")
# .remove(): Remove um elemento. Gera um erro (KeyError) se o elemento não existir.
meu_set.remove(11)
print(f"Set após remover o 11 com '.remove()': {meu_set}")
# meu_set.remove(99) # Esta linha geraria um erro: KeyError: 99

# .discard(): Remove um elemento. Não gera erro se o elemento não existir.
meu_set.discard(10)
print(f"Set após remover o 10 com '.discard()': {meu_set}")
meu_set.discard(99) # Não existe, mas não gera erro
print(f"Set após tentar remover o 99 com '.discard()': {meu_set}")

# .pop(): Remove e retorna um elemento arbitrário (aleatório) do set.
# Gera um erro se o set estiver vazio.
elemento_removido = meu_set.pop()
print(f"Elemento removido com '.pop()': {elemento_removido}")
print(f"Set após o '.pop()': {meu_set}")

# .clear(): Remove todos os elementos do set.
meu_set.clear()
print(f"Set após '.clear()': {meu_set}")
print("-" * 30)


# 4. Operações de Conjuntos
print("### Operações de Conjuntos ###")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}\n")

# União: Todos os elementos que estão em A, ou em B, ou em ambos.
# Operador |
uniao_operador = set_a | set_b
print(f"União (A | B): {uniao_operador}")
# Método .union()
uniao_metodo = set_a.union(set_b)
print(f"União (A.union(B)): {uniao_metodo}\n")

# Interseção: Elementos que estão presentes em ambos os conjuntos.
# Operador &
intersecao_operador = set_a & set_b
print(f"Interseção (A & B): {intersecao_operador}")
# Método .intersection()
intersecao_metodo = set_a.intersection(set_b)
print(f"Interseção (A.intersection(B)): {intersecao_metodo}\n")

# Diferença: Elementos que estão em A, mas não estão em B.
# Operador -
diferenca_operador = set_a - set_b
print(f"Diferença (A - B): {diferenca_operador}")
# Método .difference()
diferenca_metodo = set_a.difference(set_b)
print(f"Diferença (A.difference(B)): {diferenca_metodo}\n")

# Diferença Simétrica: Elementos que estão em A ou em B, mas não em ambos.
# Operador ^
simetrica_operador = set_a ^ set_b
print(f"Diferença Simétrica (A ^ B): {simetrica_operador}")
# Método .symmetric_difference()
simetrica_metodo = set_a.symmetric_difference(set_b)
print(f"Diferença Simétrica (A.symmetric_difference(B)): {simetrica_metodo}")
print("-" * 30)


# 5. Outros Métodos Úteis
print("### Outros Métodos Úteis ###")
set_c = {1, 2, 3, 4, 5, 6}
set_d = {1, 2, 3}
set_e = {7, 8, 9}
print(f"Set C: {set_c}")
print(f"Set D: {set_d}")
print(f"Set E: {set_e}\n")

# .issubset(): Verifica se um set é um subconjunto de outro.
# Todo elemento de D está em C?
print(f"D é subconjunto de C? (D.issubset(C)): {set_d.issubset(set_c)}") # True
print(f"C é subconjunto de D? (C.issubset(D)): {set_c.issubset(set_d)}") # False
print()

# .issuperset(): Verifica se um set contém outro set.
# C contém todos os elementos de D?
print(f"C é superconjunto de D? (C.issuperset(D)): {set_c.issuperset(set_d)}") # True
print(f"D é superconjunto de C? (D.issuperset(C)): {set_d.issuperset(set_c)}") # False
print()

# .isdisjoint(): Verifica se dois sets não têm nenhum elemento em comum.
# C e D têm elementos em comum?
print(f"C e D são disjuntos? (C.isdisjoint(D)): {set_c.isdisjoint(set_d)}") # False
# D e E têm elementos em comum?
print(f"D e E são disjuntos? (D.isdisjoint(E)): {set_e.isdisjoint(set_d)}") # True
print("-" * 30)

# .copy(): Retorna uma cópia rasa (shallow copy) do set.
set_original = {10, 20, 30}
set_copia = set_original.copy()
set_copia.add(40)
print(f"Set Original: {set_original}")
print(f"Set Cópia (modificado): {set_copia}")
print("-" * 30)


# 6. Percorrendo um Set
print("### Percorrendo um Set ###")
set_frutas = {"maçã", "banana", "cereja"}
for fruta in set_frutas:
    print(f"Fruta: {fruta}")
print("-" * 30)

# Exemplo prático: Encontrar letras únicas em uma palavra
palavra = "abracadabra"
letras_unicas = set(palavra)
print(f"A palavra '{palavra}' tem as seguintes letras únicas: {letras_unicas}")
print(f"Número de letras únicas: {len(letras_unicas)}")
