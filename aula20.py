valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ') 

valor1 = int(valor_1)
valor2 = int(valor_2)#Se estiver como strig ele não identificar como número inteiro, mas como texto dando erro

if valor1 > valor2:
    print(f'O primeiro valor {valor1} é maior que o segundo valor {valor2}')
elif valor2 > valor1:
    print(f'O Segundo valor {valor2} é maior que o primeiro valor {valor1}')
else:
    print(f'Os valores {valor2} e {valor2} são iguais')
