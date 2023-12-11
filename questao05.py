#começo criando a lista de numeros e de pares e peço os valores usando o range pra repetir a variável com input
lista = []
pares = []
for numeros in range(0,5):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

#faço o processo de indentificação de números pares baseado na lista de números inteiros
for inteiros in lista:
     if inteiros % 2 == 0:
         pares.append(inteiros)

par = len(pares)
print(f"{par} valores pares ({pares}).")