"""
╔════════════════════════════════════════════════════════════════════════════╗
║           ERROS E EXCEÇÕES EM PYTHON - GUIA COMPLETO                      ║
╚════════════════════════════════════════════════════════════════════════════╝

O que são Exceções?
- Exceções são eventos que ocorrem durante a execução do programa
- Quando Python encontra um erro, ele gera uma exceção
- Se não tratada, a exceção interrompe o programa
- Podemos capturar e tratar exceções com try/except

Hierarquia de Exceções em Python:
BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception (a mais importante para tratamento)
        ├── StopIteration
        ├── ArithmeticError (ZeroDivisionError, OverflowError)
        ├── LookupError (IndexError, KeyError)
        ├── NameError
        ├── TypeError
        ├── ValueError
        ├── AttributeError
        └── ... mais de 50 tipos diferentes
"""

print("\n" + "="*80)
print("1. EXCEÇÕES MAIS COMUNS - EXEMPLOS PRÁTICOS")
print("="*80)

# ════════════════════════════════════════════════════════════════════════════
# 1. ZeroDivisionError - Divisão por zero
# ════════════════════════════════════════════════════════════════════════════
print("\n[1] ZeroDivisionError - Não é possível dividir por zero")
print("-" * 80)

try:
    # Tentativa: dividir um número por zero
    resultado = 10 / 0
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    # Captura a exceção e exibe mensagem amigável
    print("❌ ERRO: Não é permitido dividir por zero!")
    print("   Solução: Verificar se o divisor é diferente de zero antes de calcular")

# Exemplo correto com tratamento
print("\n✅ Solução segura:")
divisor = 0
if divisor != 0:
    print(f"10 / {divisor} = {10 / divisor}")
else:
    print("Divisor é zero, operação não pode ser realizada")

# ════════════════════════════════════════════════════════════════════════════
# 2. IndexError - Índice fora do intervalo
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[2] IndexError - Tentativa de acessar um índice inexistente")
print("-" * 80)

try:
    # Lista com 3 elementos (índices 0, 1, 2)
    numeros = [10, 20, 30]
    print(f"Lista: {numeros}")
    
    # Tentativa de acessar índice 5 (que não existe)
    print(f"Elemento no índice 5: {numeros[5]}")
except IndexError:
    # Captura quando a lista não tem o índice solicitado
    print("❌ ERRO: Índice não existe na lista!")
    print(f"   A lista tem apenas {len(numeros)} elementos")
    print(f"   Índices válidos: 0 a {len(numeros)-1}")

# Exemplo correto com verificação
print("\n✅ Solução segura:")
indice = 5
if 0 <= indice < len(numeros):
    print(f"Elemento no índice {indice}: {numeros[indice]}")
else:
    print(f"Índice {indice} não existe (válidos: 0 a {len(numeros)-1})")

# ════════════════════════════════════════════════════════════════════════════
# 3. KeyError - Chave inexistente em dicionário
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[3] KeyError - Tentativa de acessar uma chave inexistente em dicionário")
print("-" * 80)

try:
    # Dicionário com chaves específicas
    pessoa = {"nome": "João", "idade": 30}
    print(f"Dicionário: {pessoa}")
    
    # Tentativa de acessar chave que não existe
    print(f"Email: {pessoa['email']}")
except KeyError as e:
    # Captura e exibe qual chave não foi encontrada
    print(f"❌ ERRO: A chave {e} não existe no dicionário!")
    print(f"   Chaves disponíveis: {list(pessoa.keys())}")

# Exemplo correto com métodos seguros
print("\n✅ Soluções seguras:")
print(f"Usando .get() com padrão: {pessoa.get('email', 'Não informado')}")
print(f"Verificando 'in': {'email' in pessoa}")

# ════════════════════════════════════════════════════════════════════════════
# 4. ValueError - Valor inválido para operação
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[4] ValueError - Valor inadequado para a operação")
print("-" * 80)

try:
    # Tentativa de converter string não-numérica para inteiro
    texto = "abc"
    print(f"Convertendo '{texto}' para inteiro...")
    numero = int(texto)
except ValueError:
    # Captura quando o valor não pode ser convertido
    print(f"❌ ERRO: Não é possível converter '{texto}' para inteiro!")
    print("   ValueError ocorre quando o tipo de dados é correto, mas o valor é inválido")

# Exemplo correto com validação
print("\n✅ Solução segura:")
texto = "42"
try:
    numero = int(texto)
    print(f"'{texto}' convertido com sucesso: {numero}")
except ValueError:
    print(f"'{texto}' não é um número válido")

# ════════════════════════════════════════════════════════════════════════════
# 5. TypeError - Tipo de dados incorreto
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[5] TypeError - Operação com tipo de dados incompatível")
print("-" * 80)

try:
    # Tentativa de concatenar string com número
    resultado = "Idade: " + 30
except TypeError as e:
    # Captura quando se tenta operação entre tipos incompatíveis
    print(f"❌ ERRO: {e}")
    print("   Não é possível concatenar string com inteiro!")

# Exemplo correto com conversão
print("\n✅ Solução segura:")
idade = 30
resultado = "Idade: " + str(idade)  # Converte número para string
print(resultado)

# ════════════════════════════════════════════════════════════════════════════
# 6. NameError - Variável ou função não definida
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[6] NameError - Tentativa de usar variável/função não definida")
print("-" * 80)

try:
    # A variável 'variavel_inexistente' não foi definida
    print(variavel_inexistente)
except NameError as e:
    # Captura quando tenta usar algo que não foi definido
    print(f"❌ ERRO: {e}")
    print("   Você tentou usar uma variável que não foi definida!")

# Exemplo correto
print("\n✅ Solução segura:")
minha_variavel = "Agora estou definida!"
print(minha_variavel)

# ════════════════════════════════════════════════════════════════════════════
# 7. AttributeError - Atributo inexistente em objeto
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[7] AttributeError - Tentativa de acessar atributo inexistente")
print("-" * 80)

class Carro:
    def __init__(self):
        self.marca = "Toyota"
        self.model = "Corolla"

try:
    meu_carro = Carro()
    print(f"Marca: {meu_carro.marca}")
    print(f"Modelo: {meu_carro.modelo}")  # 'modelo' não existe, é 'model'
except AttributeError as e:
    # Captura quando tenta acessar atributo que não existe
    print(f"❌ ERRO: {e}")
    print(f"   Atributos disponíveis: {[a for a in dir(meu_carro) if not a.startswith('_')]}")

# Exemplo correto
print("\n✅ Solução segura:")
print(f"Modelo: {meu_carro.model}")
print(f"Atributos: marca={meu_carro.marca}, model={meu_carro.model}")

# ════════════════════════════════════════════════════════════════════════════
# 8. FileNotFoundError - Arquivo não encontrado
# ════════════════════════════════════════════════════════════════════════════
print("\n\n[8] FileNotFoundError - Tentativa de abrir arquivo inexistente")
print("-" * 80)

try:
    # Tentativa de abrir arquivo que não existe
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
    # Captura quando o arquivo não é encontrado
    print("❌ ERRO: Arquivo 'arquivo_inexistente.txt' não encontrado!")
    print("   Verifique se o caminho e o nome do arquivo estão corretos")

# Exemplo seguro com verificação
print("\n✅ Solução segura:")
import os
caminho = "arquivo_inexistente.txt"
if os.path.exists(caminho):
    with open(caminho, "r") as arquivo:
        conteudo = arquivo.read()
else:
    print(f"Arquivo '{caminho}' não existe neste diretório")

print("\n" + "="*80)
print("2. SINTAXE COMPLETA: try/except/else/finally")
print("="*80)

"""
try:
    # Código que pode gerar exceção
    resultado = 10 / 2
except ZeroDivisionError:
    # Executado APENAS se ZeroDivisionError ocorrer
    print("Erro: divisão por zero")
except (TypeError, ValueError):
    # Pode capturar múltiplas exceções
    print("Erro: tipo ou valor inválido")
except Exception as e:
    # Captura QUALQUER exceção (menos específico)
    print(f"Erro inesperado: {e}")
else:
    # Executado APENAS se NÃO houver exceção
    print(f"Cálculo bem-sucedido: {resultado}")
finally:
    # Sempre executado, independente se houve exceção ou não
    print("Limpeza ou finalização de recursos")
"""

print("\nExemplo prático completo:")
print("-" * 80)

def dividir(a, b):
    try:
        print(f"Tentando dividir {a} por {b}...")
        resultado = a / b
    except ZeroDivisionError:
        print("❌ Erro: divisão por zero capturada!")
        resultado = None
    except TypeError as e:
        print(f"❌ Erro de tipo: {e}")
        resultado = None
    else:
        print(f"✅ Divisão realizada com sucesso!")
    finally:
        print("➜ Bloco finally sempre é executado (limpeza de recursos)\n")
    
    return resultado

# Testando diferentes cenários
print("[Teste 1] Divisão normal:")
resultado1 = dividir(10, 2)
print(f"Resultado: {resultado1}\n")

print("[Teste 2] Divisão por zero:")
resultado2 = dividir(10, 0)
print(f"Resultado: {resultado2}\n")

print("[Teste 3] Tipos inválidos:")
resultado3 = dividir("10", 2)
print(f"Resultado: {resultado3}\n")

print("="*80)
print("3. EXCEÇÕES CUSTOMIZADAS (Criadas pelo Programador)")
print("="*80)

# Criando uma exceção customizada
class SalarioInvalidoError(Exception):
    """Exceção lançada quando o salário é inválido"""
    pass

class IdadeInvalidaError(Exception):
    """Exceção lançada quando a idade é inválida"""
    pass

class Funcionario:
    def __init__(self, nome, age, salario):
        self.nome = nome
        self.age = age
        self.salario = salario
    
    def validar(self):
        """Valida dados do funcionário e lança exceções customizadas se inválidos"""
        if self.age < 18:
            raise IdadeInvalidaError(f"Idade {self.age} é menor que 18!")
        
        if self.salario < 0:
            raise SalarioInvalidoError(f"Salário negativo: R${self.salario}")
        
        print(f"✅ Funcionário {self.nome} validado com sucesso!")

print("\n[Teste 1] Funcionário com dados válidos:")
try:
    func1 = Funcionario("Ana Silva", 28, 3500)
    func1.validar()
except IdadeInvalidaError as e:
    print(f"❌ IdadeInvalidaError: {e}")
except SalarioInvalidoError as e:
    print(f"❌ SalarioInvalidoError: {e}")

print("\n[Teste 2] Funcionário menor de idade:")
try:
    func2 = Funcionario("João", 16, 2000)
    func2.validar()
except IdadeInvalidaError as e:
    print(f"❌ IdadeInvalidaError: {e}")
except SalarioInvalidoError as e:
    print(f"❌ SalarioInvalidoError: {e}")

print("\n[Teste 3] Funcionário com salário negativo:")
try:
    func3 = Funcionario("Maria", 25, -1000)
    func3.validar()
except IdadeInvalidaError as e:
    print(f"❌ IdadeInvalidaError: {e}")
except SalarioInvalidoError as e:
    print(f"❌ SalarioInvalidoError: {e}")

print("\n" + "="*80)
print("4. BOAS PRÁTICAS NO TRATAMENTO DE EXCEÇÕES")
print("="*80)

print("""
✓ BOM - Capturar exceções específicas:
try:
    valor = int(entrada)
except ValueError:
    print("Digite um número válido")

✗ RUIM - Capturar tudo de forma genérica:
try:
    valor = int(entrada)
except:
    print("Algo deu errado")

✓ BOM - Usar mensagens informativas:
except ValueError as e:
    print(f"Erro na conversão: {e}")

✓ BOM - Usar else e finally:
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    print("Arquivo aberto com sucesso")
finally:
    arquivo.close()  # Sempre executado

✓ BOM - Criar exceções customizadas:
class DadoInvalidoError(Exception):
    pass

✓ BOM - Re-lançar exceção com context:
try:
    operacao()
except ValueError as e:
    raise DadoInvalidoError("Operação falhou") from e
""")

print("\n" + "="*80)
print("5. RESUMO DE EXCEÇÕES COMUNS")
print("="*80)

excecoes_resumo = {
    "ZeroDivisionError": "Divisão por zero",
    "IndexError": "Índice fora do intervalo de lista/tupla",
    "KeyError": "Chave não existe em dicionário",
    "ValueError": "Valor inválido para operação",
    "TypeError": "Tipo de dados incompatível",
    "NameError": "Variável ou função não definida",
    "AttributeError": "Atributo não existe em objeto",
    "FileNotFoundError": "Arquivo não encontrado",
    "IOError": "Erro na leitura/escrita de arquivo",
    "ImportError": "Módulo não encontrado",
    "RecursionError": "Limite de recursão excedido",
    "MemoryError": "Memória insuficiente",
}

print("\nExceções mais utilizadas:\n")
for excecao, descricao in excecoes_resumo.items():
    print(f"  • {excecao:<25} → {descricao}")

print("\n" + "="*80)
