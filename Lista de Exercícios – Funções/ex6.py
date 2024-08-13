def soma_intervalo(n1, n2):
    return sum(range(n1, n2 + 1))

n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))

resultado = soma_intervalo(n1, n2)
print(f"A soma dos números inteiros no intervalo [{n1}, {n2}] é: {resultado}")
