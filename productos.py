import json

def archivo_existe(ruta_archivo):                                        # Funcion para verificar que el archivo existe
    try:
        with open(ruta_archivo, "r", encoding="utf-8"):                 
            return True                          
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return False

def guardar_productos(datos):                                            # Funcion para guardar los productos en un archivo .json
    ruta_archivo = "productos.json"                                        # Guardar en el mismo directorio
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:         # Abre el archivo en modo escritura
            json.dump(datos, archivo, indent=4)                             # Guarda los datos en el archivo   
    except IOError as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")           

def encontrar_todos():                                                          #Retorna todos los productos
    ruta_archivo = "productos.json"                                            
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:                #Abre el archivo en modo lectura
            datos = json.load(archivo)  
        return datos
    except FileNotFoundError:
        return []                                                                # retorna una lista vacia si no encuentra el archivo
    except json.JSONDecodeError:
        print(f"Error al leer {ruta_archivo}: JSON mal formado")
        return []                                                               

def guardar_todos(datos):                                                        #Guarda los productos en el json
    ruta_archivo = "productos.json"                                              
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:               
            json.dump(datos, archivo, indent=4)
    except IOError as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")

def actualizar_inventario(codigo_producto, cantidad_aumentar):                    #Aumenta el inventario de un producto en el .json, solo admite valores positivos
    ruta_archivo = "productos.json"                                               # Archivo en el mismo directorio
    
    if cantidad_aumentar <= 0:                                                    #Verifica que la cantidad sea positiva
        print("Error: La cantidad a aumentar debe ser un número positivo.")
        return
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
        return
    except json.JSONDecodeError:
        print(f"Error al leer {ruta_archivo}: JSON mal formado.")
        return

    producto_encontrado = False
    for producto in productos:                                                          #Ciclo for para recorrer la lista con codigo y stock para aumentar
        if producto['codigo'] == codigo_producto:
            producto_encontrado = True
            producto['stock'] += cantidad_aumentar
            print(f"Inventario actualizado para {producto['nombre']}. Nueva cantidad en stock: {producto['stock']}")
            break

    if not producto_encontrado:
        print(f"Producto con código {codigo_producto} no encontrado.")
        return

    try:
        with open(ruta_archivo, 'w', encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4)
        print("Cambios guardados en el archivo products.json.")
    except IOError as e:
        print(f"Error al guardar los cambios en {ruta_archivo}: {e}")

def agregar_producto(nuevo_producto):                                               #Agrega un nuevo producto y hace la funcion de añadirlo al .json
    productos = encontrar_todos() 
    productos.append(nuevo_producto)  
    guardar_todos(productos)

def encontrar_producto_por_codigo(codigo):                                          #Busca en la lista de productos el producto por codigo
    productos = encontrar_todos() 
    producto = next((producto for producto in productos if producto['codigo'] == codigo), None)
    return producto

def editar_producto(codigo_producto, nombre=None, categoria=None, descripcion=None):      #Editar productos en codigo  
    productos = encontrar_todos() 
    producto = encontrar_producto_por_codigo(codigo_producto)

    if not producto:
        print(f"Producto con código {codigo_producto} no encontrado")
        return False

    if nombre:
        producto['nombre'] = nombre
    if categoria:
        producto['categoria'] = categoria
    if descripcion:
        producto['descripcion'] = descripcion

    guardar_todos(productos)  
    print(f"Producto {codigo_producto} editado correctamente")
    return True

def eliminar_producto(codigo_producto):                                             #Elimina un producto con codigo
    productos = encontrar_todos() 
    producto = encontrar_producto_por_codigo(codigo_producto)

    if not producto:
        print(f"Producto con código {codigo_producto} no encontrado")
        return False
    
    productos.remove(producto)  
    guardar_todos(productos)  
    print(f"Producto {codigo_producto} eliminado correctamente")
    return True

def editar_stock_producto(codigo_producto, nuevo_stock):                                #Actualiza el stock de un producto
    productos = encontrar_todos() 
    producto = encontrar_producto_por_codigo(codigo_producto)

    if not producto:
        print(f"Producto con código {codigo_producto} no encontrado.")
        return False
    
    producto['stock'] = nuevo_stock
    guardar_todos(productos)  
    print(f"Stock del producto {codigo_producto} actualizado a {nuevo_stock}.")
    return True

def actualizar_cantidad_producto_en_pedido(pedido, codigo_producto, nueva_cantidad):            #Edita la cantidad de producto en un pedido
    for item in pedido['detalles_pedido']:
        if item['codigo'] == codigo_producto:
            item['cantidad'] = nueva_cantidad
            return True
    return False

def eliminar_producto_del_pedido(codigo_producto):                                                  #Elimina un producto de un pedido
    ruta_archivo_pedidos = "ordenes.json"  
    try:
        with open(ruta_archivo_pedidos, 'r', encoding="utf-8") as archivo:
            pedidos = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo_pedidos} no existe.")
        return
    except json.JSONDecodeError:
        print(f"Error al leer {ruta_archivo_pedidos}: JSON mal formado.")
        return

    pedido_encontrado = False   
    producto_eliminado = False

    for pedido in pedidos:                                                                          #Recorre cada pedido en la lista pedidos
        if 'detalles_pedido' in pedido and isinstance(pedido['detalles_pedido'], list):             #Verifica si el pedido tiene la clave detalles_pedido y si es una lista
            for producto in pedido['detalles_pedido']:                                              #Recorre la lista detalles_pedido dentro de pedido
                if isinstance(producto, dict) and producto.get("codigo") == codigo_producto:        #Verifica el diccionario y si coinciden los codigos
                    pedido['detalles_pedido'].remove(producto)
                    producto_eliminado = True                                               
                    print(f"Producto {codigo_producto} eliminado del pedido.")
                    
                    if not pedido['detalles_pedido']:
                        pedidos.remove(pedido)
                        print("El pedido está vacío y será eliminado.")
                    break
            if producto_eliminado:
                pedido_encontrado = True
                break

    if not pedido_encontrado:
        print(f"Producto con código {codigo_producto} no encontrado en ningún pedido.")
        return

    try:
        with open(ruta_archivo_pedidos, 'w', encoding="utf-8") as archivo:
            json.dump(pedidos, archivo, indent=4)
        print("Cambios guardados en el archivo pedidos.json.")
    except IOError as e:
        print(f"Error al guardar los cambios en {ruta_archivo_pedidos}: {e}")

def imprimir_detalles_producto():                                                                   #Imprime los detalles de un producto
    productos = encontrar_todos()
    print("-" * 60)
    print("| codigo_producto | nombre          | cantidad_en_stock | precio_unidad |")
    for item in productos:
        print(f"| {item['codigo']}          | {item['nombre']}           | {item['stock']}            | {item['precio_unidad']}         |")
    print("-" * 60)

def editar_precio_producto(codigo_producto, nuevo_precio):                                          #Edita precio de un producto
    productos = encontrar_todos() 
    producto = encontrar_producto_por_codigo(codigo_producto)

    if not producto:
        print(f"Producto con código {codigo_producto} no encontrado.")
        return False
    
    producto['precio_unidad'] = nuevo_precio
    guardar_todos(productos)  
    print(f"Precio del producto {codigo_producto} actualizado a {nuevo_precio}.")
    return True

def encontrar_productos_por_nombre(nombre):                                                         #Encuentra productos por nombre
    productos = encontrar_todos()
    productos_coincidentes = [producto for producto in productos if nombre.lower() in producto['nombre'].lower()]
    
    if not productos_coincidentes:
        print(f"No se encontraron productos con el nombre {nombre}.")
        return []

    print("-" * 60)
    print("| codigo_producto | nombre          | cantidad_en_stock | precio_unidad |")
    for item in productos_coincidentes:
        print(f"| {item['codigo']}          | {item['nombre']}           | {item['stock']}            | {item['precio_unidad']}         |")
    print("-" * 60)
    return productos_coincidentes

def alerta_bajo_stock():                                                                            #Crea una alerta cuando el stock esta por debajo de dos
    productos = encontrar_todos()
    productos_bajo_stock = [producto for producto in productos if producto['cantidad_en_stock'] < 2]
        
    if not productos_bajo_stock:
        print("No hay productos con bajo stock.")
        return

    print("Alerta: Los siguientes productos tienen menos de 2 unidades en stock:")
    print("-" * 60)
    print("| codigo_producto | nombre          | cantidad_en_stock |")
    for item in productos_bajo_stock:
        print(f"| {item['codigo']}          | {item['nombre']}           | {item['stock']}            |")
    print("-" * 60)

def descontar_inventario(codigo_producto, cantidad_vendida):                                        #Descuenta productos del inventario en el archivo .json, solo permite valores positivos
    ruta_archivo = "productos.json" 
    if cantidad_vendida <= 0:
        print("Error: La cantidad a descontar debe ser un número positivo.")
        return

    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
        return
    except json.JSONDecodeError:
        print(f"Error al leer {ruta_archivo}: JSON mal formado.")
        return

    producto_encontrado = False
    for producto in productos:
        if producto['codigo'] == codigo_producto:
            producto_encontrado = True

            # Verificar si hay suficiente stock para la venta
            if producto['stock'] < cantidad_vendida:
                print(f"No hay suficiente inventario para vender {cantidad_vendida} unidades del producto {producto['nombre']}. Stock actual: {producto['stock']}")
                return
            
            # Descontar del stock
            producto['stock'] -= cantidad_vendida
            print(f"Inventario actualizado para {producto['nombre']}. Nueva cantidad en stock: {producto['stock']}")
            break

    if not producto_encontrado:
        print(f"Producto con código {codigo_producto} no encontrado.")
        return

    try:
        with open(ruta_archivo, 'w', encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4)
        print("Cambios guardados en el archivo products.json.")
    except IOError as e:
        print(f"Error al guardar los cambios en {ruta_archivo}: {e}")