# Exercício 1
def calcular_fatorial():
    n = int(input("Digite um número inteiro positivo: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}")

# Exercício 2
def soma_n_numeros():
    n = int(input("Digite um número inteiro: "))
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print(f"A soma dos {n} primeiros números naturais é {soma}")

# Exercício 3
def tabuada():
    n = int(input("Digite um número inteiro: "))
    print(f"Tabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Exercício 4
def contagem_regressiva():
    n = int(input("Digite um número inteiro: "))
    for i in range(n, -1, -1):
        print(i)

# Exercício 5
def maior_menor_numero():
    numeros = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

# Exercício 6
def verificar_primo():
    n = int(input("Digite um número inteiro: "))
    if n <= 1:
        print(f"{n} não é primo.")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} não é primo.")
            return
    print(f"{n} é primo.")

# Exercício 7
def fibonacci_ate_oito():
    fib = [0, 1]
    while len(fib) < 8:
        fib.append(fib[-1] + fib[-2])
    print("Sequência de Fibonacci até o oitavo número:", fib)

# Exercício 8
def inverter_lista():
    lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]
    lista.reverse()
    print("Lista invertida:", lista)

# Exercício 9
def verificar_palindromo():
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == palavra[::-1]:
        print(f"'{palavra}' é um palíndromo.")
    else:
        print(f"'{palavra}' não é um palíndromo.")

# Exercício 10
def ordenar_lista():
    lista = [int(x) for x in input("Digite números inteiros separados por espaço: ").split()]
    crescente = sorted(lista)
    decrescente = sorted(lista, reverse=True)
    print("Ordem crescente:", crescente)
    print("Ordem decrescente:", decrescente)