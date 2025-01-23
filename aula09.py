nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# Verificando se os campos estão vazios
if nome and idade:
    ...
else: 
    print('Desculpe, você deixou campos vazios.')

print(f'Seu nome é {nome}.')
print(f'Seu nome ao contrário é {nome[::-1]}.')

if " " in nome:
    print('Seu nome contém espaços.')
else:
    print('Seu nome não contém espaços.')
        
print(f'Seu nome tem {len(nome)} letras.')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A última letra do seu nome é {nome[-1]}')
