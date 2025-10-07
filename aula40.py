""" Calculadora com while """
while True:
    print('Sua calculadora em python')
    try:
        Digite_primeiro_número = input("Digite o primeiro número: ")
        Digite_segundo_número = input("Digite o segundo número: ")
        operação = input("Qual operação deseja realizar [+] [-] [x] [/]: ")

        
        Digite_primeiro_número_float = float(Digite_primeiro_número)
        Digite_segundo_número_float = float(Digite_segundo_número)

        if operação == '+':
            resultado = Digite_primeiro_número_float + Digite_segundo_número_float
            print(resultado)
        elif operação == '-':
            resultado = Digite_primeiro_número_float - Digite_segundo_número_float
            print(resultado)
        elif operação == 'x':
            resultado = Digite_primeiro_número_float * Digite_segundo_número_float
            print(resultado)
        elif operação == '/':
            resultado = Digite_primeiro_número_float / Digite_segundo_número_float
            print(resultado)
    except:
        print("Erro")
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break