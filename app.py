from classes import *
from funcoes import *
import os

while True:
    print("BEM VINDO A LOCADORA")
    print("Selecione a opção que deseja")
    opcao = int(input("1 - Cadastrar cliente \n2 - Cadastrar item\n-->"))
    
    if opcao == 1:
        cadastroCliente()
    elif opcao == 2:
        registrarItem()