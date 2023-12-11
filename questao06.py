#começo criando as listas e pedindo os valores
lista = []
positivos = []
for i in range(0,6):
    valor = int(input("Digite um valor: "))
    #adiciono os valores a lista principal
    lista.append(valor)

#identifico e transfiro os valores positivos pra lista de positivos
for valores in lista:
    if valores > -1:
        positivos.append(valores)
    
#uso a função "len" novamente para mostrar a quantidade de números positivos no final do programa
quantidade = len(positivos)

#faço o processo de divisão e obtenção da média dos números positivos
media = (sum(positivos))/quantidade

#mostro o resultado final
print(f"{quantidade} valores positivos{positivos}.")
print(f"A média dos números positivos é: {media}")