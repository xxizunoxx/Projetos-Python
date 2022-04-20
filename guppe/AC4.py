x = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
dia_s = str(input())
qtd_d = int(input())

if qtd_d == 0:
    print(f'chega hoje!')
else:
    n_lista = x.index(dia_s)
    x1 = x[n_lista:len(x)] + x[0:n_lista]
    entrega = x1[qtd_d]
    if entrega == dia_s:
        print('chega hoje')
    else:
        print(f'sera entregue {entrega}')