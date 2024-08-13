def eh_divisivel(x, y):
    return 1 if x % y == 0 else 0

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
resultado = eh_divisivel(x, y)
print(resultado)
