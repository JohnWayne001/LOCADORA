from classes import *
import os

locSenai = Locadora("Senai", "Rua dos filmes")

def cadastroCliente():
        os.system("cls")
        print("--TELA DE CADASTRO---")
        print("")
        nome = input("Qual o seu nome?\n-->")
        cpf = int(input("Qual o seu CPF?\n-->"))


def registrarItem():
    print("O que você deseja registrar?")
    registro = int(input("1 - Filme \n2 - Jogo\n-->"))
    if registro == 1:
        print("CADASTRE SEU FILME")
        codigo_filme = int(input("Qual o ID do filme?\n-->"))
        titulo_filme = input("Qual o título do filme?\n-->")
        genero_filme = input("Qual o gênero do filme?\n-->")
        duracao_filme = input("Qual a duração do filme em minutos?\n-->")

        locSenai.cadastrarItem(Filme(codigo= codigo_filme, titulo= titulo_filme, genero = genero_filme, duracao = duracao_filme))
        print("Filme cadastrado com sucesso")

    elif registro == 2:
        print("CADASTRE SEU JOGO")
        codigo_jogo = input("Qual o ID do jogo?\n-->")
        titulo_jogo = input("Qual o título do jogo?\n-->")
        plataforma_jogo = input("Qual a plataforma do jogo?\n-->")
        faixaEtaria_jogo = input("Qual a faixa etária do jogo?\n-->")
    
        Jogo(codigo= codigo_jogo, titulo= titulo_jogo, plataforma= plataforma_jogo, faixaEtaria= faixaEtaria_jogo)

        locSenai.cadastrarItem(Jogo(codigo= codigo_jogo, titulo= titulo_jogo, plataforma= plataforma_jogo, faixaEtaria= faixaEtaria_jogo))
        print("Filme cadastrado com sucesso")