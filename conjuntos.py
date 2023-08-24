#1. Crie um conjunto com os números de 1 a 10 e imprima o conjunto.
print("\n1:")
conjunto = {1,2,3,4,5,6,7,8,9,10}
print(conjunto)

#2.Crie dois conjuntos, um com os números de 1 a 5 e outro com os números de 3 a 7. Imprima a união, a interseção e a diferença simétrica dos conjuntos.
print(" \n2:")
conjunto1 = {1,2,3,4,5}
conjunto2= {3,4,5,6,7}
uniao = conjunto1.union(conjunto2)
print(uniao)

intersecao = conjunto1.intersection(conjunto2)
print(intersecao)

diferenca = conjunto1.symmetric_difference(conjunto2)
print(diferenca)

#3. Crie um conjunto com as vogais (a, e, i, o, u) e peça ao usuário para digita uma palavra. Imprima as vogais que aparecem na palavra digitada.
print("\n3:")
conjunto_vogais = {'a','e','i','o','u'}
palavra = input("Digite uma palavra : ")

for i in palavra:
    if i in conjunto_vogais:
        print(i)

#Crie dois conjuntos com nomes de frutas e verifique se há alguma fruta em comum entre os conjuntos.
print("\n4:")
conjunto_frutas1 = {'maçã','uva'}
conjunto_frutas2 = {'maçã','laranja'}

intersecao_frutas = conjunto_frutas1.intersection(conjunto_frutas2)
print(intersecao_frutas)

#Crie um conjunto com números inteiros aleatórios e imprima o maior e o menor número do conjunto.
print("\n5:")
conjuntoAleatorio = {40,22,52,71,84,6,89}

maior = 0
menor = 0

for i in conjuntoAleatorio:
    if i >= maior:
        maior = i
        menor = i

    elif i <= menor:
        menor = i

print("O maior numero é :", maior)
print("O menor numero é :", menor)

#Crie um conjunto com as cores do arco-íris (vermelho, laranja, amarelo, verde, azul, anil, violeta) e peça ao usuário para digitar uma cor. Verifique se a cor digitada está no conjunto e imprima uma mensagem correspondente.
print("\n6:")
conjuntoArcoIris = {'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta'}
cor = input("Digite uma cor:")

if cor in conjuntoArcoIris:
    print("CONJUNTO CONTÉM ESSA COR")

else:
    print("NAO CONTÉM ESSA COR")

#Crie um conjunto com os dias da semana (segunda, terça, quarta, quinta, sexta, sábado, domingo) e remova os dias úteis (segunda a sexta). Imprima o vconjunto resultante.
print("\n7:")
conjuntoDias = {'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'}
conjuntoDias.remove('segunda')
conjuntoDias.remove('terça')
conjuntoDias.remove('quarta')
conjuntoDias.remove('quinta')
conjuntoDias.remove('sexta')
print(conjuntoDias)

#Crie um conjunto com os números de 1 a 20 e outro conjunto com os números pares de 1 a 10. Imprima a diferença entre os dois conjuntos.
print("\n8:")
conjunto1a20 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
conjuntoPares = {2,4,6,8,10}

diferenca8 = conjunto1a20.difference(conjuntoPares)
print(diferenca8)

#Crie um conjunto com as notas de um aluno em uma disciplina e verifique se ele foi aprovado (média 7) ou reprovado (média abaixo de 7).
print("\n9:")

notas = {7.5, 6.5, 9.0}

media = sum(notas) / 3

if media >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Notas do aluno:", notas)
print("Média:", media)
print("Aluno foi:", situacao)

#Crie um conjunto com os números primos de 1 a 20 e verifique se um número digitado pelo usuário está no conjunto.
print("\n10:")
conjuntoPrimos = {2, 3, 5, 7, 11, 13, 17, 19}
número = int(input("Digite um número de 1 a 20: "))

if número in conjuntoPrimos:
    print(f"O número {número} está no conjunto.")
else:
    print(f"O número {número} não está no conjunto.")