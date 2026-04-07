'''
Aplicación para tienda
Version: v5

Que incluye:
    - Se resuelven los BUGS 3 y 4, validando que los valores sean numéricos

Qué problemas tiene esta versión (v5): BUGS

'''

continuar_llevando_productos = True
valor_total_compra = 0
i = 0
#El ciclo whilee se utiliza cuando NO se sabe cuantas veces se va a repetir
while continuar_llevando_productos == True:
    print(f"----------------- Ingrese los datos del producto {i + 1}:  -----------------")

    el_nombre_tiene_error = True
    while el_nombre_tiene_error == True:
        print("Ingrese el nombre del producto que va a comprar: ")
        nombre_del_producto = input()
        if nombre_del_producto == "": #Solución al BUG número 1
            print("ERROR: El nombre del producto no puede ser vacio")
        else:
            if len(nombre_del_producto) > 20: #Solución al BUG número 10
                print("ERROR: El nombre del producto no puede tener más de 20 caracteres")
            else:
                el_nombre_tiene_error = False
    #output
    error_con_precio_del_producto = True
    while error_con_precio_del_producto == True:
        print("Ingrese el precio del producto que va a comprar: ")
        precio_del_producto = input()
        if precio_del_producto == "": #Solución al BUG número 2
            print("ERROR: El precio del producto no puede ser vacío")
        else:
            try:
                precio_del_producto = float(precio_del_producto)
                if precio_del_producto < 0: #Solución al BUG número 5
                    print("ERROR: El precio del producto no puede ser negativo")
                else:
                    error_con_precio_del_producto = False
            except:
                print("ERROR: Para el precio del producto por favor ingrese sólo números")


    #output
    print("Ingrese el valor del descuento del producto: ")
    #input + variable
    descuento = input()
    if descuento == "": #Solución al BUG número 6
        descuento = "0"

    descuento = float(descuento)

    if descuento < 0: #Solucíon al BUG número 7
        print("ERROR: El descuento no puede ser un valor negativo")
    else:
        if precio_del_producto < descuento: #Solución al BUG número 8
            print("ERROR: El descuento no puede superar el valor del producto")
        else:
            precio_final_del_producto = precio_del_producto - descuento

            #output
            print(f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")
            valor_total_compra = valor_total_compra + precio_final_del_producto
            i = i + 1
            print("Desea llevar otro producto? s/n: ")
            desea_llevar_otro_producto = input()
            
            if(desea_llevar_otro_producto != "s" and desea_llevar_otro_producto != "n"):
                print("Solo puede ingresar las opciones s o n")
            else:
                if desea_llevar_otro_producto == "n":
                    continuar_llevando_productos = False

print(f"El valor total de la compra es: {valor_total_compra}")
print("Gracias por su compra")