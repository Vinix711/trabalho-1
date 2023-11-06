respostas = {"Ótimo": 0, "Bom": 0, "Regular": 0, "Péssimo": 0}
idades = []
idadesRespostas = []
respondentes = []

while True:
    idade = int(input("Idade do respondente (ou digite -1 para encerrar): "))
    if idade == -1:
        break
    resposta = input("Avaliação do atendimento (Ótimo, Bom, Regular, Péssimo): ").strip().capitalize()

    if resposta in respostas:
        respostas[resposta] += 1
    idades.append(idade)
    idadesRespostas.append((idade, resposta))
    respondentes.append((len(respondentes) + 1, idade, resposta))

if len(respondentes) > 0:
   
    idadesRespostas.sort() 
    respondenteMaisNovo = idadesRespostas[0]
    respondenteMaisVelho = idadesRespostas[-1]


    mediaIdade = sum(idades) / len(respondentes)

    print(f"Total de respondentes: {len(respondentes)}")
    for resposta, quantidade in respostas.items():
        print(f"{resposta}: {quantidade} ({(quantidade / len(respondentes) * 100):.2f}%)")
    print(f"Média de idade dos respondentes: {mediaIdade:.2f} anos")
    print(f"O respondente mais velho possuía a idade: {respondenteMaisVelho[0]} anos e sua resposta foi: {respondenteMaisVelho[1]}")
    print(f"O respondente mais novo possuía a idade: {respondenteMaisNovo[0]} anos e sua resposta foi: {respondenteMaisNovo[1]}")

    print("\nLista de Respondentes:")
    for respondente in respondentes:
        print(f"Respondente {respondente[0]} - Idade: {respondente[1]} anos, Avaliação: {respondente[2]}")
else:
    print("Nenhum respondente registrado.")
