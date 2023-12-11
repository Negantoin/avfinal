#primeiro eu peço o valor do salario
salario = float(input("Digite o seu salário: R$"))

#começo a definir as condições como descrito na questão
if salario >= 0 and salario <= 400:
    #declaro a variável da porcentagem que vai servir pros futuros cálculos e também pra mostrar o reajuste
    porcentagem = salario * 15 /100
    #declaro a variável do novo salário que vale o valor do salário somado com o valor do reajuste
    salariofinal = salario + porcentagem
    print(f"Seu novo salário é: R${salariofinal} \nO reajuste foi de: R${porcentagem} \nO percentual é de: 15%")

#copio e colo o bloco de código anterior que é o padrão do programa e só precisa trocar os valores
elif salario >= 400.01 and salario <= 800:
    porcentagem = salario * 12 /100
    salariofinal = salario + porcentagem
    print(f"Seu novo salário é: R${salariofinal} \nO reajuste foi de: R${porcentagem} \nO percentual é de: 12%")