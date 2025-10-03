entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '150123'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Logado')
else:
    print('Acesso não permitido')