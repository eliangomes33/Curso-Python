
""" 
1. Verificador de Números Primos
Peça ao usuário um número.

Use um for para verificar se ele é divisível por algum número além de 1 e dele mesmo.

Use if/else para imprimir se é primo ou não. """

num = int(input("Digite um número: "))

eh_primo = True  


for i in range(2, num):
    if num % i == 0:
        eh_primo = False
        break  

if eh_primo and num > 1:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo.")

