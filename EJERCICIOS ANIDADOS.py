##crea un programa
def contador(contar):
   # contar=0
    def incrementa():
        nonlocal contar
        contar= contar+1
        return contar
    return incrementa

mi_cuenta=contador(1)
print(mi_cuenta())
print(mi_cuenta())


"""ejericio: escribir una funcion que calcule el total de una factura tras aplicarle el IVA
la funcion debe recibir la cantidad sin Iva y el porcentaje de Iva a aplicar
y devolver el toral de la factura. Si se invoca la funcion sin pasarle el porcentaje
de Iva, debera aplicar un 21%
"""
def total_fact(cantidad, porcentaje=21):
     return cantidad+ (cantidad*porcentaje)/100
cantidad=0
cantidad = float(input("ingresa la cantidad: "))
iva=int(input("ingresa la cantidad sin IVA del producto a comprar:"))
iva =0
iva=int(input("ingrese el vslo del iva: ")   )
print(f"el tortal de la factura es:{total_fact(cantidad,iva)}")
