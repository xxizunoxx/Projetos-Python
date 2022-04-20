valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

pi = 3.14159 #    valor de PI
tri = (a * c) / 2 #    calculo da area do
cir = pi * c ** 2 #    calculo da area do
trap = ((a + b) * c) / 2 #    calculo da area do
quad = b ** 2 #    calculo da area do
ret = a * b  #    calculo da area do

print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')