# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite outro número: ')) não recomendado fazer a conversão na mesma linha
#Input sempre é string
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
#sempre realizar a mudança da variavel apos a entrada
#Em outra linha de coditgo
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')