try:
    x = int(input("Digite o primeiro numero:"))
    y = int(input("Digite o segundo numero:"))
    total = x / y
    print(total)
except ValueError:
    print("Voce deve informar dois numeros.")

except ZeroDivisionError:
    print("Voce nao pode digitar zero no segundo numero.")

except Exception as e :
    print("Ocorreu o erro:", e)

else:
       print("Se tudo der certo,eu serei impresso.") 

finally:
    print("Isso aqui será impresso.")