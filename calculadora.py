import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_DATOS = os.path.join(BASE_DIR, "datos")
ARCHIVO_HISTORIAL = os.path.join(CARPETA_DATOS, "historial.txt")

print("Calculadora digital-Proyecto de progra ")
# =====================================
# =======
# CALCULADORA DIGITAL
# Proyecto de Programación
# ============================================


# ============================================
# FUNCION: validar numero
# ============================================

def validar_numero(texto):
    """
    Solicita un número al usuario y valida la entrada
    """
    while True:
        try:
            numero = float(input(texto))
            return numero
        except:
            print("Error: Ingrese un número válido.")


# ============================================
# FUNCIONES DE CALCULADORA BASICA
# ============================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    return a / b


def modulo(a, b):
    return a % b


def potencia(a, b):
    return a ** b

# ============================================
# FUNCIONES DE CONVERSION DE DATOS
# ============================================

def bytes_a_kb(bytes):
    return bytes / 1024


def kb_a_bytes(kb):
    return kb * 1024


def kb_a_mb(kb):
    return kb / 1024


def mb_a_kb(mb):
    return mb * 1024


def mb_a_gb(mb):
    return mb / 1024


def gb_a_mb(gb):
    return gb * 1024

# ============================================
# FUNCIONES DE SISTEMAS NUMERICOS
# ============================================

# Decimal a Binario (ALGORITMO MANUAL)
def decimal_a_binario(decimal):

    decimal = int(decimal)

    if decimal == 0:
        return "0"

    binario = ""

    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

    return binario


# Binario a Decimal
def binario_a_decimal(binario):

    decimal = 0
    potencia = 0

    for digito in reversed(binario):

        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return decimal


# Decimal a Hexadecimal
def decimal_a_hexadecimal(decimal):

    decimal = int(decimal)

    if decimal == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""

    while decimal > 0:
        residuo = decimal % 16
        hexadecimal = hex_chars[residuo] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


# Hexadecimal a Decimal
def hexadecimal_a_decimal(hexadecimal):

    hex_chars = "0123456789ABCDEF"

    hexadecimal = hexadecimal.upper()

    decimal = 0
    potencia = 0

    for digito in reversed(hexadecimal):

        valor = hex_chars.index(digito)
        decimal += valor * (16 ** potencia)
        potencia += 1

    return decimal

# ============================================
# MENU CALCULADORA BASICA
# ============================================

def menu_calculadora():
    
    print("\n--- CALCULADORA BASICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Potencia")
    
    opcion = input("Seleccione una opción: ")
    
    a = validar_numero("Ingrese el primer número: ")
    b = validar_numero("Ingrese el segundo número: ")
    
    if opcion == "1":
        resultado = sumar(a, b)
        operacion = f"{a} + {b}"
        
    elif opcion == "2":
        resultado = restar(a, b)
        operacion = f"{a} - {b}"
        
    elif opcion == "3":
        resultado = multiplicar(a, b)
        operacion = f"{a} * {b}"
        
    elif opcion == "4":
        resultado = dividir(a, b)
        operacion = f"{a} / {b}"
        
    elif opcion == "5":
        resultado = modulo(a, b)
        operacion = f"{a} % {b}"
        
    elif opcion == "6":
        resultado = potencia(a, b)
        operacion = f"{a} ** {b}"
        
    else:
        print("Opción inválida")
        return
    
    print("Resultado:", resultado)
    
    # guardar en historial
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    agregar_al_historial(f"{fecha} | {operacion} = {resultado}")


# ============================================
# MOSTRAR HISTORIAL
# ============================================

#Agregar cosas al historial
def agregar_al_historial(operacion):

    historial.append(operacion)

    # Limitar a 10 elementos
    if len(historial) > 10:
        historial.pop(0)

# Lista para guardar historial
historial = []

def mostrar_historial():
    
    print("\n--- HISTORIAL ---")
    
    if len(historial) == 0:
        print("No hay operaciones.")
        
    else:
        for item in historial:
            print(item)

#Opción para limpiar historial
def limpiar_historial():

    historial.clear()

    print("Historial borrado correctamente")

# ============================================
# GUARDAR HISTORIAL EN ARCHIVO
# ============================================

def guardar_historial():
    try:
        if not os.path.exists(CARPETA_DATOS):
            os.makedirs(CARPETA_DATOS)

        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            for operacion in historial:
                archivo.write(operacion + "\n")

        print("Historial guardado en:", ARCHIVO_HISTORIAL)

    except Exception as e:
        print("Error al guardar historial:", e)


# ============================================
# CARGAR HISTORIAL DESDE ARCHIVO
# ============================================

def cargar_historial():
    try:
        if os.path.exists(ARCHIVO_HISTORIAL):
            with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    agregar_al_historial(linea.strip())

            print("Historial cargado correctamente")

    except Exception as e:
        print("Error al cargar historial:", e)

#Llamar a la función aquí
cargar_historial()

# ============================================
# MENU CONVERSOR DE DATOS
# ============================================

def menu_conversion():
    
    print("\n--- CONVERSOR DE UNIDADES DE DATOS ---")
    print("1. Bytes a Kilobytes")
    print("2. Kilobytes a Bytes")
    print("3. Kilobytes a Megabytes")
    print("4. Megabytes a Kilobytes")
    print("5. Megabytes a Gigabytes")
    print("6. Gigabytes a Megabytes")
    
    opcion = input("Seleccione una opción: ")
    
    valor = validar_numero("Ingrese el valor: ")
    
    if opcion == "1":
        resultado = bytes_a_kb(valor)
        operacion = f"{valor} Bytes a KB"
        
    elif opcion == "2":
        resultado = kb_a_bytes(valor)
        operacion = f"{valor} KB a Bytes"
        
    elif opcion == "3":
        resultado = kb_a_mb(valor)
        operacion = f"{valor} KB a MB"
        
    elif opcion == "4":
        resultado = mb_a_kb(valor)
        operacion = f"{valor} MB a KB"
        
    elif opcion == "5":
        resultado = mb_a_gb(valor)
        operacion = f"{valor} MB a GB"
        
    elif opcion == "6":
        resultado = gb_a_mb(valor)
        operacion = f"{valor} GB a MB"
        
    else:
        print("Opción inválida")
        return
    
    print("Resultado:", resultado)
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    agregar_al_historial(f"{fecha} | {operacion} = {resultado}")

# ============================================
# MENU SISTEMAS NUMERICOS
# ============================================

def menu_sistemas():

    print("\n--- SISTEMAS NUMERICOS ---")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Decimal a Hexadecimal")
    print("4. Hexadecimal a Decimal")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        valor = validar_numero("Ingrese número decimal: ")
        resultado = decimal_a_binario(valor)
        operacion = f"{int(valor)} decimal a binario"

    elif opcion == "2":

        valor = input("Ingrese número binario: ")
        resultado = binario_a_decimal(valor)
        operacion = f"{valor} binario a decimal"

    elif opcion == "3":

        valor = validar_numero("Ingrese número decimal: ")
        resultado = decimal_a_hexadecimal(valor)
        operacion = f"{int(valor)} decimal a hexadecimal"

    elif opcion == "4":

        valor = input("Ingrese número hexadecimal: ")
        resultado = hexadecimal_a_decimal(valor)
        operacion = f"{valor} hexadecimal a decimal"

    else:
        print("Opción inválida")
        return

    print("Resultado:", resultado)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    agregar_al_historial(f"{fecha} | {operacion} = {resultado}")

# ============================================
# MENU PRINCIPAL
# ============================================

def menu_principal():
    
    while True:
        
        print("\n====== CALCULADORA DIGITAL ======")
        print("1. Calculadora básica")
        print("2. Conversor de datos")
        print("3. Sistemas numericos")
        print("4. Ver historial")
        print("5. Borrar el historial")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_calculadora()
            
        elif opcion == "2":
            menu_conversion()
            
        elif opcion == "3":
            menu_sistemas()
        
        elif opcion == "4":
            mostrar_historial()
        
        elif opcion == "5":
            limpiar_historial()

        elif opcion == "6":
            guardar_historial()
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida")

# ============================================
# INICIAR PROGRAMA
# ============================================

menu_principal()
#CSV import
