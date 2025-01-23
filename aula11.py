"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é impar ou par. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
numero_inteiro = numero.isdigit() 

if numero_inteiro == False:
    print('O número digitado não é inteiro.')
else: 
    numero = int(numero)
    if (numero % 2) == 0:
        print(f'O número {numero} é um número par.')
    else:
        print(f'O número {numero} é um  número ímpar.')
        