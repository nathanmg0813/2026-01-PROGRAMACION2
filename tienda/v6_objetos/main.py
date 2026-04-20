from producto import Producto

# Ya puedo crear objetos con la clase producto
producto_1 = Producto()
producto_1.nombre = "zapatos"
producto_1.precio = 100

producto_2 = Producto()
producto_2.nombre = "camisa"
producto_2.precio = 300
producto_2.desciento = 50


total_de_la_compra = producto_1.precio + producto_2.precio

print(f"El total de la compra es: {total_de_la_compra}")
