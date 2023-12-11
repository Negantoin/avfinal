#primeiro declaro a variável senha pra que haja um valor correto
senha = 2002

#peço ao usuário que digite a senha usando a variável "tentativa"
tentativa = int(input("Digite a senha: "))

#crio um sistema deloop pra que o programa continue pedindo a senha depois que o usuário erra
while tentativa != senha:
    print("Senha Inválida!")
    tentativa = int(input("Digite a senha: "))

if tentativa == senha:
    print("Acesso Permitido!")