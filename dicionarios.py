#1. Crie um dicionário vazio e adicione duas chaves e valores a ele.
print("\n1:")
dicionarioVazio = {}
dicionarioVazio['Nome'] = 'Gabriel'
dicionarioVazio['Idade'] = '18'
print(dicionarioVazio)

#2. Crie um dicionário com as chaves &quot;nome&quot;, &quot;idade&quot; e &quot;cidade&quot; e preencha com seus dados. Imprima o dicionário.
print("\n2:")
meu_dicionario1 = {'nome':'Gabriel','Idade':18,'cidade':'Guarapuava'}
print(meu_dicionario1)

#3. Crie um dicionário com o nome e o preço de três produtos diferentes. Imprima o dicionário.
print("\n3:")
meu_dicionario2 = {'ARROZ':10,'FEIJÃO':8,'CARNE':25}
print(meu_dicionario2)

#4. Crie um dicionário com o nome de três estados e suas respectivas capitais. Peça ao usuário para digitar um estado e imprima a capital correspondente.
print("\n4:")
meu_dicionario3 = {'São Paulo':'SP','Rio de Janeiro':'RJ','Paraná':'Curitiba'}
estado_digitado = input("Digite o nome de um estado: ")
capital = meu_dicionario3.get(estado_digitado)
if capital:
    print(f"A capital do estado de {estado_digitado} é {capital}.")
else:
    print("Estado não encontrado no dicionário.")


#5. Crie um dicionário com o nome de cinco cidades e suas respectivas populações. Imprima a cidade com a maior população.
print("\n5:")
meu_dicionario4 = {'GUARAPUAVA': 182644, 'CURITIBA': 1773733, 'LONDRINA': 575377, 'TURVO': 13095, 'PINHÃO': 32559}

maior = 0

for cidade, populacao in meu_dicionario4.items():
    if populacao > maior:
        maior = populacao
        cidade_maior_populacao = cidade

print("A cidade com maior população é:", cidade_maior_populacao, "com", maior, "habitantes.")

#6. Crie um dicionário com o nome de três alimentos e suas respectivas calorias. Peça ao usuário para digitar um alimento e imprima a quantidade de calorias correspondente.
print("\n6:")

meu_dicionario5 = {'Chocolate': 598, 'Manteiga': 590, 'Leite': 452}
alimento = input("Digite o nome de um alimento: ")

if alimento in meu_dicionario5:
    calorias = meu_dicionario5[alimento]
    print(f"O alimento {alimento} tem {calorias} calorias.")
else:
    print("Alimento não encontrado no dicionário.")

#7. Crie um dicionário com o nome de cinco animais e suas respectivas classificações (mamífero, ave, réptil, etc.). Imprima apenas os nomes dos animais.
print("\n7:")
meu_dicionario6 = {"cachorro": "mamífero", "gato": "mamífero", "gavião": "ave", "jacaré": "réptil",  "sapo": "anfíbio"}
for animal in meu_dicionario6.keys():
    print(animal)


#8. Crie um dicionário com o nome de cinco países e suas respectivas bandeiras. Imprima apenas os nomes dos países.
print("\n8:")
meu_dicionario7 = {"Brasil": "bandeira", "Estados Unidos": "bandeira", "Venezuela": "bandeira", "Canadá": "bandeira",  "México": "bandeira"}
for pais in meu_dicionario7.keys():
    print(pais)

#9. Crie um dicionário com o nome de cinco frutas e suas respectivas cores. Imprima o nome de cada fruta seguido de sua cor.
print("\n9:")
meu_dicionario8 = {"Maçã": "Vermelha", "Laranja": "Laranja", "Banana": "Amarela", "Kiwi": "Verde",  "Abacate": "Verde"}
for fruta,cor in meu_dicionario8.items():
    print(fruta,cor)

#10. Crie um dicionário com o nome de três jogos e a quantidade de jogadores necessária. Peça ao usuário para digitar um jogo e imprima a quantidade de jogadores correspondente.
print("\n10:")
meu_dicionario10 = {'Futebol':'22','Basquete':'10','Volei':'12'}
esporte_digitado = input("Digite o nome de um esporte: ")
jogadoresNumero = meu_dicionario10.get(esporte_digitado)
if jogadoresNumero:
    print(f"O numero de jogadores que precisa para jogar {esporte_digitado} é {jogadoresNumero}.")
else:
    print("Estado não encontrado no dicionário.")

