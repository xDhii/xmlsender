## Mensagem de todas as telas ##
import os, sys, shutil

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mensageminicial():
    print()
    print("\033[1;30;47m        Criador de IDOC v0.3.10 (beta)        ")
    print()
    print('\33[1;37;40mEstá faltando alguma empresa ou tipo de documento?')
    print('\33[1;37;40mMe avise: adriano.valumin@sovos.com')
    print('\033[0m')
    print()
    print()