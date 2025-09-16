from classes import *
import os

locSenai = Locadora()

def cadastroCliente():
        os.system("cls")
        print("===TELA DE CADASTRO===")
        print("")
        nome = input("Qual o seu nome?\n-->")
        cpf = int(input("Qual o seu CPF?\n-->"))
        locSenai.cadastrarCliente(Cliente(nome= nome, cpf= cpf))


def registrarItem():
    print("O que você deseja registrar?")
    registro = int(input("1 - Filme \n2 - Jogo\n-->"))
    if registro == 1:
        print("===CADASTRE SEU FILME===")
        id_filme = len(locSenai.listarItens()) + 1
        titulo_filme = input("Qual o título do filme?\n-->")
        genero_filme = input("Qual o gênero do filme?\n-->")
        duracao_filme = input("Qual a duração do filme em minutos?\n-->")
        

        locSenai.cadastrarItem(Filme(id= id_filme, titulo= titulo_filme, genero = genero_filme, duracao = duracao_filme))
        print("Filme cadastrado com sucesso")

    elif registro == 2:
        print("CADASTRE SEU JOGO")
        id_jogo = len(locSenai.listarItens()) + 1
        titulo_jogo = input("Qual o título do jogo?\n-->")
        plataforma_jogo = input("Qual a plataforma do jogo?\n-->")
        faixaEtaria_jogo = input("Qual a faixa etária do jogo?\n-->")

        locSenai.cadastrarItem(Jogo(id= id_jogo, titulo= titulo_jogo, plataforma= plataforma_jogo, faixaEtaria= faixaEtaria_jogo))
        print("Jogo cadastrado com sucesso")



def listar_filmes():
    try:
        print("=== LISTA DE FILMES ===")
        itens = locSenai.listarItens()
        filmes = False

        if not itens:
            print("Não há nenhum filme cadastrado!")
            return
        
        for item in itens:
            if item.isDisponivel():
                status = "Disponível"
            
            else:
                status = "Alugado"
            
            print(f"{item.getId()} - Filme: {item.getTitulo()}| Gênero: {item.getGenero()}| Duração: {item.getDuracao()}min| {status}")
            filmes = True

    except Exception as e:
        print(f"Houve um erro {e}")

        if not filmes:
            print("Não há nenhum filme cadastrado!")
    
def listar_jogos():
    try:
        print("=== LISTA DE JOGOS ===")
        itens = locSenai.listarItens()
        jogos_existem = False

        if not itens:
            print("Não há nenhum jogo cadastrado!")
            return

        for item in itens:
            try:
                if item.isDisponivel():
                    status = "Disponível"
                else:
                    status = "Alugado"

                print(f"{item.getId()} - Jogo: {item.getTitulo()} | Plataforma: {item.getPlataforma()} | Faixa Etária: {item.getFaixaEtaria()}+ | {status}")
                jogos_existem = True
            except AttributeError:
                continue  

        if not jogos_existem:
            print("Não há nenhum jogo cadastrado!")

    except Exception as e:
        print(f"Houve um erro {e}")



def listar_clientes():
    try:
        print("=== LISTA DE CLIENTES ===")
        clientes = locSenai.listarClientes()

        if not clientes:
            print("Nenhum cliente cadastrado")
        
        for cliente in clientes:
            print(f"Nome: {cliente.getNome()}| CPF: {cliente.getCpf()}")

    except Exception as e:
        print(f"Houve um erro {e} :(")