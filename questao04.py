#começo pedindo um número de DDD pro usuário usando uma variável com input
ddd = int(input("Digite um DDD: "))

#faço as comparações com os números da lista usando if
if ddd == 61:
    print(f"O DDD {ddd} é da cidade de Brasília.")

#copio o código anterior e altero só alguns nomes e valores pra poupar tempo (tô fazendo essa prova no último dia. Sávio me dá uma nota boa)
elif ddd == 71:
    print(f"O DDD {ddd} é da cidade de Salvador.")

elif ddd == 11:
    print(f"O DDD {ddd} é da cidade de São Paulo.")

elif ddd == 21:
    print(f"O DDD {ddd} é da cidade do Rio de Janeiro.")

elif ddd == 32:
    print(f"O DDD {ddd} é da cidade de Juiz de Fora.")

elif ddd == 19:
    print(f"O DDD {ddd} é da cidade de Campinas.")

elif ddd == 27:
    print(f"O DDD {ddd} é da cidade de Vitória.")

elif ddd == 31:
    print(f"O DDD {ddd} é da cidade de Belo Horizonte.")

else:
    print("DDD não cadastrado.")