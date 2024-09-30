
#Crear un programa que permita a un usuario gestionar un inventario de productos.
#El inventario almacenará:
#    -> Nombre del producto.
#    -> Cantidad disponible
#    -> Precio por unidad
#
#El usuario podrá realizar las siguientes acciones:
#    -> Agregar un nuevo producto al inventario
#    -> Eliminar un producto del inventario
#    -> Actualizar cantidad
#    -> Actualizar el precio
#    -> Mostrar el inventario completo con todos los productos
#    -> Calcular el valor total del inventario
#    -> Buscar un producto específico por nombre
#   
#Requisitos:
#    -> Relaizarlo bajo la programación funcional
#    -> Usar una lista de listas para representar el inventario.
#       Cada productos será una lista con su nombre, cantidad y precios.
#    -> Implementar un menú que permita al usuario seleccionar que acción realizar
#    -> Valida las entradas del usuario para asegurar que los datos sean correctos
#    -> Ordenar la lista por nombre o por valor de inventario
#
#Funcionalidades:
#    -> Agregar un productos:
#        -> Solicitar nombre, cantidad y precio del nuevo producto.
#        -> Verificar si el producto ya existe para actualizar o agregar uno nuevo
#    -> Eliminar un producto:
#        -> Buscar un producto por nombre y eliminarlo si existe.
#    -> Actualizar la cantidad o el precio:
#        -> Permite al usuario modificar la cantidad o el precio de un producto
#           existente.
#    -> Mostrar inventario:
#        -> Mostrar una tabla con todos los productos, cantidades y precios.
#    -> Calcular el valor total del inventario:
#        -> Calcular el valor total sumando el producto de la cantidad 
#           por el precio de cada producto


# verify if the product exist in the products list
#from re import search


def exist_product(inventory, name):
    if not inventory:
        return False
    elif inventory[0][0] == name:
        return True
    else:
        return exist_product(inventory[1:], name)

# Adding a new product
def create_product(inventory, name, qti, price):
    if not inventory:
        return [[name,qti,price]]
    elif inventory[0][0] == name:
        return [name, inventory[0][1] + qti, price if price != inventory[0][2] else inventory[0][2]] + inventory[1:0]
    else:
        return [inventory[0] + create_product(inventory[1:],name,qti,price)]
    
def delete_product(inventory, name):
    if not inventory:
        return []
    elif inventory[0][0] == name:
        return delete_product(inventory[1:],name)
    else:
        return [inventory[0]] + delete_product(inventory[1:], name)

def update_quantity(inventory, name, new_cantity):
    if not inventory:
        return []
    elif inventory[0][0] == name:
        return [name, new_cantity, inventory[0][2]] + inventory[1:]
    else:
        return [inventory[0]] + update_quantity(inventory[1:], name, new_cantity)
    
def update_price(inventory, name, new_price):
    if not inventory:
        return []
    elif inventory[0][0] == name:
        return [name, inventory[0][1], new_price] + inventory[1:]
    else:
        return [inventory[0]] + update_price(inventory[1:], name, new_price)
   
def show_items(inventory):
    def show_products(_list_):
        if not _list_:
            return
        else:
            print(f"{_list_[0]}\t{_list_[1]}\t\t{_list_[2]}")
            show_products(_list_[1:])
    print("Nombre \t Cantidad \t Precio")
    show_products(inventory)
    
def total_value(inventory):
    if not inventory:
        return 0
    else:
        return (inventory[1] * inventory[2]) + total_value(inventory[1:])

def search_product(inventory, name):
    if not inventory:
        return None
    elif inventory[0][0] == name:
        return inventory[0]
    else:
        return search_product(inventory[1:], name)

def request_integer(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("Entrada invalida. Ingrese un numero entero.")
        return request_integer(msg)
    
def request_float(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("Entrada invalida. por favor, ingrese un decimal")
        return request_float(msg)


def process_option(inventory, option):
    if option == "1":        
        return continuar(create_product(inventory, str(input("Nombre: ")), request_integer("Cantidad: "), request_float("Precio: ")))
    elif option == "2":
        return continuar(delete_product(inventory,input("Nombre:")))
    elif option == "3":
        return update_quantity(inventory,input("Nombre"), request_integer("Cantidad: "), request_float("Precio: "))
    elif option == "4":
        return update_price(inventory, input("Nombre"), request_float("Nuevo precio: "))
    elif option == "5":
        show_items(inventory)
        return continuar(inventory)
    elif option == "6":
        print(f"Valor total del inventario: {total_value(inventory)}")
        return continuar(inventory)
    elif option == "7":
        return search_product(inventory,input("Nombre: "))
    elif option == "8":
        print("Saliendo del programa.")
        return


def menu(inventory, opcion):
    if opcion not in map(str, range(1, 9)):
        print("Opcion invalida. Intente de nuevo.")
        return menu(inventory, input("Seleccione una opcion: "))
    return process_option(inventory, opcion)

def continuar(inventario):
    print("\n--- Menu de opciones ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Mostrar inventario")
    print("6. Calcular valor total del inventario")
    print("7. Buscar producto")
    print("8. Salir")
    return menu(inventario, input("Seleccione una opcion: "))

def iniciar():
    print("\n--- Menu de opciones ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Mostrar inventario")
    print("6. Calcular valor total del inventario")
    print("7. Buscar producto")
    print("8. Salir")
    return menu([], input("Seleccione una opcion: "))
   
def main():
    iniciar()
    
if __name__ == "__main__":
    main()