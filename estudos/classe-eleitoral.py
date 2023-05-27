#===========================================#####=============================================================#
#Universidade de Mogi das Cruzes
#Programador: Douglas Pardim Ferreira  
#Turma: 1b ADS Noturno
#Data: 07/05/2023
#Programa: Questão 4 da Prova (Classe Eleitoral)
#===========================================#####=============================================================#

import os

while True:
    
    print("\033[033m=========================\033[m \033[1;31mConsulta Eleitoral\033[m \033[033m=======================\033[m")
    try:
        idade=int(input("\033[1;36mInforme a idade:\033[m "))
        
        if idade <1 or idade >120:
            os.system('clear')
            print("\033[31mIdade inválida!\033[m")
            print("\033[033m--------------------------------------------------------------------\033[m")
        
        elif idade <16:
            os.system('clear')
            print("\033[31mNão é um eleitor!\033[m")
            print("\033[033m--------------------------------------------------------------------\033[m")
        
        elif idade >=18 and idade <=65:
            os.system('clear')
            print("\033[31mEleitor obrigatório!\033[m")
            print("\033[033m--------------------------------------------------------------------\033[m")
        
        else:
            os.system('clear')
            print("\033[31mEleitor facultativo!\033[m")
            print("\033[033m--------------------------------------------------------------------\033[m")
    except:
        os.system('clear')
        print("\033[31mIdade inválida!\033[m")
        print("\033[033m--------------------------------------------------------------------\033[m")
        
    
    saida=input("\033[1;31mEntre com\033[m \033[1;32m(F)\033[m \033[1;31mpara finalizar ou digite\033[m \033[1;32mENTER\033[m \033[1;31mpara voltar ao Menu:\033[m ")
    print("\033[033m--------------------------------------------------------------------\033[m")
    if saida in ["F","f"]:
        break
    
    else:
        os.system('clear')





