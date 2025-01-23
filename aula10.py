numero_str = input('Vou dobrar o número que você digitar')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é igual a {numero_float * 2:0f}')
except:
    print('Isso não é um número.')