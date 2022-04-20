#    AC1 questão 1
merc_v = float(input())
merc_q = int(input())
total = merc_v * merc_q
desc_1 = total * 0.10 + total * merc_q/100
total_final = total - desc_1

print(f'{total:.2f}')
print(f'{total_final:.2f}')

#    AC1 questão 2
a = int(input())
b = int(input())
c = int(input())
tempo_gasto = a + b + c

print(f'{tempo_gasto} minutos')

#    AC1 questão 3
polegada = float(input())
cm = 2.54
tamanho = polegada * cm

print(f'{tamanho:.3f}')

#    AC1 questão 4
x = int(input())
par_mais = x + 2
par_menos = x - 1
impar_mais = x + 1
impar_menos = x - 2

if (x%2) == 0:
    print(f'{par_menos} {par_mais}')
elif (x%2) == 1:
    print(f'{impar_menos} {impar_mais}')

#    AC1 questão 5
nota_trab = float(input())
nota_prov = float(input())
media = nota_trab + nota_prov
nota_sub = int(7)
media_final = media / 2
media_sub = nota_trab + nota_sub / 2

if media_final >= 6:
    print('aprovado')
elif media_sub >= 6:
    print('talvez com a sub')
elif media_final < 6:
    print('reprovado')

#    AC1 questão 6
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


#    teste 123