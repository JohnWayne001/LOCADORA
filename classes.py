class Locadora:
    def __init__(self, nome, localizacao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__itens = []
        self.__clientes = []

    def cadastrarCliente(self, nome, cpf):
        self.__clientes.append(nome)

    def cadastrarItem(self, codigo, titulo):
        self.

    def listarClientes():
        pass

    def listarItem():
        pass


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

    def locar(self, item: Item):


    def devolver(Item):
        pass

    def listaritens():
        pass



class Item:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo
        disponibilidade = True

    def alugar():
        disponibilidade = False

    def devolver():
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