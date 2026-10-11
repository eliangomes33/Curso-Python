# dir, hasattr e getattr em python

string = 'Elian'
metodo = 'upper'

print(string)

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo,', metodo)