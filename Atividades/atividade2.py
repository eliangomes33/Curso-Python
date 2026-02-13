""" 2. Menu Interativo com While
Crie um menu que mostre opções:

Somar dois números

Subtrair dois números

Sair

Use while para manter o programa rodando até o usuário escolher sair.

Use if/elif/else para tratar cada opção. """
selecionar = ''
while selecionar != 'E':
    selecionar = input('Selecione o que deseja realizar abaixo:\n'
    'A=Adição, S=Subtração, M=Mutiplicação D=Divisão e E=Sair\n')
    if selecionar == 'A':
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o primeiro número: '))

        resultado = num_1 + num_2
        print(resultado) 

    if selecionar == 'S':
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o primeiro número: '))

        resultado = num_1 - num_2
        print(resultado) 
    if selecionar == 'M':
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o primeiro número: '))

        resultado = num_1 * num_2
        print(resultado) 
    if selecionar == 'D':
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o primeiro número: '))

        resultado = num_1 / num_2
        print(resultado) 
    if selecionar == 'E':
        break