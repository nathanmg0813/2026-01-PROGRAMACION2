''' 
Aplicacion para tienda
Version: v1

Que incluye_
 - Variables
    - Input
    - Output
    - Tipos de variables:
      - Sting (str)_ cadenas de texto o de caracteres. Ejemplo "hola", "precio es 50", "10"
      - Numericas entero (int): 5, 100. 134, -1234
      - Numericas float (float): 70.5, 83.1235
      - Boolean (bool): True o False
      - Objeto: Tipos personalizados
    - Operadores
     - +: suma
     - -: resta
     - * multiplicacion
     - / division

Que problemas tiene esta version (v1): BUGS
   1.  No valida que el nombre del producto NO sea vacio: Se resuelve en la v2
   2.  No valida que el precio del producto NO sea vacio: Se resuelve en la v2
   3.  No se valida que el precio del producto NO sea numerico* (No se resuelve en la version 2, sino en una version que contenga "Manejo de errores")
   4.  No se valida que el descuento del producto NO sea numerico* (No se resuelve en la version 2, sino en una version que contenga "Manejo de errores")
   5.  No se valida que el precio del producto sea positivo v2
   6.  Si el descuento es vacio, no se debe aplicar descuento
   7.  No se valida que el descuento del producto sea positivo v2
   8.  No se valida que el precio del producto sea menor o igual que el descuento del producto. Es decir, el descuento no puede superar el valor del producto v2

   

   '''

#output
print("Ingrese el nombre del pruducto que va a comprar: ")
#input + variable
nombre_del_producto = input()

#output
print("Ingrese el precio del producto que va a comprar: ")
#input + variable
precio_del_producto = input()
precio_del_producto = float(precio_del_producto)

#output
print ("Ingrese el descuento del producto: ")
#input + varible
descuento = input()
descuento = float(descuento)

precio_final_del_producto = precio_del_producto - descuento

#output
print(f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")
