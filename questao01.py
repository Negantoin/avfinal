#primeiro eu peço o valor do salario pro usuario e faço questão de pedir que se use ponto e duas casas decimais
salario = float(input("Digite o valor do seu salário (use ponto e duas casas decimais): R$"))

#defino a condição que, se verdadeira, vai definir que o usuario está isento de impostos 
if salario <= 2000.00:
    #como nesse caso não tem taxa de imposto, só é preciso dizer isso ao usuário usando um "print"
    print("Você está ISENTO de impostos!")

#defino a segunda condição dos 8% de imposto
elif salario >= 2000.01 and salario <= 3000.00:
    #como a partir desse valor é preciso ter o valor do imposto, eu crio a variável "imposto" e descrevo o calculo de porcentagem baseado no salário
    imposto = salario * 8 /100
    #então eu mostro o valor do imposto igualzinho tá pedindo na questão (Sávio me dá uma nota boa pfvr)
    print(f"Você deve pagar R$ {imposto} de imposto!")

#pra diminuir meu trabalho eu só copio e colo o código anterior e aí só preciso mudar alguns valores
elif salario >= 3000.01 and salario <= 4500.00:
    imposto = salario * 18 /100
    print(f"Você deve pagar R$ {imposto} de imposto!")

#mesma coisa só que só precisa de uma comparação no if ao invés de duas
elif salario > 4500.00:
    imposto = salario * 28 /100
    print(f"Você deve pagar R$ {imposto} de imposto!")