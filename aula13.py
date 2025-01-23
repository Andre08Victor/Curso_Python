"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva 
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; se tiver mais que 
6 letras, escreva "Seu nome é grande".
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')
