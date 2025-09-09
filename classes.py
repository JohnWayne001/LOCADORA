class Item:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponibilidade = True

    def alugar(self):
        if self.__disponibilidade:
            disponibilidade = False

    def devolver(self):
        if not self.__disponibilidade:
            disponibilidade = True


class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao

class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

    def locar(self, item: Item):
        if self.__disponibilidade:
            self.__disponibilidade = False
        

    def devolver(self, item: Item):
        if self.__disponibilidade:
            self.__disponibilidade = True

    def listaritens(self):
        for i in self.__itensLocados:
            print(f"Livro: {i}")


class Locadora:
    def __init__(self, nome, localizacao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__itens = []
        self.__clientes = []

    def cadastrarCliente(self, clientes: Cliente):
        self.__clientes.append(clientes)

    def cadastrarItem(self, item: Item):
        self.__itens.append(item)
        self.__itens.append(Item)

    def listarClientes(self):
        for i in self.__clientes:
            print(f"Clientes: {i}")

    def listarItem(self):
        for i in self.__itens:
            print(f"Itens: {i}")