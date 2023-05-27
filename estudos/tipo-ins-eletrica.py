#===========================================#####=============================================================#
#Universidade de Mogi das Cruzes
#Programador: Douglas Pardim Ferreira / Alan Carlos da Silva / Cesar Alves Caetano de Oliveira 
#RGM:11231100708 / 11231101757 / 11231101808
#Turma: 1b ADS Noturno
#Data: 14/04/2023
#Programa: Preço e tipo de instalação da energia elétrica
#===========================================#####=============================================================#

#Usuário deverá entrar com kwh e o tipo de instalação
cor='\033[1;32;41m'
fim='\033[0m'
imp=("----------- Taxa do fornecimento de energia elétrica ------------")
print(f'{cor} {imp}{fim}')

kwh=float(input("Entre com a quantidade de kWh consumida:"))
cor1='\033[1;31;40m'
fim1='\033[0m'
imp1=("-------------------------- Instalação ---------------------------")
print(f'{cor1} {imp1}{fim1}')
print("                      r - para residências")
print("                      c - para comércio")
print("                      i - para indústrias")
cor1='\033[1;31;40m'
fim1='\033[0m'
imp2=("-----------------------------------------------------------------")
print(f'{cor1} {imp2}{fim1}')

tipo_instalacao=input("Entre com o tipo de instalação:")
print("----------------------------------------------------------------")

#Processo e a saída do preço da energia elétrica
if tipo_instalacao == "r":
    if kwh <= 500:
        preco = kwh*0.40
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))
    else:
        preco = kwh*0.65
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))

elif tipo_instalacao == "c":
    if kwh <= 1000:
        preco = kwh*0.55
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))
    else:
        preco = kwh*0.60
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))

elif tipo_instalacao == "i":
    if kwh <= 5000:
        preco = kwh*0.55
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))
    else:
        preco = kwh*0.60
        print("Preço a pagar pelo fornecimento de energia elétrica: R$%.2f" %(preco))

#Saída do tipo de instalação inválida
else:
    print("Tipo de instalação inválida, tente novamente!")
print("----------------------------------------------------------------")


