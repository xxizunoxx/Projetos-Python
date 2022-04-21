#    Área do Círculo
raio = float(input())

pi = 3.14159

area = pi * raio ** 2

print(f'A={area:.4f}')

#    Códigos aleatorios
a = int(1)
b = int((a + 1) ** 3 * 3 + a)

if b <= 25:
    c = 3
else:
    c = 4
    a = 3
d = b - c + a * 2

print(f'{a} {b} {c} {d}')

#    Códigos aleatorios2
H = 3
J = 9 % 2 + H

if J < 5:
    K = 3
    L = 4
elif J < 10:
    K = 6
    L = 7
    H = 8
else:
    K = 9
    L = 10

M = H + K + L * (J - 3)

print(f'{H} {J} {K} {L} {M}')

#    Códigos aleatorios3
A = 3
B = 2 ** A
C = 2

if B <= 9:
    C = C + (3 * A)
else:
    B = 2
    C = 4 * A

D = B + C - A

print(f'{A} {B} {C} {D}')

#    Códigos aleatorios4
H = 3
J = 10 // H

if J <= 5:
    K = 3 ** H
    L = 5 - H
elif J <=10:
    K = 4 * H
    L = 8 / H
    H = 8

M = K % L + H + J

print(f'{H} {J} {K} {L} {M}')

#    Códigos aleatorios5
x = int(input('Digite um número de 1 a 10:' ))

if x <= 1 or x >=10:
    print(f'digite outro numero')

#    Códigos aleatorios6

#    Códigos aleatorios7

#    Soma Simples
A = input()
A = int(A)
B = input()
B = int(B)

soma = A + B

print(f'SOMA =', soma)

#    Média 1
A = float(input())
B = float(input())

media = (3.5*A + 7.5*B) / 11

print(f'MEDIA = {media:.5f}')

#     git add . "adiciona as alterações para subir para a nuvem"
#     git commit -m "adiciona uma descrição"
#     git push -u origin Projeto-Facul "subir repositório novo para nuvem"
#     git push "subir o repositorio para o github"

