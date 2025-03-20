from menu import *

def menu_principal_():
    print(menu_bienvenida)

    while True:
        print(menu_principal)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                
                print("Generar nuevo pedido")
            case "2":
                menu_inventario_productos_()
            case "3": 
                menu_administrar_pedidos_()
            case "4":
                print("Saliendo del portal usuario")
                break
            case _:
                print
           
def menu_inventario_productos_():
    while True:
        print(menu_inventario_productos)
        opc = input("Seleccione opcion a escoger: ")

        match opc:
            case "1":
                print
            case "2":
                print
            case "3": 
                menu_administrar_pedidos_()
            case "4":
                print
            case "5":
                print
            case "6":
                print
            case "7":
                print("Regresar al menu principal")
                break
            case _:
                print

def menu_administrar_pedidos_():
    while True:
        print(menu_administrar_pedidos)
        opc = input("Seleccione opcion a escoger: ")

        match opc:
            case "1":
                print
            case "2":
                print
            case "3": 
                print
            case "4":
                print("Regresar al menu principal")
                break
            case _:
                print

def actualizar_inventario_producto_():
    while True:
        print(actualizar_inventario_producto)
        opc = input("Seleccione opcion a escoger: ")

        match opc:
            case "1":
                print
            case "2":
                print
            case "3": 
                print("Regresar al menu inventario")
                break
            case _:
                print


menu_principal_()




