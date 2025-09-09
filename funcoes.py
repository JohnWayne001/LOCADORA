from classes import *
import os

locSenai = Locadora("Senai", "Rua dos filmes")

def cadastroCliente():
        os.system("cls")
        print("--TELA DE CADASTRO---")
        print("")
        nome = input("Qual o seu nome?\n-->")
        cpf = int(input("Qual o seu CPF?\n-->"))

def cadastrarFilme():
    print("CADASTRE SEU FILME")
    codigo = input("Qual o ID do filme?")
    titulo = input("Qual o título do filme?")
    genero = input("Qual o gênero do filme?")
    duracao = input("Qual a duração do filme em minutos?")

    locSenai.cadastrarFilme(codigo = codigo, titulo = titulo, genero = genero, duracao = duracao)
    print("Filme cadastrado com sucesso")

def cadastrarJogo():
    print("CADASTRE SEU JOGO")
    codigo = input("Qual o ID do jogo?")
    titulo = input("Qual o título do jogo?")
    plataforma = input("Qual a plataforma do jogo?")
    faixaEtaria = input("Qual a faixa etária do jogo?")
  
    locSenai.cadastrarJogo(codigo = codigo, titulo = titulo, plataforma = plataforma, faixaEtaria = faixaEtaria)
    print("Filme cadastrado com sucesso")
