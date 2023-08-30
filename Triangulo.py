a = int(input("Ingrese el primer lado del triangulo: "))
b = int(input("Ingrese el segundo lado del triangulo: "))
c = int(input("Ingrese el tercer lado del triangulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Es un triangulo equilatero.")
    elif a == b or a == c or b == c:
        print("Es un triangulo isosceles.")
    else:
        print("Es un triangulo escaleno.")
else:
    print("No es un triangulo.")

