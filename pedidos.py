from productos import encontrar_todos as encontrar_todos_productos, guardar_todos as guardar_productos
from ordenes import encontrar_todos as encontrar_todos_pedidos, guardar_ordenes
from tabulate import tabulate
import json

def ver_pedidos():                                                                           #Ver json de pedidos realizados                      
    datos_pedidos = encontrar_todos_pedidos()  
    if not datos_pedidos:
        print("No hay pedidos registrados")
        return
    print("Pedidos realizados:")
    print("-" * 50)
    for pedido in datos_pedidos:
        print(f"Pedido Codigo: {pedido['codigo_pedido']}")
        print(f"Detalles del pedido:")
        total_cantidad = 0
        total_precio = 0
        for detalle in pedido['detalles_pedido']:                                               #For muestra el total del pedido con sus valores
            cantidad = detalle['cantidad']
            precio_unidad = detalle['precio_unidad']
            total_cantidad += cantidad
            total_precio += cantidad * precio_unidad
            print(f"  Producto: {detalle['codigo']} - Cantidad: {cantidad} - Precio unidad: {precio_unidad}")
        print(f"Total de productos: {total_cantidad}")
        print(f"Precio total: {total_precio}")
        print("-" * 50)

def ver_pedidos_por_codigo(codigo):                                                             #Muestra el pedido con el codigo dado, y muestra el total del pedido con valores
    try:
        datos_pedidos = encontrar_todos_pedidos()

        if not isinstance(datos_pedidos, list):
            print("Error: No se pudo obtener la lista de pedidos.")
            return
        pedido = next((pedido for pedido in datos_pedidos if pedido.get("codigo_pedido") == codigo), None)
        if not pedido:
            print(f"No se encontró un pedido con el código {codigo}")
            return
        print("-" * 50)
        print(f"Pedido encontrado con código: {pedido.get('codigo_pedido')}")
        print("Detalles del pedido:")
        if not isinstance(pedido.get("detalles_pedido"), list):
            print("Este pedido no tiene detalles.")
            return

        total_cantidad = 0
        total_precio = 0
        for detalle in pedido["detalles_pedido"]:
            cantidad = detalle.get('cantidad', 0)
            precio_unidad = detalle.get('precio_unidad', 0)
            total_cantidad += cantidad
            total_precio += cantidad * precio_unidad
            print(f"  Producto: {detalle.get('codigo', 'N/A')} - Cantidad: {cantidad} - Precio unidad: {precio_unidad}")

        print("-" * 50)
        print(f"Total de productos: {total_cantidad}")
        print(f"Precio total: {total_precio}")
        print("-" * 50)
    except Exception as e:
        print(f"Error al buscar el pedido: {e}")

def formulario_realizar_pedido():                                                                   #Formulario para empezar a realizar un pedido
    datos_productos = encontrar_todos_productos()
    datos_pedidos = encontrar_todos_pedidos()

    productos_disponibles = list(filter(lambda producto: producto.get("stock") > 0, datos_productos))       #Retorna la lista con los productos con stock por encima de 0

   
    productos_filtrados = [                                                                                  # Crear copias de productos sin modificar los datos originales
        {k: v for k, v in producto.items() if k not in ["categoria", "proveedor", "precio_proveedor"]}
        for producto in productos_disponibles
    ]

    print("Lista de productos en stock")
    print(tabulate(productos_filtrados, headers="keys", tablefmt="grid", numalign="center", showindex="always"))        #Muestra la lista de productos en una tabla, sin algunas categorias

    if datos_pedidos:
        ultimo_codigo_pedido = datos_pedidos[-1]["codigo_pedido"]
    else:
        ultimo_codigo_pedido = 0  
    nuevo_codigo_pedido = ultimo_codigo_pedido + 1  

    formulario = {
        "codigo_pedido": nuevo_codigo_pedido,
        "codigo_cliente": "PN-001",
        "detalles_pedido": []
    }

    while True:
        entrada = input("Ingrese el código o índice del producto que desee (-1 para terminar): ").strip()

        if entrada == "-1":
            break
        if entrada.isdigit():  
            indice_producto = int(entrada)
            if indice_producto < 0 or indice_producto >= len(productos_disponibles):
                print("Índice inválido, inténtalo de nuevo")
                continue
            producto_seleccionado = productos_disponibles[indice_producto]
        else:  
            producto_seleccionado = next((producto for producto in productos_disponibles if producto["codigo"] == entrada), None)
            if not producto_seleccionado:
                print("Código de producto inválido, inténtalo de nuevo")
                continue

        cantidad = int(input(f"Ingrese la cantidad de '{producto_seleccionado['nombre']}' que desea (stock: {producto_seleccionado['stock']}): "))

        if cantidad > producto_seleccionado["stock"]:
            print("Cantidad no disponible")
            continue

        detalle_pedido = {
            "codigo": producto_seleccionado["codigo"],
            "cantidad": cantidad,
            "precio_unidad": producto_seleccionado["precio_venta"],
            "numero_linea": len(formulario["detalles_pedido"]) + 1
        }
        formulario["detalles_pedido"].append(detalle_pedido)

        producto_seleccionado["stock"] -= cantidad

        print(f"Producto seleccionado: {producto_seleccionado['nombre']} - Cantidad: {cantidad}")

        if producto_seleccionado["stock"] == 2:                                                                             #Alerta que avisa que solo queda poco stock de un producto
            print(f"Alerta: El producto '{producto_seleccionado['nombre']}' tiene solo 2 unidades restantes en stock.")

    if not formulario["detalles_pedido"]:
        print("No se agregó ningún producto al pedido")
        return
    
    datos_pedidos.append(formulario)
    guardar_ordenes(datos_pedidos)
    guardar_productos(datos_productos)

    ver_pedidos_por_codigo(nuevo_codigo_pedido)
