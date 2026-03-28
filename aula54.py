lista_comprar = ['Feijão', 'Tomate', 'Arroz', 'Macarrão', 'Manteiga', 'Carne',
                  'Ovo']
opcao = 0

while opcao != 's':
    print(f'Selecione uma opção\t')
    opcao = input('[i]nserir [a]pagar [l]star [s]air: ')

    if opcao == 'i':
        novo_item = input('O que deseja adicionar: ')
        lista_comprar.append(novo_item )
        print("Novo item adiconado a lista: ", lista_comprar)

    elif opcao == 'a':
        print("Itens na lista atualmente: ", lista_comprar)
        apagar_item = input("Qual intem deseja remover: ")
        if apagar_item in lista_comprar:
            lista_comprar.remove(apagar_item)
            print(f"'{apagar_item}' foi removido com sucesso!")
        else:
            print(f"O item '{apagar_item}' não está na lista.")
    elif opcao  == 'l':
        print("A lista atual é: ", lista_comprar)





