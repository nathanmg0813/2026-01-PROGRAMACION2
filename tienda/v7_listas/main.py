from typing import List
from producto import Producto

lista_productos: list[Producto] = []


def main():
    pr1 = Producto()
    pr1.nombre = "zapatos"
    pr1.precio = 10
    lista_productos.append(pr1)

    pr2 = Producto()
    pr2.nombre = "aceite"
    pr2.precio = 20
    lista_productos.append(pr2)
    
    pr3 = Producto()
    pr3.nombre = "atun"
    pr3.precio = 30
    lista_productos.append(pr3)

    total_venta = 0
    for producto in lista_productos:
        total_venta = total_venta + producto.precio

    print(f"El total de la venta es: {total_venta}")
    
if __name__ == "__main__":
    main()
