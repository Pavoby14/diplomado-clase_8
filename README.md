# Reto 2: Sistema de gestión de pedidos e inventario

Actividad de **Arreglos y tipos abstractos de datos (Parte 1)** realizada en Python.

## ¿Qué hace el programa?

Permite registrar, mostrar, editar y eliminar productos y pedidos desde un menú. Usa listas para almacenar los datos y funciones para organizar cada operación. Al registrar un pedido descuenta las unidades del inventario; al eliminarlo, las devuelve si el producto todavía existe.

## Ejecución

1. Tener Python 3 instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python reto2_inventario_pedidos.py
```

4. Seleccionar las opciones del menú. Primero registrar un producto y luego crear un pedido.

## Funciones principales

- `registrar_producto`, `mostrar_productos`, `editar_producto`, `eliminar_producto`: gestionan el inventario.
- `registrar_pedido`, `mostrar_pedidos`, `editar_pedido`, `eliminar_pedido`: gestionan los pedidos.
- `buscar_producto`, `buscar_pedido`: encuentran registros por su código o número.
- `menu`: muestra las opciones y permite repetir acciones hasta elegir 0.

## Estructuras utilizadas

- **Listas:** almacenan productos y pedidos; cada registro es otra lista.
- **Condicionales `if`:** validan las opciones, los datos y el stock.
- **Ciclos `for`:** recorren los registros.
- **Ciclo `while`:** mantiene el menú activo.
- **Funciones:** separan las distintas tareas para facilitar cambios futuros.

## Rendimiento y mejoras posibles

La búsqueda por código recorre las listas y tarda más cuantos más registros existan. Para una aplicación grande se podrían utilizar diccionarios y una base de datos. Esta versión es educativa: **los datos se pierden al cerrar el programa**. No guarda información de forma permanente.

## Capturas del programa en ejecución

Una vez ejecutado el programa, tomar capturas de la pantalla y guardarlas dentro de la carpeta `imagenes` con estos nombres:

### Menú principal
![Menú principal](imagenes/menu.png)

### Productos registrados
![Productos registrados](imagenes/productos.png)

### Pedidos registrados
![Pedidos registrados](imagenes/pedidos.png)

> Las capturas deben ser reales y tomadas al ejecutar el archivo `.py` en tu computadora. Agrega estas imágenes a GitHub junto con el código.
