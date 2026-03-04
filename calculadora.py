import csv
from datetime import datetime

print("Calculadora digital-Proyecto de progra ")
# =====================================
# =======
# CALCULADORA DIGITAL
# Proyecto de Programación
# ============================================

# Lista para guardar historial
historial = []


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
    historial.append(f"{operacion} = {resultado}")


# ============================================
# MOSTRAR HISTORIAL
# ============================================

def mostrar_historial():
    
    print("\n--- HISTORIAL ---")
    
    if len(historial) == 0:
        print("No hay operaciones.")
        
    else:
        for item in historial:
            print(item)

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
# MENU PRINCIPAL
# ============================================

def menu_principal():
    
    while True:
        
        print("\n====== CALCULADORA DIGITAL ======")
        print("1. Calculadora básica")
        print("2. Ver historial")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_calculadora()
            
        elif opcion == "2":
            mostrar_historial()
            
        elif opcion == "3":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida")


# ============================================
# INICIAR PROGRAMA
# ============================================

menu_principal()
#CSV import
