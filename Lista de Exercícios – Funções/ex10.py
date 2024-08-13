def maior_valor(a, b):
    return a if a > b else b

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
resultado = maior_valor(a, b)
print(f"O maior valor é: {resultado}")
