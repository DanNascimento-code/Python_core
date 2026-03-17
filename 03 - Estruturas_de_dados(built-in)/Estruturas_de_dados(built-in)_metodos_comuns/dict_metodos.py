"""
Este arquivo demonstra os métodos mais comuns utilizados com dicionários em Python.
"""

# Dicionário de exemplo
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

print(f"Dicionário original: {carro}
")

# Método keys()
# Retorna uma visão de todas as chaves do dicionário.
chaves = carro.keys()
print(f"Método keys(): {chaves}")

# Método values()
# Retorna uma visão de todos os valores do dicionário.
valores = carro.values()
print(f"Método values(): {valores}")

# Método items()
# Retorna uma visão de todos os pares de chave-valor como tuplas.
itens = carro.items()
print(f"Método items(): {itens}
")

# Método get(chave, valor_padrao)
# Retorna o valor para a chave especificada. Se a chave não for encontrada,
# retorna o valor_padrao (ou None, se não for fornecido).
modelo_carro = carro.get("modelo")
cor_carro = carro.get("cor", "Não especificada")
print(f"Método get('modelo'): {modelo_carro}")
print(f"Método get('cor', 'Não especificada'): {cor_carro}
")

# Método pop(chave, valor_padrao)
# Remove a chave especificada e retorna o valor correspondente. Se a chave não for
# encontrada, retorna o valor_padrao (se fornecido), caso contrário, levanta um erro.
ano_removido = carro.pop("ano")
print(f"Valor removido com pop('ano'): {ano_removido}")
print(f"Dicionário após pop('ano'): {carro}
")

# Método popitem()
# Remove e retorna o último par de chave-valor inserido no dicionário (a partir do Python 3.7).
# Em versões anteriores, remove um par de forma arbitrária.
ultimo_item = carro.popitem()
print(f"Último item removido com popitem(): {ultimo_item}")
print(f"Dicionário após popitem(): {carro}
")

# Método update(outro_dicionario)
# Atualiza o dicionário com os pares de chave-valor de outro dicionário ou de um
# iterável de pares de chave-valor.
carro.update({"marca": "Chevrolet", "modelo": "Camaro", "ano": 2022})
print(f"Dicionário após update(): {carro}
")

# Método clear()
# Remove todos os itens do dicionário, deixando-o vazio.
carro.clear()
print(f"Dicionário após clear(): {carro}
")

# Método fromkeys(sequencia, valor)
# Cria um novo dicionário a partir de uma sequência de chaves, com todas as chaves
# tendo o mesmo valor especificado.
chaves_novo_carro = ["marca", "modelo", "ano"]
novo_carro = dict.fromkeys(chaves_novo_carro, "Não definido")
print(f"Novo dicionário criado com fromkeys(): {novo_carro}")

