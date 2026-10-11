# Generator expression, Interables e Iterators em Python
minha_lista = ["Maçã", "Banana", "Cereja"]

# Obtendo o iterator a partir da lista
meu_iterator = iter(minha_lista)

# Pegando os itens um por vez
print(next(meu_iterator))  # Saída: Maçã
print(next(meu_iterator))  # Saída: Banana
print(next(meu_iterator))  # Saída: Cereja

# Se tentarmos pegar mais um item, o iterator levanta uma exceção:
# print(next(meu_iterator))  # Gera o erro: StopIteration