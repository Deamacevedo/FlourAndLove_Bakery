from menu import *
from productos import descontar_inventario,actualizar_inventario,eliminar_producto_del_pedido
from usuario import formulario_agregar_producto,tabla_productos,tabla_productos_por_categoria
from usuario import buscar_producto_por_codigo,buscar_producto_por_nombre,eliminar_producto_por_codigo
from pedidos import formulario_realizar_pedido,ver_pedidos_por_codigo,ver_pedidos
from ordenes import eliminar_pedido,editar_stock_producto_en_pedido

def menu_principal_():
    print(menu_bienvenida)
    while True:
        print(menu_principal)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                formulario_realizar_pedido()
            case "2":
                menu_inventario_productos_()
            case "3": 
                menu_administrar_pedidos_()
            case "4":
                print("Saliendo del portal usuario")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")
           
def menu_inventario_productos_():
    while True:
        print(menu_inventario_productos)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                tabla_productos()
            case "2":
                dato_categoria = input("Ingrese la categoria: Pan, Pastel, Postre: ").lower()
                tabla_productos_por_categoria(dato_categoria)
            case "3": 
                menu_actualizar_inventario_producto_()
            case "4":
                menu_editar_productos_()
            case "5":
                nombre_producto = input("Ingrese el nombre del producto: ")
                buscar_producto_por_nombre(nombre_producto)
            case "6":
                codigo_producto = input("Ingrese el codigo del producto: ")
                buscar_producto_por_codigo(codigo_producto)
            case "7":
                print("Regresar al menu principal")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")

def menu_administrar_pedidos_():
    while True:
        print(menu_administrar_pedidos)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                menu_editar_pedido_()
            case "2":
                eliminar_pedido()
            case "3": 
                ver_pedidos()
            case "4":
                try:
                    codigo_pedido = int(input("Ingrese codigo del pedido: "))
                    ver_pedidos_por_codigo(codigo_pedido)
                except ValueError:
                    print("Error: Debe ingresar un número entero válido para el código del pedido.")
            case "5":
                print("Regresar al menu principal")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")

def menu_actualizar_inventario_producto_():
    while True:
        print(menu_actualizar_inventario_producto)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                codigo_producto = input("Digite el codigo del producto: ")
                cantidad_aumentar = int(input("Digite la cantidad a aumentar: "))
                actualizar_inventario(codigo_producto,cantidad_aumentar)
            case "2":
                codigo_producto = input("Digite el codigo del producto: ")
                cantidad_disminuir = int(input("Digite la cantidad a descontar: "))
                descontar_inventario(codigo_producto,cantidad_disminuir)
            case "3": 
                print("Regresar al menu inventario")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")

def menu_editar_pedido_():
    while True:
        print(menu_editar_pedido)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                codigo_producto = input("Ingrese el codigo del producto: ")
                eliminar_producto_del_pedido(codigo_producto)
            case "2":
                codigo_pedido = input("Ingrese el codigo de la orden: ")
                codigo_producto = input("Ingrese el codigo del producto: ")
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                editar_stock_producto_en_pedido(codigo_pedido,codigo_producto,nueva_cantidad)
            case "3":
                print("Regresar al menu pedidos")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")

def menu_editar_productos_():
    while True:
        print(menu_editar_productos)
        opc = input("Seleccione opcion a escoger: ")
        match opc:
            case "1":
                formulario_agregar_producto()
            case "2":
                codigo_producto = input("Ingrese el codigo del producto a remover: ")
                eliminar_producto_por_codigo(codigo_producto)
            case "3":
                print("Regresar al menu inventario de productos")
                break
            case _:
                print("Digite una opcion valida. ")
                print("")
