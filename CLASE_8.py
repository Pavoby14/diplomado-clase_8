"""Reto 2: sistema sencillo de inventario y pedidos"""

productos = []
pedidos = []


def buscar_producto(codigo):
    # Busca el codigo en la lista de productos.
    for producto in productos:
        if producto[0] == codigo:
            return producto
    return None


def registrar_producto():
    codigo = input('Codigo del producto: ').strip()
    if not codigo or buscar_producto(codigo) is not None:
        print('Codigo vacio o ya registrado.')
        return
    nombre = input('Nombre del producto: ').strip()
    if not nombre:
        print('El nombre no puede estar vacio.')
        return
    try:
        cantidad = int(input('Cantidad disponible: '))
        precio = float(input('Precio unitario: '))
    except ValueError:
        print('Cantidad o precio incorrecto.')
        return
    if cantidad < 0 or precio < 0:
        print('La cantidad y el precio no pueden ser negativos.')
        return
    productos.append([codigo, nombre, cantidad, precio])
    print('Producto registrado.')


def mostrar_productos():
    if not productos:
        print('No hay productos registrados.')
        return
    print('\n--- INVENTARIO ---')
    for producto in productos:
        print('Codigo:', producto[0], '| Nombre:', producto[1],
              '| Stock:', producto[2], '| Precio: $', format(producto[3], '.2f'))


def editar_producto():
    codigo = input('Codigo a editar: ').strip()
    producto = buscar_producto(codigo)
    if producto is None:
        print('Producto no encontrado.')
        return
    nombre = input('Nuevo nombre: ').strip()
    try:
        cantidad = int(input('Nueva cantidad: '))
        precio = float(input('Nuevo precio: '))
    except ValueError:
        print('Datos incorrectos. No se realizaron cambios.')
        return
    if not nombre or cantidad < 0 or precio < 0:
        print('Datos no validos. No se realizaron cambios.')
        return
    producto[1] = nombre
    producto[2] = cantidad
    producto[3] = precio
    print('Producto actualizado.')


def eliminar_producto():
    codigo = input('Codigo a eliminar: ').strip()
    producto = buscar_producto(codigo)
    if producto is None:
        print('Producto no encontrado.')
        return
    # Los pedidos antiguos mantienen una copia del nombre y precio.
    productos.remove(producto)
    print('Producto eliminado.')


def buscar_pedido(numero):
    for pedido in pedidos:
        if pedido[0] == numero:
            return pedido
    return None


def registrar_pedido():
    numero = input('Numero del pedido: ').strip()
    if not numero or buscar_pedido(numero) is not None:
        print('Numero vacio o ya registrado.')
        return
    codigo = input('Codigo del producto: ').strip()
    producto = buscar_producto(codigo)
    if producto is None:
        print('El producto no existe.')
        return
    try:
        cantidad = int(input('Cantidad a pedir: '))
    except ValueError:
        print('Cantidad incorrecta.')
        return
    if cantidad <= 0 or cantidad > producto[2]:
        print('Cantidad no valida o stock insuficiente.')
        return
    producto[2] -= cantidad
    pedidos.append([numero, codigo, producto[1], cantidad, producto[3]])
    print('Pedido registrado. Total: $', format(cantidad * producto[3], '.2f'))


def mostrar_pedidos():
    if not pedidos:
        print('No hay pedidos registrados.')
        return
    print('\n--- PEDIDOS ---')
    for pedido in pedidos:
        print('Pedido:', pedido[0], '| Producto:', pedido[2], '| Cantidad:', pedido[3],
              '| Total: $', format(pedido[3] * pedido[4], '.2f'))


def editar_pedido():
    numero = input('Numero del pedido a editar: ').strip()
    pedido = buscar_pedido(numero)
    if pedido is None:
        print('Pedido no encontrado.')
        return
    producto = buscar_producto(pedido[1])
    if producto is None:
        print('No se puede editar: el producto fue eliminado.')
        return
    try:
        nueva_cantidad = int(input('Nueva cantidad: '))
    except ValueError:
        print('Cantidad incorrecta.')
        return
    disponible = producto[2] + pedido[3]
    if nueva_cantidad <= 0 or nueva_cantidad > disponible:
        print('Cantidad no valida o stock insuficiente.')
        return
    producto[2] = disponible - nueva_cantidad
    pedido[3] = nueva_cantidad
    print('Pedido actualizado.')


def eliminar_pedido():
    numero = input('Numero del pedido a eliminar: ').strip()
    pedido = buscar_pedido(numero)
    if pedido is None:
        print('Pedido no encontrado.')
        return
    producto = buscar_producto(pedido[1])
    if producto is not None:
        producto[2] += pedido[3]
    pedidos.remove(pedido)
    print('Pedido eliminado. Stock devuelto si el producto existe.')


def menu():
    while True:
        print('\n===== INVENTARIO Y PEDIDOS =====')
        print('1. Registrar producto')
        print('2. Mostrar productos')
        print('3. Editar producto')
        print('4. Eliminar producto')
        print('5. Registrar pedido')
        print('6. Mostrar pedidos')
        print('7. Editar pedido')
        print('8. Eliminar pedido')
        print('0. Salir')
        opcion = input('Seleccione una opcion: ').strip()
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            editar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            registrar_pedido()
        elif opcion == '6':
            mostrar_pedidos()
        elif opcion == '7':
            editar_pedido()
        elif opcion == '8':
            eliminar_pedido()
        elif opcion == '0':
            print('Programa finalizado.')
            break
        else:
            print('Opcion no valida.')


if __name__ == '__main__':
    menu()
