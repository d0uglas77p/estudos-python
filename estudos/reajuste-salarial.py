#===========================================#####=============================================================#
#Universidade de Mogi das Cruzes
#Programador: Douglas Pardim Ferreira 
#Turma: 1b ADS Noturno
#Data: 14/04/2023
#Programa: Reajuste Salárial
#===========================================#####=============================================================#

print("----------------------------- Reajuste Salárial -----------------------------")

#Usuário entrará com o salário atual
salario=float(input("Informe o salário do colaborador R$"))

#função para incrementar a % no reajuste
simbolo="%"

#Processo e saída do novo salário
if salario<1500:
    reajuste = salario*0.15
    novo_salario = salario+reajuste
    print("Novo salário do colaborador R$%.2f \nCom reajuste de 15%s" %(novo_salario, simbolo))

elif salario>=1500 and salario<=4000:
    reajuste = salario*0.10
    novo_salario = salario+reajuste
    print("Novo salário do colaborador R$%.2f \nCom reajuste de 10%s" %(novo_salario, simbolo))

else:
    reajuste = salario*0.05
    novo_salario = salario+reajuste
    print("Novo salário do colaborador R$%.2f \nCom reajuste de 0,05%s" %(novo_salario, simbolo))
    
print("----------------------------- Reajuste Salárial -----------------------------")

