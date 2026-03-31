# =============================================================================
# STACK E QUEUE - Estruturas de Dados Fundamentais
# =============================================================================
# 
# STACK (Pilha): Estrutura LIFO (Last In, First Out)
# - Último elemento adicionado é o primeiro a ser removido
# - Funciona como uma pilha de pratos: você tira o prato de cima primeiro
#
# QUEUE (Fila): Estrutura FIFO (First In, First Out)
# - Primeiro elemento adicionado é o primeiro a ser removido
# - Funciona como uma fila de supermercado: quem chega primeiro, é atendido primeiro
# =============================================================================


# =============================================================================
# 1. IMPLEMENTAÇÃO DE STACK (PILHA)
# =============================================================================

class Stack:
    """
    Classe que implementa uma pilha (Stack) usando lista.
    Operações principais:
    - push(item): adiciona um elemento no topo da pilha
    - pop(): remove e retorna o elemento do topo
    - peek(): retorna o elemento do topo sem remover
    - is_empty(): verifica se a pilha está vazia
    """
    
    def __init__(self):
        # Passo 1: Inicializar uma lista vazia para armazenar os elementos
        self.items = []
    
    def push(self, item):
        """
        Passo 2: Adiciona um elemento ao topo da pilha
        Operação: O(1) - tempo constante
        """
        self.items.append(item)
    
    def pop(self):
        """
        Passo 3: Remove e retorna o elemento do topo
        - Se a pilha estiver vazia, retorna None
        Operação: O(1) - tempo constante
        """
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """
        Passo 4: Retorna o elemento do topo SEM remover
        Operação: O(1) - tempo constante
        """
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """
        Passo 5: Verifica se a pilha está vazia
        Operação: O(1) - tempo constante
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Passo 6: Retorna o tamanho da pilha
        """
        return len(self.items)
    
    def __str__(self):
        """Representação em string da pilha"""
        return f"Stack({self.items})"


# =============================================================================
# 2. IMPLEMENTAÇÃO DE QUEUE (FILA)
# =============================================================================

class Queue:
    """
    Classe que implementa uma fila (Queue) usando lista.
    Operações principais:
    - enqueue(item): adiciona um elemento no final da fila
    - dequeue(): remove e retorna o primeiro elemento
    - peek(): retorna o primeiro elemento sem remover
    - is_empty(): verifica se a fila está vazia
    """
    
    def __init__(self):
        # Passo 1: Inicializar uma lista vazia para armazenar os elementos
        self.items = []
    
    def enqueue(self, item):
        """
        Passo 2: Adiciona um elemento no final da fila
        Operação: O(1) - tempo constante
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Passo 3: Remove e retorna o primeiro elemento da fila
        - Se a fila estiver vazia, retorna None
        Operação: O(n) - tempo linear (porque remove do início da lista)
                  Nota: Usando collections.deque seria O(1)
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """
        Passo 4: Retorna o primeiro elemento SEM remover
        Operação: O(1) - tempo constante
        """
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """
        Passo 5: Verifica se a fila está vazia
        Operação: O(1) - tempo constante
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Passo 6: Retorna o tamanho da fila
        """
        return len(self.items)
    
    def __str__(self):
        """Representação em string da fila"""
        return f"Queue({self.items})"


# =============================================================================
# 3. IMPLEMENTAÇÃO OTIMIZADA DE QUEUE USANDO collections.deque
# =============================================================================

from collections import deque

class QueueOtimizada:
    """
    Implementação mais eficiente de fila usando collections.deque.
    deque permite operações O(1) em ambas as pontas.
    """
    
    def __init__(self):
        # Passo 1: Usar deque para melhor performance
        self.items = deque()
    
    def enqueue(self, item):
        """Adiciona elemento no final - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove elemento do início - O(1) (diferente de lista que é O(n))"""
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def peek(self):
        """Retorna primeiro elemento - O(1)"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Verifica se está vazia - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Retorna tamanho - O(1)"""
        return len(self.items)


# =============================================================================
# EXEMPLOS DE USO - STACK
# =============================================================================

print("\n" + "="*70)
print("EXEMPLOS DE STACK (PILHA) - LIFO")
print("="*70)

# Exemplo 1: Stack básico
print("\n--- Exemplo 1: Operações básicas de Stack ---")
stack = Stack()

# Adicionando elementos (push)
print("Adicionando elementos: 10, 20, 30, 40")
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(f"Stack após push: {stack}")

# Verificando o topo (peek)
print(f"Elemento no topo (peek): {stack.peek()}")
print(f"Tamanho da stack: {stack.size()}")

# Removendo elementos (pop)
print("\nRemovendo elementos (pop):")
print(f"Pop 1: {stack.pop()} → {stack}")
print(f"Pop 2: {stack.pop()} → {stack}")
print(f"Pop 3: {stack.pop()} → {stack}")


# Exemplo 2: Verificar parênteses balanceados usando Stack
print("\n--- Exemplo 2: Verificar parênteses balanceados ---")

def verificar_parenteses_balanceados(expressao):
    """
    Usa Stack para verificar se uma expressão tem parênteses balanceados.
    Passo a passo:
    1. Para cada '(', adicionamos à pilha
    2. Para cada ')', removemos da pilha
    3. Se a pilha estiver vazia ao encontrar ')', está desbalanceado
    4. Se a pilha não estiver vazia ao final, está desbalanceado
    """
    stack = Stack()
    
    for char in expressao:
        if char == '(':
            stack.push(char)
            print(f"  '{char}' → Stack: {stack.items}")
        elif char == ')':
            if stack.is_empty():
                print(f"  '{char}' → ERRO: ')' sem '(' correspondente!")
                return False
            stack.pop()
            print(f"  '{char}' → Stack: {stack.items}")
    
    if not stack.is_empty():
        print(f"ERRO: Faltam ')' para fechar os '('")
        return False
    
    return True

# Testando expressões
expressoes = ["(())", "(()", "())"]
for expr in expressoes:
    print(f"\nVerificando: {expr}")
    resultado = verificar_parenteses_balanceados(expr)
    print(f"Resultado: {'✓ Balanceado' if resultado else '✗ Desbalanceado'}")


# Exemplo 3: Converter número decimal para binário usando Stack
print("\n--- Exemplo 3: Converter decimal para binário ---")

def decimal_para_binario(numero):
    """
    Usa Stack para converter um número decimal para binário.
    Passo a passo:
    1. Dividir o número por 2 e guardar o resto na pilha
    2. Repetir até o número ser 0
    3. Retirar elementos da pilha (ordem inversa = número binário)
    """
    stack = Stack()
    
    print(f"Convertendo {numero} para binário:")
    temp = numero
    
    while temp > 0:
        resto = temp % 2
        stack.push(resto)
        print(f"  {temp} ÷ 2 = {temp // 2} resto {resto} → Stack: {stack.items}")
        temp = temp // 2
    
    binario = ""
    while not stack.is_empty():
        binario += str(stack.pop())
    
    return binario

numero = 13
resultado = decimal_para_binario(numero)
print(f"Resultado: {numero} em binário é {resultado}")


# =============================================================================
# EXEMPLOS DE USO - QUEUE
# =============================================================================

print("\n\n" + "="*70)
print("EXEMPLOS DE QUEUE (FILA) - FIFO")
print("="*70)

# Exemplo 1: Queue básica
print("\n--- Exemplo 1: Operações básicas de Queue ---")
queue = Queue()

# Adicionando elementos (enqueue)
print("Adicionando elementos: 100, 200, 300, 400")
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
print(f"Queue após enqueue: {queue}")

# Verificando o primeiro (peek)
print(f"Primeiro elemento (peek): {queue.peek()}")
print(f"Tamanho da queue: {queue.size()}")

# Removendo elementos (dequeue)
print("\nRemovendo elementos (dequeue):")
print(f"Dequeue 1: {queue.dequeue()} → {queue}")
print(f"Dequeue 2: {queue.dequeue()} → {queue}")
print(f"Dequeue 3: {queue.dequeue()} → {queue}")


# Exemplo 2: Simulação de fila de atendimento
print("\n--- Exemplo 2: Simulação de fila de atendimento ao cliente ---")

class ClienteFila:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def __repr__(self):
        return f"Cliente {self.id}: {self.nome}"

# Criando fila de clientes
fila_atendimento = Queue()

# Adicionando clientes
clientes = [
    ClienteFila(1, "João"),
    ClienteFila(2, "Maria"),
    ClienteFila(3, "Pedro"),
    ClienteFila(4, "Ana")
]

print("Clientes chegando na fila:")
for cliente in clientes:
    fila_atendimento.enqueue(cliente)
    print(f"  {cliente} entrou na fila → Total: {fila_atendimento.size()}")

# Atendendo clientes
print("\nAtendendo clientes:")
while not fila_atendimento.is_empty():
    cliente = fila_atendimento.dequeue()
    print(f"  Atendendo {cliente} → Fila: {fila_atendimento.size()} cliente(s) aguardando")


# Exemplo 3: Simulação de impressora com fila de documentos
print("\n--- Exemplo 3: Fila de impressão ---")

class DocumentoImpressao:
    def __init__(self, id, nome, paginas):
        self.id = id
        self.nome = nome
        self.paginas = paginas
    
    def __repr__(self):
        return f"Doc {self.id}: {self.nome} ({self.paginas}pgs)"

# Criando fila de impressão
fila_impressao = QueueOtimizada()

# Adicionando documentos
documentos = [
    DocumentoImpressao(1, "Relatório.pdf", 5),
    DocumentoImpressao(2, "Planilha.xlsx", 3),
    DocumentoImpressao(3, "Apresentação.pptx", 10),
    DocumentoImpressao(4, "Contrato.docx", 2)
]

print("Documentos na fila de impressão:")
for doc in documentos:
    fila_impressao.enqueue(doc)
    print(f"  {doc} adicionado → Total: {fila_impressao.size()}")

# Imprimindo documentos
print("\nImprimindo documentos:")
paginas_totais = 0
while not fila_impressao.is_empty():
    doc = fila_impressao.dequeue()
    paginas_totais += doc.paginas
    print(f"  Imprimindo {doc} → Fila: {fila_impressao.size()}")

print(f"Total de páginas impressas: {paginas_totais}")


# Exemplo 4: Comparar performance de Queue vs QueueOtimizada
print("\n--- Exemplo 4: Comparação de performance ---")
import time

print("Adicionando 10.000 elementos e removendo todos:")

# Queue tradicional
queue_tradicional = Queue()
start = time.time()
for i in range(10000):
    queue_tradicional.enqueue(i)
for i in range(10000):
    queue_tradicional.dequeue()
tempo_tradicional = time.time() - start

# Queue otimizada (deque)
queue_otimizada = QueueOtimizada()
start = time.time()
for i in range(10000):
    queue_otimizada.enqueue(i)
for i in range(10000):
    queue_otimizada.dequeue()
tempo_otimizado = time.time() - start

print(f"Queue (lista):              {tempo_tradicional:.6f} segundos")
print(f"QueueOtimizada (deque):     {tempo_otimizado:.6f} segundos")
print(f"Melhoria: {tempo_tradicional/tempo_otimizado:.2f}x mais rápido!")


# =============================================================================
# RESUMO E COMPARAÇÃO
# =============================================================================

print("\n\n" + "="*70)
print("RESUMO: STACK vs QUEUE")
print("="*70)

print("""
╔════════════════════════════════════════════════════════════════════╗
║                         STACK (PILHA)                              ║
╠════════════════════════════════════════════════════════════════════╣
║ Ordem:          LIFO (Last In, First Out)                          ║
║ Operações:      push(), pop(), peek(), is_empty()                  ║
║ Complexidade:   O(1) para todas operações                          ║
║ Casos de uso:   - Desfazer/Refazer (Undo/Redo)                    ║
║                 - Verificar parênteses balanceados                 ║
║                 - Navegação em browsers (histórico)                ║
║                 - Conversão de bases numéricas                     ║
║                 - Avaliar expressões matemáticas                   ║
║                 - Backtracking em algoritmos                       ║
╚════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════╗
║                        QUEUE (FILA)                                ║
╠════════════════════════════════════════════════════════════════════╣
║ Ordem:          FIFO (First In, First Out)                         ║
║ Operações:      enqueue(), dequeue(), peek(), is_empty()           ║
║ Complexidade:   O(1) com deque, O(n) com lista                     ║
║ Casos de uso:   - Filas de atendimento ao cliente                  ║
║                 - Fila de impressão                                ║
║                 - Processamento de requisições                     ║
║                 - BFS (Busca em largura)                           ║
║                 - Agendamento de tarefas                           ║
║                 - Buffer de dados                                  ║
╚════════════════════════════════════════════════════════════════════╝

DICA: Use collections.deque para implementar Queue em produção!
""")

print("\n" + "="*70)
print("FIM DOS EXEMPLOS")
print("="*70)
