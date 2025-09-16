from classes import *
from funcoes import *
import os

while True:
    print("BEM VINDO A LOCADORA")
    print("Selecione a opção que deseja")
    opcao = int(input("1 - Cadastrar cliente \n2 - Cadastrar item \n3 - Listar filmes \n4 - Listar jogos \n0 - Sair do menu\n--> "))
    
    match opcao:
        case 1:
            cadastroCliente()
        case 2:
            registrarItem()
        case 3:
            listar_filmes()
        case 4:
            listar_jogos()
        case 5:
            listar_clientes()
        case 0:
            print("Saindo...")
            break