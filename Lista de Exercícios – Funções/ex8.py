def imprimir_dia(numero):
    dias = {
        1: "DOM", 2: "SEG", 3: "TER", 4: "QUA",
        5: "QUI", 6: "SEX", 7: "SAB"
    }
    if numero in dias:
        print(dias[numero])
    else:
        print("Número inválido")

numero = int(input("Digite um número de 1 a 7: "))
imprimir_dia(numero)
