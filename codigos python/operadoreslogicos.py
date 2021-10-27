media = float(input ("Informe a media: "))
frequencia = float(input("Informe a frequencia: "))

 if media < 5 or frequencia < 25:
    print("Reprovado")

elif media > 7 and frequencia > 75:
    print("Aprovado")

else:
    print("prova final")