import os

lista_de_compras = []
while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_de_compras.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except: 
            print('Não foi possível apagar esse índice.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('Nada para listar.')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
    else:
        ('Por favor, escolha i, a ou l.')