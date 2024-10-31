print("'ax²+bx+c' Şeklindeki 2.Dereceden 1 Bilinmeyemli Denlkem İçin;\n")


a = float(input("a değerini girin:\n"))
b = float(input("b değerini girin:\n"))
c = float(input("c değerini girin:\n"))

d=float(((b**2)-(4*a*c))**0.5)
x1=float((-b+d)/(2*a))
x2=float((-b-d)/(2*a))

print("Hesaplanıyor...\n")
print("x₁ = '{}'\nx₂ = '{}'\n".format(x1,x2))
print("Hesaplandi\n")