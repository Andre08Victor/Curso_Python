"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 19-23.
"""

horario = input('Que horas são? ')
horario = int(horario)

if horario >= 0 and horario <= 11:
    print('Bom dia.')
elif horario >= 12 and horario <= 17:
    print('Boa tarde.')
else: 
    print('Boa noite.')