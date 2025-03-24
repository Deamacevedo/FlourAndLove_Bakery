from productos import encontrar_todos, agregar_producto, guardar_todos
from tabulate import tabulate

def formulario_agregar_producto():                                                          #Funcion para agregar productos con todos sus atributos
    datos = encontrar_todos()
    codigo_producto = input("Ingrese el codigo del producto: ") 
    productos_encontrados = list(filter(lambda producto: producto.get("codigo") == codigo_producto, datos))
    if not len(productos_encontrados):
        formulario = {
            "codigo": codigo_producto,
            "nombre": input("Ingrese el nombre del producto: "),
            "categoria": input("Ingrese la categoria del producto ejemplo (pan, pastel, postre): "),
            "descripcion": input("Ingrese la descripcion del producto: "),
            "proveedor": input("Ingrese el proveedor del producto: "),
            "stock": input("Ingrese el stock del producto: "),
            "precio_compra": input("Ingrese el precio de compra del producto: "),
            "precio_venta": input("Ingrese el precio de venta del producto: ")  
            }
        agregar_producto(formulario)
        print(f"Producto {formulario['codigo']} agregado correctamente")
    else:
        print("El codigo del producto ya existe")

def tabla_productos():
    datos = encontrar_todos()
    datos_modificados = []
    for diccionario in datos:
        diccionario.pop("descripcion", None)  
        diccionario.pop("proveedor", None)
        diccionario.pop("precio_compra", None)
        datos_modificados.append(diccionario)
    print(tabulate(datos_modificados, headers="keys", tablefmt="grid", numalign="center", showindex="always"))

def tabla_productos_por_categoria(categoria):
    datos = encontrar_todos()  
    datos_modificados = []
    categoria = categoria.lower()  
    for diccionario in datos:
        if diccionario.get("categoria", "").lower() == categoria:
            diccionario.pop("proveedor", None)
            diccionario.pop("precio_compra", None)
            datos_modificados.append(diccionario)
    if datos_modificados:
        print(tabulate(datos_modificados, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    else:
        print(f"No se encontraron productos en la categoria '{categoria}'")

def buscar_producto_por_nombre(nombre):
    datos = encontrar_todos()
    productos_encontrados = list(filter(lambda producto: nombre.lower() in producto["nombre"].lower(), datos))
    
    if productos_encontrados:
        print(tabulate(productos_encontrados, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    else:
        print(f"No se encontraron productos con el nombre '{nombre}'")
    
def buscar_producto_por_codigo(codigo_producto):
    datos = encontrar_todos()  
    producto = next((p for p in datos if p['codigo'] == codigo_producto), None)
    if producto:
        print("\nProducto encontrado:")
        print(tabulate([producto], headers="keys", tablefmt="grid", numalign="center", showindex=False))
    else:
        print(f"No se encontro un producto con el codigo '{codigo_producto}'")

def actualizar_inventario():
    codigo_producto = input("Ingrese el codigo del producto para actualizar: ")
    cantidad_a_actualizar = int(input("Ingrese la cantidad a agregar: "))
    datos = encontrar_todos()
    producto = next((p for p in datos if p['codigo'] == codigo_producto), None)
    if producto:
        nuevo_stock = producto['stock'] + cantidad_a_actualizar
        if nuevo_stock >= 0:
            producto['stock'] = nuevo_stock
            guardar_todos(datos)
            print(f"Inventario actualizado para {producto['nombre']}. Nueva cantidad en stock: {producto['stock']}")
        else:
            print("No se puede actualizar el inventario con una cantidad negativa. El inventario no puede ser menor a 0")
    else:
        print(f"No se encontro un producto con el codigo '{codigo_producto}'")

def eliminar_producto_por_codigo(codigo_producto):
    datos = encontrar_todos()
    producto = next((p for p in datos if p['codigo'] == codigo_producto), None)
    if producto:
        datos.remove(producto)
        guardar_todos(datos)
        print(f"Producto con codigo '{codigo_producto}' eliminado correctamente")
    else:
        print(f"No se encontro un producto con el codigo '{codigo_producto}'")

