"""
Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor.

Características dos Dicionários:
- Mutáveis: Os dicionários podem ser alterados após a sua criação.
- Indexados por Chave: Os valores em um dicionário são acessados através de suas
chaves, não por um índice numérico como nas listas.

Quando usar Dicionários:
- Armazenamento de Dados Estruturados: Ideais para representar objetos do mundo real,
como um registro de usuário (com chaves como "nome", "email", "idade").
- Contagem de Frequência: Úteis para contar a ocorrência de itens em uma coleção.
- Mapeamento: Quando você precisa associar um valor a outro, como um dicionário
de tradução de palavras.
"""

# Criação de um dicionário
# Um dicionário é criado usando chaves {} e separando os pares de chave-valor por vírgulas.
# A chave e o valor são separados por dois pontos :.

# Exemplo: Dicionário de informações de um usuário
usuario = {
    "nome": "Alice",
    "email": "alice@example.com",
    "idade": 30,
    "cidade": "São Paulo"
}

print(f"Dicionário de usuário: {usuario}")

# Acessando valores em um dicionário
# Para acessar um valor, utilizamos a chave correspondente entre colchetes [].
nome_usuario = usuario["nome"]
idade_usuario = usuario["idade"]

print(f"Nome do usuário: {nome_usuario}")
print(f"Idade do usuário: {idade_usuario}")

# Adicionando e atualizando valores
# Para adicionar um novo par de chave-valor ou atualizar um valor existente,
# basta atribuir um valor a uma chave.

# Adicionando uma nova informação
usuario["profissao"] = "Engenheira de Software"
print(f"Dicionário após adicionar a profissão: {usuario}")

# Atualizando uma informação existente
usuario["cidade"] = "Rio de Janeiro"
print(f"Dicionário após atualizar a cidade: {usuario}")

# Removendo valores
# O método pop() remove um item com base na chave e retorna o valor removido.
# O comando del remove um item com base na chave.

# Removendo a idade usando pop()
idade_removida = usuario.pop("idade")
print(f"Idade removida: {idade_removida}")
print(f"Dicionário após remover a idade: {usuario}")

# Removendo o email usando del
del usuario["email"]
print(f"Dicionário após remover o email: {usuario}")

# Verificando a existência de uma chave
# O operador in pode ser usado para verificar se uma chave existe em um dicionário.
tem_nome = "nome" in usuario
tem_email = "email" in usuario

print(f"A chave 'nome' existe no dicionário? {tem_nome}")
print(f"A chave 'email' existe no dicionário? {tem_email}")

# Iterando sobre um dicionário
# Você pode iterar sobre as chaves, valores ou ambos.

# Iterando sobre as chaves
print("\nIterando sobre as chaves:")
for chave in usuario:
    print(f"Chave: {chave}, Valor: {usuario[chave]}")

# Iterando sobre os valores
print("\nIterando sobre os valores:")
for valor in usuario.values():
    print(f"Valor: {valor}")

# Iterando sobre os pares de chave-valor
print("\nIterando sobre os pares de chave-valor:")
for chave, valor in usuario.items():
    print(f"Chave: {chave}, Valor: {valor}")
