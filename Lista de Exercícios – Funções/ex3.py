def calcular_media_e_verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6.0:
        print(f"PARABÉNS! Você foi aprovado com média {media:.2f}")
    else:
        print(f"Infelizmente, você não foi aprovado. Sua média foi {media:.2f}")

nota1 = 7.5
nota2 = 8.0
calcular_media_e_verificar_aprovacao(nota1, nota2)
