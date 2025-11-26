import mysql.connector
from mysql.connector import Error
def conectar_mysql(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if conn.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return conn

    except mysql.connector.ProgrammingError as e:
        print(f"Error al conectar a MySQL: : {e}")
        return None
conexion = conectar_mysql("localhost", "root", "", "ferreteria")
cur = conexion.cursor()

def inicio_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    cur.execute("SELECT * FROM trabajadores WHERE usuario=%s AND contrasena=%s",
                (usuario, contrasena))
    datos = cur.fetchone()

    if datos:
        print("Inicio de sesión correcto. Bienvenido:", datos[2])
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False

def alta_producto():
    print("\n--- Alta de Producto ---")
    codigo = input("Código: ")

    cur.execute("SELECT * FROM productos WHERE codigo=%s", (codigo,))
    if cur.fetchone():
        print("Ese código ya existe.")
        return

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    marca = input("Marca: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    cur.execute("""
        INSERT INTO productos (codigo, nombre, categoria, marca, descripcion, precio, stock)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (codigo, nombre, categoria, marca, descripcion, precio, stock))

    conexion.commit()
    print("Producto registrado.")


# =======================================
# ALTA CLIENTE
# =======================================
def alta_cliente():
    print("\n--- Alta de Cliente ---")
    clave = input("Clave del cliente: ")

    cur.execute("SELECT * FROM clientes WHERE clave=%s", (clave,))
    if cur.fetchone():
        print("Esa clave ya existe.")
        return

    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    cur.execute("""
        INSERT INTO clientes (clave, nombre, telefono, correo)
        VALUES (%s,%s,%s,%s)
    """, (clave, nombre, telefono, correo))

    conexion.commit()
    print("Cliente registrado.")


# =======================================
# CONSULTAR PRODUCTO
# =======================================
def consultar_producto():
    print("\n--- Consultar Producto ---")
    codigo = input("Código del producto: ")

    cur.execute("SELECT * FROM productos WHERE codigo=%s", (codigo,))
    prod = cur.fetchone()

    if prod:
        print(f"\nCódigo: {prod[1]}")
        print(f"Nombre: {prod[2]}")
        print(f"Categoría: {prod[3]}")
        print(f"Marca: {prod[4]}")
        print(f"Descripción: {prod[5]}")
        print(f"Precio: {prod[6]}")
        print(f"Stock: {prod[7]}")
    else:
        print("Producto no encontrado.")


# =======================================
# CONSULTAR CLIENTE
# =======================================
def consultar_cliente():
    print("\n--- Consultar Cliente ---")
    clave = input("Clave del cliente: ")

    cur.execute("SELECT * FROM clientes WHERE clave=%s", (clave,))
    cli = cur.fetchone()

    if cli:
        print(f"\nClave: {cli[1]}")
        print(f"Nombre: {cli[2]}")
        print(f"Teléfono: {cli[3]}")
        print(f"Correo: {cli[4]}")
    else:
        print("Cliente no encontrado.")


# =======================================
# MOSTRAR TODOS LOS PRODUCTOS
# =======================================
def mostrar_productos():
    print("\n--- Productos Registrados ---")
    cur.execute("SELECT * FROM productos")
    datos = cur.fetchall()

    if not datos:
        print("No hay productos registrados.")
    else:
        for p in datos:
            print(f"[{p[1]}] {p[2]} | {p[4]} | ${p[6]} | Stock: {p[7]}")


# =======================================
# MOSTRAR TODOS LOS CLIENTES
# =======================================
def mostrar_clientes():
    print("\n--- Clientes Registrados ---")
    cur.execute("SELECT * FROM clientes")
    datos = cur.fetchall()

    if not datos:
        print("No hay clientes registrados.")
    else:
        for c in datos:
            print(f"[{c[1]}] {c[2]} | Tel: {c[3]}")


# =======================================
# REGISTRAR VENTA
# =======================================
def realizar_venta():
    print("\n--- Registrar Venta ---")
    codigo = input("Código del producto: ")

    cur.execute("SELECT * FROM productos WHERE codigo=%s", (codigo,))
    prod = cur.fetchone()

    if not prod:
        print("Producto no encontrado.")
        return

    cantidad = int(input("Cantidad: "))

    if cantidad > prod[7]:
        print("No hay suficiente stock.")
        return

    cliente = input("Clave de cliente (999 si es público): ")

    fecha = input("Fecha de venta (dd/mm/aaaa): ")

    total = prod[6] * cantidad

    cur.execute("""
        INSERT INTO ventas (codigo_producto, id_cliente, fecha, cantidad, total)
        VALUES (%s,%s,%s,%s,%s)
    """, (codigo, cliente, fecha, cantidad, total))

    nuevo_stock = prod[7] - cantidad
    cur.execute("UPDATE productos SET stock=%s WHERE codigo=%s",
                (nuevo_stock, codigo))

    conexion.commit()
    print("Venta registrada.")



def mostrar_ventas():
    print("\n--- Historial de Ventas ---")
    cur.execute("SELECT * FROM ventas")
    ventas = cur.fetchall()

    if not ventas:
        print("No hay ventas registradas.")
    else:
        for v in ventas:
            print(f"Folio {v[0]} | Producto: {v[1]} | Cliente: {v[2]} | Fecha: {v[3]} | Cant: {v[4]} | Total: {v[5]}")



def menu():
    while True:
        print("\n--- SISTEMA DE FERRETERÍA ---")
        print("1. Alta producto")
        print("2. Alta cliente")
        print("3. Consultar producto")
        print("4. Consultar cliente")
        print("5. Mostrar todos los productos")
        print("6. Mostrar todos los clientes")
        print("7. Registrar venta")
        print("8. Mostrar ventas")
        print("9. Salir")

        op = input("Opción: ")

        if op == "1":
            alta_producto()
        elif op == "2":
            alta_cliente()
        elif op == "3":
            consultar_producto()
        elif op == "4":
            consultar_cliente()
        elif op == "5":
            mostrar_productos()
        elif op == "6":
            mostrar_clientes()
        elif op == "7":
            realizar_venta()
        elif op == "8":
            mostrar_ventas()
        elif op == "9":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
if inicio_sesion():
    menu()
