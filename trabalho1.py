corPreferida = {"Azul": 0, "Verde": 0, "Rosa": 0}
idade = 0
sexo = {"Masculino": 0, "Feminino": 0}

totalDeRespondentes = 0

idadePessoaMaisVelhaQuePrefereACor = {"Azul": 0, "Verde": 0, "Rosa": 0}

idadePessoaMaisNovaQuePrefereACor = {"Azul": 0, "Verde": 0, "Rosa": 0}

quantidadeDePessoasDoSexoMasculinoQuePrefereACor = {"Azul": 0, "Verde": 0, "Rosa": 0}

quantidadeDePessoasDoSexoFemininoQuePrefereACor = {"Azul": 0, "Verde": 0, "Rosa": 0}

quantidadeDePessoas = 0

while True:
    opcao = input("Deseja responder este formulário? (S/N): ").upper() 
    
    if opcao != "S":
        break

    quantidadeDePessoas += 1
    print(f"Respostas para a pessa {quantidadeDePessoas}:")
    cor = input("Qual é a sua cor preferida (Azul, Verde, ou Rosa)? ").capitalize()
    if cor in corPreferida:
        corPreferida[cor] += 1
        idade = int(input("Qual é a sua idade? "))
        
        if idade > idadePessoaMaisVelhaQuePrefereACor[cor]:
            idadePessoaMaisVelhaQuePrefereACor[cor] = idade
        
        if idade < idadePessoaMaisNovaQuePrefereACor[cor]:
            idadePessoaMaisNovaQuePrefereACor[cor] = idade
        genero = input ("Qual é o seu sex (Masculino/Feminino)").capitalize()
        if genero in sexo: 
            sexo[genero] += 1
        
        if genero == "Maculino":
            quantidadeDePessoasDoSexoMasculinoQuePrefereACor [cor] += 1
        else: 
            quantidadeDePessoasDoSexoFemininoQuePrefereACor [cor] += 1

totalDeRespondentes = sum(corPreferida.values())
porcentagens = {cor: (quantidade / quantidadeDePessoas * 100) for cor, quantidade in corPreferida.items()}

print("Porcentagem de Preferecia de cor:")
for cor, porcentagem in porcentagens.items():
    print (f"{cor}: {porcentagem:.2f}%")

print("Idade da pessoa mais velha que prefere cada cor:")
for cor, idade in idadePessoaMaisVelhaQuePrefereACor.items():
      print(f"{cor}: {idade} anos")
      
print("Idade da pessoa mais nova que prefere cada cor:")
for cor, idade in idadePessoaMaisNovaQuePrefereACor.items():
     print(f"{cor}: {idade} anos")

print("Quantidade de pessoas do sexo masculin que prefere cada cor:")
for cor, quantidade in quantidadeDePessoasDoSexoMasculinoQuePrefereACor.items():
    print(f"{cor}: {quantidade}")

print("Quantidade de pesoas do sexo masculino que prefere cada cor:")
for cor, quantidade in quantidadeDePessoasDoSexoFemininoQuePrefereACor.items():
    print(f"{cor}: {quantidade}")

print(f"Quantidade de pessoas que respondeu a pegunta: {quantidadeDePessoas}")