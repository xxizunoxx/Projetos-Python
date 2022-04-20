x,y = map(int, input().split())
resto = max(x,y) % min(x,y)

if resto == 0:
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')