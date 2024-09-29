"""
Crear un programa que permita a un usuario gestionar un inventario de productos.
El inventario almacenará:
    -> Nombre del producto.
    -> Cantidad disponible
    -> Precio por unidad

El usuario podrá realizar las siguientes acciones:
    -> Agregar un nuevo producto al inventario
    -> Eliminar un producto del inventario
    -> Actualizar cantidad
    -> Actualizar el precio
    -> Mostrar el inventario completo con todos los productos
    -> Calcular el valor total del inventario
    -> Buscar un producto específico por nombre
   
Requisitos:
    -> Relaizarlo bajo la programación funcional
    -> Usar una lista de listas para representar el inventario.
       Cada productos será una lista con su nombre, cantidad y precios.
    -> Implementar un menú que permita al usuario seleccionar que acción realizar
    -> Valida las entradas del usuario para asegurar que los datos sean correctos
    -> Ordenar la lista por nombre o por valor de inventario

Funcionalidades:
    -> Agregar un productos:
        -> Solicitar nombre, cantidad y precio del nuevo producto.
        -> Verificar si el producto ya existe para actualizar o agregar uno nuevo
    -> Eliminar un producto:
        -> Buscar un producto por nombre y eliminarlo si existe.
    -> Actualizar la cantidad o el precio:
        -> Permite al usuario modificar la cantidad o el precio de un producto
           existente.
    -> Mostrar inventario:
        -> Mostrar una tabla con todos los productos, cantidades y precios.
    -> Calcular el valor total del inventario:
        -> Calcular el valor total sumando el producto de la cantidad 
           por el precio de cada producto
"""

#verify if the product exist in the products list
def exist_product(inventory, name):
    if not inventory:
        return False
    elif inventory[0][0] == name:
        return True
    else:
        return exist_product(inventory[1:], name)

# Agregar un nuevo producto
def create_product(inventory, name, qti, price):
    
    