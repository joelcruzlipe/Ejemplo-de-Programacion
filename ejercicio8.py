def cel(f):
    c=round(((f-32)*5)/9,2)
    return c

def kel(f):
    k=round(((f-32)*5)/9+273.15,2)
    return k

f=int(input("Grados en Fahrenheit : "))

print("Equivalente Celsius = {}".format(cel(f)))
print("Equivalente Kelvin = {}".format(kel(f)))
