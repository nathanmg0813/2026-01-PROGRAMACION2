''' 
Aplicacion para tienda
Version: v2

Que incluye_
   - Decisiones, validaciones

Que problemas tiene esta version (v2): BUGS
  1. 
   '''

#output
print("Ingrese el nombre del pruducto que va a comprar: ")
#input + variable
nombre_del_producto = input()
if nombre_del_producto == "": #Solucion al BUG Numero 1
    print("ERROR: El nombre del producto no puede ser vacio")
else:
   #output
   print("Ingrese el precio del producto que va a comprar: ")
   #input + variable
   precio_del_producto = input()
   if precio_del_producto == "": #Solucion al BUG numero 2
       print("ERROR: El precio del producto no puede ser vacio")
   else: 
      precio_del_producto = float(precio_del_producto)
      if precio_del_producto < 0: #Solucion al BUG numero 5
         print("ERROR: El precio del producto no puede ser negativo") 
      else:
         #output
         print ("Ingrese el descuento del producto: ")
         #input + varible
         descuento = input()
         if descuento == "": #Solucion al BUG numero 6
            descuento = "0"

         descuento = float(descuento)
         if descuento < 0: #Solucion al BUG numero 7
            print("ERROR: El descuento no puede ser un valor negativo")
         else: 
            if precio_del_producto < descuento: #Solucion al BUG numero 8
               print("ERROR: El descuento no puede superar el valor del producto")
            else:
               precio_final_del_producto = precio_del_producto - descuento

               #output
               print(f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")
