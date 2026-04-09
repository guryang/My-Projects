print("Welcome to the system to calculate the average! ")

def notas(n1, n2):
    media = (n1+n2)/2
    
    if media > 8:
        print(media)
        return "Você passou"
    else:
        print(media)
        return "Reprovado! "
        
a = input("Informe a nota 1: ")
b = input("Informe a nota 2: ")

result = notas(float(a), float(b))

print(result)

