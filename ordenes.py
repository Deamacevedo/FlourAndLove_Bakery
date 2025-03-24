import json
from productos import encontrar_todos as encontrar_todos_productos, guardar_todos as guardar_todos_productos

def archivo_existe(ruta_archivo):                                             #Funcion verifica si el archivo existe, si no lo crea
    try:
        with open(ruta_archivo, "r"):
            return True
    except FileNotFoundError:
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            file.write("[]")                                                    # Si el archivo no existe, lo crea vacío con una lista vacía []
        return False
    
def guardar_ordenes(data):                                                      #Guarda los datos en el .json
    ruta_archivo = "ordenes.json"    
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as file:                #Abre el archivo en modo escritura para guardar ordenes
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")           

def encontrar_todos():                                                         #Obtiene todos los pedidos desde el archivos ordenes.json
    ruta_archivo = "ordenes.json"
    if not archivo_existe(ruta_archivo):                                        #Si no existe el archivo, retorna una lista vacia
        return []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:              
        datos = json.load(archivo)                                              #Carga el .json
        return datos                                                            #Retorna el json almacenado en la variable datos
    
def agregar_pedido(nuevo_pedido):                                               #Agrega un nuevo pedido verificando el stock de productos
    pedidos = encontrar_todos()                                                 #Encontrar todos obtiene todos los pedidos en ordenes.json
    pedidos.append(nuevo_pedido)                                                #Agrega un nuevo pedido
    productos = encontrar_todos_productos()                                     #Devuelve el stock actual de los productos

    for detalle in nuevo_pedido['detalles_pedido']:                             #For para recorrer cada producto dentro del pedido 
        codigo_producto = detalle['codigo']
        cantidad_solicitada = detalle['cantidad']
        producto = next((p for p in productos if p['codigo'] == codigo_producto), None)         #Busca el producto en la lista de productos con el next()

        if producto:
            if producto['stock'] >= cantidad_solicitada:                                        #Verifica el stock del producto con la cantidad solicitada
                producto['stock'] -= cantidad_solicitada                                        
            else:
                print(f"No hay suficiente stock para el producto {producto['nombre']}")
                pedidos.remove(nuevo_pedido)                                                    #Eliminar el pedido si no hay suficiente stock
                break
        else:
            print(f"Producto con código {codigo_producto} no encontrado")

    else:                                                                               # Este 'else' está relacionado con el ciclo for, no con el if
        guardar_ordenes(pedidos)
        guardar_todos_productos(productos)
        print(f"Pedido {nuevo_pedido['codigo_pedido']} registrado")

def encontrar_todas_ordenes():                                                         #Obtiene todos los pedidos
    pedidos = encontrar_todos()
    return pedidos

def ver_pedidos_por_codigo(codigo):                                                     #Funcion para ver los pedidos por codigos  
    pedidos = encontrar_todos()                                                         
    pedidos_filtrados = [pedido for pedido in pedidos if pedido['codigo_pedido'] == codigo]        #Crea una lista filtrada donde contiene los pedidos que coincidan con el codigo     
    if pedidos_filtrados:                                                                         #Obtiene el pedido que solicitamos con el codigo
        for pedido in pedidos_filtrados:                                                            
            print(pedido)
    else:
        print(f"No se encontraron pedidos con el código {codigo}")

def editar_pedido():                                                                              #Editar un pedido existente
    datos_pedidos = encontrar_todas_ordenes()
    if not datos_pedidos:
        print("No hay pedidos registrados")
        return

    try:
        codigo_pedido = int(input("Ingrese el código del pedido a editar: "))
    except ValueError:
        print("El código de pedido debe ser un número.")
        return

    pedido = next((pedido for pedido in datos_pedidos if pedido["codigo_pedido"] == codigo_pedido), None)       #Busca el pedido con el codigo ingresado en la lista de pedidos

    if not pedido:
        print(f"No se encontró un pedido con el código {codigo_pedido}")                                        #Si no existe el pedido retorna un none
        return

    print("Detalles del pedido actual (solo código y cantidad)")                                    
    for detalle in pedido['detalles_pedido']:
        print(f"  Producto: {detalle['codigo']} - Cantidad: {detalle['cantidad']}")

    codigo_producto = input("Ingrese el código del producto a cambiar: ")                           
    try:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número.")
        return

    actualizado = False
    for detalle in pedido['detalles_pedido']:                                                       #Recorremos la lista detalles_pedido dentro del pedido
        if detalle['codigo'] == codigo_producto:                                                    
            detalle['cantidad'] = nueva_cantidad                                                    
            actualizado = True
            print(f"Cantidad actualizada para el producto {codigo_producto}")
            break
    
    if not actualizado:
        print(f"Producto con código {codigo_producto} no se ha encontrado en el pedido")

    guardar_ordenes(datos_pedidos)                                                                  #Guarda la lista actualizada

def eliminar_pedido():                                                                              #Elimina un pedido
    datos_pedidos = encontrar_todas_ordenes()
    if not datos_pedidos:
        print("No hay pedidos registrados")
        return

    try:
        codigo_pedido = int(input("Ingrese el código del pedido que desea eliminar: "))
    except ValueError:
        print("El código de pedido debe ser un número.")
        return

    pedido = next((pedido for pedido in datos_pedidos if pedido["codigo_pedido"] == codigo_pedido), None)       #Busca el pedido con el codigo de pedido y lo almacena en la variable pedido

    if not pedido:
        print(f"No se encontró un pedido con el código {codigo_pedido}")
        return

    confirmacion = input(f"Está seguro de que desea eliminar el pedido con código {codigo_pedido}? 1.Si 2.No: ").lower()
    if confirmacion != '1':
        print("Eliminación cancelada")
        return

    datos_pedidos.remove(pedido)
    guardar_ordenes(datos_pedidos)
    print(f"Pedido con el código {codigo_pedido} ha sido eliminado")

def eliminar_producto_del_pedido(codigo_pedido, codigo_producto):                                   #Elimina un producto de un pedido segun su codigo y el codigo del producto
    ruta_archivo = "ordenes.json"    
    if not archivo_existe(ruta_archivo):
        print(f"El archivo {ruta_archivo} no existe.")
        return
    with open(ruta_archivo, 'r', encoding="utf-8") as archivo:                                      #Carga los pedidos desde el .json
        pedidos = json.load(archivo)
    try:
        codigo_pedido = int(codigo_pedido)                                                          #Asegura convertir el codigo de pedido a entero
    except ValueError:
        print(f"El código de pedido {codigo_pedido} no es válido.")
        return

    
    for pedido in pedidos:                                                                          # Buscar y eliminar el producto del pedido
        if pedido['codigo_pedido'] == codigo_pedido:
            longitud_original = len(pedido['detalles_pedido'])                                      
            pedido['detalles_pedido'] = [producto for producto in pedido['detalles_pedido'] if producto['codigo_producto'] != codigo_producto]

            if not pedido['detalles_pedido']:                                                               # Si el pedido está vacío después de eliminar el producto, preguntar si eliminarlo
                print(f"El pedido {codigo_pedido} ahora está vacío.")
                eliminar_pedido = input(f"¿Deseas eliminar el pedido {codigo_pedido} también? (s/n): ")
                if eliminar_pedido.lower() == 's':
                    pedidos.remove(pedido)

            if len(pedido['detalles_pedido']) != longitud_original:                                         # Solo guardar si hubo cambios en los detalles del pedido
                with open(ruta_archivo, 'w', encoding="utf-8") as archivo:
                    json.dump(pedidos, archivo, indent=4)                                                   
                print(f"Producto {codigo_producto} ha sido removido del pedido {codigo_pedido}")
            else:
                print(f"No se encontró el producto {codigo_producto} en el pedido {codigo_pedido}")
            break
    else:
        print(f"No se encontró un pedido con el código {codigo_pedido}")

def editar_stock_producto_en_pedido(codigo_pedido, codigo_producto, nueva_cantidad):                #Edita la cantidad en stock de un producto dentro de un pedido existente
    pedidos = encontrar_todas_ordenes()
    if not pedidos:
        print("No hay pedidos disponibles")
        return

    pedido = next((pedido for pedido in pedidos if str(pedido["codigo_pedido"]) == str(codigo_pedido)), None)       

    if not pedido:
        print(f"No se encontró un pedido con el código {codigo_pedido}")
        return

    for item in pedido["detalles_pedido"]:
        if str(item["codigo"]) == codigo_producto:
            producto_encontrado = True
            try:
                nueva_cantidad = int(nueva_cantidad)
            except ValueError:
                print("La cantidad debe ser un número válido.")
                return

            productos = encontrar_todos_productos()
            producto = next((p for p in productos if p['codigo'] == codigo_producto), None)
            if producto:
                if nueva_cantidad <= producto['stock']:
                    item['cantidad'] = nueva_cantidad
                    print(f"Se actualizó la cantidad del producto {codigo_producto} en el pedido.")
                else:
                    print(f"No hay suficiente stock disponible para el producto {codigo_producto}. Stock actual: {producto['stock']}")
            else:
                print(f"Producto con código {codigo_producto} no encontrado en el inventario.")
            break
    else:
        print(f"No se encontró el producto con código {codigo_producto} en el pedido.")

    guardar_ordenes(pedidos)
    print("Pedido actualizado correctamente.")