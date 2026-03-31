"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                        ESTRUTURA DE DADOS: HASH TABLE                          ║
║                                                                                ║
║ Uma Hash Table (ou Tabela Hash) é uma estrutura de dados que implementa uma     ║
║ matriz associativa - uma estrutura que mapeia chaves para valores.             ║
║                                                                                ║
║ CONCEITO:                                                                      ║
║ - Usa uma HASH FUNCTION para converter uma chave em um índice de array         ║
║ - Armazena pares (chave, valor) em uma estrutura para acesso rápido           ║
║ - Tempo de acesso médio: O(1)                                                 ║
║ - Tempo no pior caso: O(n) quando há muitas colisões                          ║
║                                                                                ║
║ COLISÕES:                                                                      ║
║ - Ocorrem quando duas chaves diferentes geram o mesmo hash                     ║
║ - Solução 1: SEPARATE CHAINING - usar listas encadeadas em cada posição       ║
║ - Solução 2: OPEN ADDRESSING - encontrar outra posição disponível             ║
║                                                                                ║
║ Nesta implementação usamos SEPARATE CHAINING (lista de tuplas/listas)         ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

class HashTable:
    """
    Implementação de uma Hash Table usando Separate Chaining para resolver colisões.
    
    Cada posição do array interno contém uma lista de pares (chave, valor).
    """
    
    def __init__(self, size=10):
        """
        Inicializa a hash table.
        
        Args:
            size (int): Tamanho do array interno (número de "buckets")
        """
        # Tamanho da tabela
        self.size = size
        
        # Array com 'size' posições, cada uma iniciando como uma lista vazia
        # Estas listas armazenarão pares [chave, valor] em caso de colisão
        self.table = [[] for _ in range(size)]
        
        # Contador para rastrear número de elementos armazenados (opcional, mas útil)
        self.count = 0
    
    def _hash_function(self, key):
        """
        Função hash que converte uma chave em um índice do array.
        
        PASSO-A-PASSO:
        1. Converte a chave em string (para trabalhar com qualquer tipo)
        2. Calcula a soma dos códigos ASCII de cada caractere
        3. Aplica módulo pelo tamanho da tabela para garantir índice válido
        
        Args:
            key: A chave a ser convertida em hash
            
        Returns:
            int: Índice válido entre 0 e self.size-1
        """
        # Passo 1: Converter chave para string
        key_str = str(key)
        
        # Passo 2: Calcular soma dos valores ASCII dos caracteres
        hash_value = 0
        for char in key_str:
            hash_value += ord(char)
        
        # Passo 3: Usar módulo para obter índice dentro do tamanho
        index = hash_value % self.size
        
        return index
    
    def insert(self, key, value):
        """
        Insere um par (chave, valor) na hash table.
        
        PASSO-A-PASSO:
        1. Calcula o hash da chave para obter o índice
        2. Acessa a lista naquele índice (bucket)
        3. Verifica se a chave já existe - se sim, atualiza o valor
        4. Se não existe, adiciona novo par [chave, valor] à lista
        
        Args:
            key: Chave para armazenar
            value: Valor associado à chave
        """
        # Passo 1: Calcular índice usando a função hash
        index = self._hash_function(key)
        
        # Passo 2 e 3: Acessar a lista (bucket) e verificar se chave existe
        bucket = self.table[index]
        
        # Passo 3: Procurar pela chave na lista
        for i, (k, v) in enumerate(bucket):
            # Se a chave já existe, atualizar valor
            if k == key:
                bucket[i] = [key, value]
                print(f"  ✓ Chave '{key}' atualizada com valor '{value}' no índice {index}")
                return
        
        # Passo 4: Se não encontrou, adicionar novo par
        bucket.append([key, value])
        self.count += 1
        print(f"  ✓ Inserido '{key}': '{value}' no índice {index}")
    
    def search(self, key):
        """
        Busca um valor pela chave na hash table.
        
        PASSO-A-PASSO:
        1. Calcula o hash da chave para obter o índice
        2. Acessa a lista naquele índice (bucket)
        3. Percorre a lista procurando pela chave
        4. Se encontrar, retorna o valor; caso contrário retorna None
        
        Args:
            key: Chave a ser buscada
            
        Returns:
            O valor associado à chave, ou None se não encontrada
        """
        # Passo 1: Calcular índice
        index = self._hash_function(key)
        
        # Passo 2: Acessar a lista (bucket)
        bucket = self.table[index]
        
        # Passo 3 e 4: Procurar pela chave na lista
        for k, v in bucket:
            if k == key:
                print(f"  ✓ Encontrado '{key}': '{v}' no índice {index}")
                return v
        
        # Não encontrou
        print(f"  ✗ Chave '{key}' não encontrada")
        return None
    
    def delete(self, key):
        """
        Remove um par (chave, valor) da hash table.
        
        PASSO-A-PASSO:
        1. Calcula o hash da chave para obter o índice
        2. Acessa a lista naquele índice (bucket)
        3. Procura pela chave na lista
        4. Se encontrar, remove o par e retorna True
        5. Se não encontrar, retorna False
        
        Args:
            key: Chave a ser removida
            
        Returns:
            bool: True se removido com sucesso, False se chave não existe
        """
        # Passo 1: Calcular índice
        index = self._hash_function(key)
        
        # Passo 2: Acessar a lista (bucket)
        bucket = self.table[index]
        
        # Passo 3, 4 e 5: Procurar e remover
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                print(f"  ✓ Removido '{key}' do índice {index}")
                return True
        
        # Não encontrou
        print(f"  ✗ Chave '{key}' não existe para remover")
        return False
    
    def display(self):
        """
        Exibe o conteúdo da hash table de forma legível.
        Mostra cada índice e seus pares (chave, valor).
        """
        print("\n┌─── CONTEÚDO DA HASH TABLE ───┐")
        print(f"│ Tamanho: {self.size}, Elementos: {self.count} │")
        print("└──────────────────────────────┘")
        
        for index, bucket in enumerate(self.table):
            if bucket:  # Só mostra buckets não-vazios
                print(f"  Índice {index}: {bucket}")
            else:
                print(f"  Índice {index}: [vazio]")


# ════════════════════════════════════════════════════════════════════════════════
#                              EXEMPLOS DE USO
# ════════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    print("=" * 80)
    print("EXEMPLO 1: Criando uma Hash Table e inserindo elementos")
    print("=" * 80)
    
    # Criar uma hash table com 5 posições
    print("\n1. Criando hash table com tamanho = 5")
    ht = HashTable(size=5)
    print("   ✓ Hash Table criada")
    
    # Inserir alguns pares chave-valor
    print("\n2. Inserindo pares (chave, valor):")
    ht.insert("nome", "Alice")
    ht.insert("idade", 25)
    ht.insert("cidade", "São Paulo")
    ht.insert("profissão", "Desenvolvedora")
    ht.insert("país", "Brasil")
    
    # Exibir conteúdo da tabela
    print("\n3. Conteúdo da hash table após inserções:")
    ht.display()
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("EXEMPLO 2: Buscando elementos")
    print("=" * 80)
    
    print("\n1. Buscando valores existentes:")
    valor1 = ht.search("nome")
    valor2 = ht.search("idade")
    
    print("\n2. Tentando buscar chave que não existe:")
    valor3 = ht.search("salário")
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("EXEMPLO 3: Atualizando um valor")
    print("=" * 80)
    
    print("\n1. Atualizando o valor de 'idade' para 26:")
    ht.insert("idade", 26)
    
    print("\n2. Conteúdo após atualização:")
    ht.display()
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("EXEMPLO 4: Removendo elementos")
    print("=" * 80)
    
    print("\n1. Removendo 'profissão':")
    ht.delete("profissão")
    
    print("\n2. Tentando remover 'email' (não existe):")
    ht.delete("email")
    
    print("\n3. Conteúdo após remoções:")
    ht.display()
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("EXEMPLO 5: Demonstrando colisões")
    print("=" * 80)
    
    print("\n1. Criando nova hash table com tamanho pequeno (3) para forçar colisões:")
    ht2 = HashTable(size=3)
    
    print("\n2. Inserindo várias chaves (algumas gerarão colisões):")
    ht2.insert("apple", "maçã")
    ht2.insert("app", "aplicativo")      # Probável colisão com 'apple'
    ht2.insert("grape", "uva")
    ht2.insert("date", "data")           # Probável colisão
    ht2.insert("tar", "alcatrão")
    
    print("\n3. Conteúdo com colisões resolvidas por separate chaining:")
    ht2.display()
    
    print("\n4. Buscando em buckets com colisões:")
    ht2.search("app")
    ht2.search("date")
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("EXEMPLO 6: Caso de uso real - Dicionário de Telefones")
    print("=" * 80)
    
    print("\n1. Criando agenda de telefones:")
    agenda = HashTable(size=7)
    
    print("\n2. Adicionando contatos:")
    agenda.insert("alice", "11-99999-1111")
    agenda.insert("bob", "21-98888-2222")
    agenda.insert("carol", "31-97777-3333")
    agenda.insert("david", "41-96666-4444")
    
    print("\n3. Agora consultando telefones:")
    print(f"\nTelefone de Alice: {agenda.search('alice')}")
    print(f"Telefone de Bob: {agenda.search('bob')}")
    
    print("\n4. Atualizando telefone de Alice:")
    agenda.insert("alice", "11-99999-5555")
    print(f"Novo telefone de Alice: {agenda.search('alice')}")
    
    print("\n5. Agenda final:")
    agenda.display()
    
    # ────────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("RESUMO - COMPLEXIDADE DE TEMPO")
    print("=" * 80)
    print("""
    Operação          Tempo Médio    Pior Caso
    ─────────────────────────────────────────
    Inserção          O(1)           O(n)
    Busca             O(1)           O(n)
    Remoção           O(1)           O(n)
    
    Nota: O tempo médio é O(1) quando a Hash Table está bem distribuída.
          O pior caso O(n) ocorre quando há muitas colisões (hash ruim ou
          tabela pequena com muitos elementos).
    """)
    
    print("\n" + "=" * 80)
    print("FIM DOS EXEMPLOS")
    print("=" * 80)
