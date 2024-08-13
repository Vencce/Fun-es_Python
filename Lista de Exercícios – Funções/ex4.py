def peso_ideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso = (72.7 * altura) - 58
    return peso

altura = 1.75
sexo = 2
resultado_peso_ideal = peso_ideal(altura, sexo)
print(f"O peso ideal é: {resultado_peso_ideal:.2f} kg")
