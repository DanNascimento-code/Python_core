

# 1. Criação de uma Classe
# A sintaxe básica para criar uma classe:
class MinhaClasse:
    """
    Esta é uma classe de exemplo que demonstra os conceitos básicos.
    """
    
    # Método construtor (__init__): chamado quando um objeto é criado
    def __init__(self, atributo_instancia):
        """
        O método __init__ inicializa os atributos de uma instância.
        'self' refere-se à instância atual do objeto.
        """
        # Atributo de instância: específico para cada instância
        self.atributo_instancia = atributo_instancia
        print(f"Objeto criado com atributo: {self.atributo_instancia}")

    # Método de instância: opera em uma instância específica (self)
    def metodo_de_instancia(self):
        """
        Este método pode acessar e modificar atributos da instância.
        """
        return f"Método de instância chamado. Atributo: {self.atributo_instancia}"

    

# 2. Instanciação (Criação de Objetos)
# Para criar um objeto (instância) de uma classe, você a chama como uma função:
print("--- Instanciação ---")
objeto1 = MinhaClasse("Valor 1")
objeto2 = MinhaClasse("Valor 2")

# 3. Acesso a Atributos e Métodos
print("\n--- Acesso a Atributos e Métodos ---")
# Acessando atributos de instância (diferentes para cada objeto)
print(f"Atributo de objeto1: {objeto1.atributo_instancia}")
print(f"Atributo de objeto2: {objeto2.atributo_instancia}")


# Chamando métodos
print(objeto1.metodo_de_instancia())
print(MinhaClasse.metodo_de_classe())
print(MinhaClasse.metodo_estatico())

# 4. Herança
# A herança permite que uma classe (filha) herde atributos e métodos de outra (pai).
print("\n--- Herança ---")

class Animal:
    """Classe base para animais."""
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "O animal faz um som genérico."

class Cachorro(Animal):
    """Classe filha que herda de Animal."""
    def fazer_som(self):
        # Polimorfismo: o método fazer_som é sobrescrito
        return "O cachorro late!"

class Gato(Animal):
    """Outra classe filha que herda de Animal."""
    def fazer_som(self):
        # Polimorfismo: o método fazer_som também é sobrescrito aqui
        return "O gato mia!"

# Instanciando as classes
animal_generico = Animal("animal")
rex = Cachorro("Rex")
felix = Gato("Felix")

print(f"{animal_generico.nome}: {animal_generico.fazer_som()}")
print(f"{rex.nome}: {rex.fazer_som()}")
print(f"{felix.nome}: {felix.fazer_som()}")


# 5. Polimorfismo
# Polimorfismo significa "muitas formas". Em POO, refere-se à capacidade de
# diferentes classes responderem à mesma mensagem (chamada de método) de maneiras diferentes.
# No exemplo acima, tanto Cachorro quanto Gato têm um método fazer_som, mas
# o comportamento é diferente para cada um.

print("\n--- Polimorfismo ---")
# Uma função pode interagir com qualquer objeto que siga uma interface comum.
def interagir_com_animal(animal):
    """Esta função demonstra o polimorfismo."""
    print(f"Interagindo com {animal.nome}: {animal.fazer_som()}")

interagir_com_animal(rex)
interagir_com_animal(felix)

# 6. Encapsulamento
# É o conceito de agrupar dados (atributos) e os métodos que os manipulam
# em uma única unidade (a classe). Também envolve restringir o acesso direto
# aos atributos, geralmente usando "getters" e "setters".

# Em Python, a convenção para um atributo "privado" é usar um sublinhado (_).
# Para um atributo "fortemente privado", usam-se dois sublinhados (__).
print("\n--- Encapsulamento ---")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade # Atributo "privado"

    def get_idade(self):
        """Método getter para a idade."""
        return self.__idade

    def set_idade(self, nova_idade):
        """Método setter para a idade com validação."""
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida!")

pessoa = Pessoa("Ana", 30)
print(f"Nome: {pessoa.nome}")
# print(pessoa.__idade) # Isso daria um AttributeError
print(f"Idade (via getter): {pessoa.get_idade()}")

pessoa.set_idade(31)
print(f"Nova idade: {pessoa.get_idade()}")

pessoa.set_idade(-5) # Tentativa de definir idade inválida

# 7. Herança Múltipla
# Python suporta herança de múltiplas classes.
print("\n--- Herança Múltipla ---")
class Pai:
    def metodo_pai(self):
        return "Método da classe Pai"

class Mae:
    def metodo_mae(self):
        return "Método da classe Mãe"

class Filho(Pai, Mae):
    pass # A classe Filho herda de Pai e Mae

filho = Filho()
print(filho.metodo_pai())
print(filho.metodo_mae())

# Python usa o MRO (Method Resolution Order) para determinar a ordem de busca
# de métodos em hierarquias complexas. Você pode ver o MRO com o atributo __mro__.
print(f"MRO da classe Filho: {Filho.__mro__}")
