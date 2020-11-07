''' Escreva uma função que recebe como parâmetro de entrada um número N positivo e exibe todos
os divisores desse número.
'''

def divisores(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


num = int(input('Informe um numero: '))
divisores(num)
