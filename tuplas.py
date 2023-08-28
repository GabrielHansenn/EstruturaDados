#1. Crie uma tupla com os números de 1 a 5 e imprima a tupla.
print("\n1:")
tupla = (1,2,3,4,5)
print(tupla)


#2. Crie uma tupla com os nomes de três países e imprima o segundo elemento da tupla.
print("\n2:")
tupla2 = ('Brasil','Estados Unidos','Russia')
print(tupla2[1])
#3. Crie uma tupla com os valores de uma conta de restaurante (valor da refeição, taxa de serviço e valor total). Imprima a tupla.
print("\n3:")
valorRefeicao = 40.00
taxaServico = 5.00
valorTotal = 45.00

tupla3 = (valorRefeicao, taxaServico, valorTotal)
print("Valor da refeição:", tupla3[0],"reais")
print("Taxa de serviço:", tupla3[1],"reais")
print("Valor total:", tupla3[2],"reais")



#4. Crie uma tupla com os nomes de cinco pessoas e peça ao usuário para digitar um número entre 1 e 5. Imprima o nome correspondente ao número digitado.
print("\n4:")
tupla4 = ('Gabriel','Arthur','Matheus','Julio','André')
numero_digitado = int(input("Digite um número entre 1 e 5: "))

if 1 <= numero_digitado <= 5:
    nome_correspondente = tupla4[numero_digitado - 1]
    print("O nome correspondente ao número digitado é:", nome_correspondente)
else:
    print("Número fora do intervalo válido.")

#5. Crie uma tupla com as notas de um aluno em uma disciplina e imprima a média das notas.
print("\n5:")
notas = (7.5, 6.5, 9.0)
media = sum(notas) / 3
print("A média do aluno foi :", media)
#6. Crie uma tupla com as cores do arco-íris (vermelho, laranja, amarelo, verde,azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor digitada está na tupla e imprima uma mensagem correspondente.
print("\n6:")
arcoIris = ('vermelho','laranja', 'amarelo', 'verde','azul', 'anil', 'violeta')
cor = input("Digite uma cor:")

if cor in arcoIris:
    print("CONJUNTO CONTÉM ESSA COR")

else:
    print("NAO CONTÉM ESSA COR")


#7. Crie uma tupla com as temperaturas de uma semana (sete dias) e imprima a temperatura máxima e mínima da semana.
print("\n7:")
temperaturaSemanal = (31,29,30,28,32,27,25)

temperatura_maxima = max(temperaturaSemanal)
temperatura_minima = min(temperaturaSemanal)

print("Temperatura máxima da semana:", temperatura_maxima)
print("Temperatura mínima da semana:", temperatura_minima)

#8. Crie uma tupla com os nomes de cinco frutas e suas respectivas cores.Imprima o nome de cada fruta seguido de sua cor.
print("\n8:")
frutas_cores = (("Maçã","Vermelha"), ("Laranja","Laranja"), ("Banana","Amarela"), ("Kiwi","Verde"), ("Abacate","Verde"))
for fruta, cor in frutas_cores:
    print(fruta, ":", cor)

#9. Crie uma tupla com os números de 1 a 10 e outra tupla com os números de 5 a 15. Imprima a interseção entre as duas tuplas.
print("\n9:")
tupla1a10 = (1,2,3,4,5,6,7,8,9,10)
tupla5a15 = (5,6,7,8,9,10,11,12,13,14,15)

conjunto1 = set(tupla1a10)
conjunto2 = set(tupla5a15)

intersecao = conjunto1.intersection(conjunto2)
print(intersecao)


#10. Crie uma tupla com as letras do alfabeto e uma segunda tupla com as vogais. Imprima a diferença entre as duas tuplas.
print("\n10:")
alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
vogais = ('a','e','i','o','u')

conjuntoAlfabeto = set(alfabeto)
conjuntoVogais = set(vogais)

diferenca = conjuntoAlfabeto.difference(conjuntoVogais)
print(diferenca)