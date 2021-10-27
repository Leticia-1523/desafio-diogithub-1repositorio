def somar(n1, n2):
    return n1 + n2

try:
    x = int(input("Digite um numero:"))
    y = int(input("Digite um numero:"))
    total = somar(x,y)
    print(total)
except Exception as e:
    print("Ocorreu o erro:", e)
