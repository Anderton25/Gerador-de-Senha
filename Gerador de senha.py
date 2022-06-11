import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1','2','3','4','5','6','7','8','9']
simbolos = ['!', '#', '$', '%','&','(',')','*', '+']

print('Bem-Vindo ao gerador de senhas!')
n_letras = int(input('Quantas letras você quer na sua senha?\n'))
n_simbolos = int(input('Quantos simbolos você quer na sua senha?\n'))
n_numeros = int(input('Quantos números você quer na sua senha?\n'))

senha_lista = []
for sen in range(1, n_letras + 1 ):
    senha_lista.append(random.choice(letras))

for sen in range(1, n_simbolos + 1):
    senha_lista += random.choice(simbolos)

for sen in range(1 , n_numeros + 1):
    senha_lista += random.choice(numeros)

random.shuffle(senha_lista)

senha = ""
for sen in senha_lista:
    senha += sen

print(f"Sua senha é: {senha}")