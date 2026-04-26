from datetime import datetime
from collections import deque

clientes = []

cola_urgente = deque()
cola_general = deque()

turnos_urgente = 2
turnos_general = 1
contador_u = 0
contador_g = 0


while True:
    print("\n" + "="*40)
    print("       REGISTRO DE NUEVO CLIENTE")
    print("="*40)

    # CÉDULA (solo números)
    while True:
        cedula = input("Cédula (solo números): ").strip()
        if cedula.isdigit():
            break
        else:
            print("Error: la cédula solo puede contener números.")

    # NOMBRE (solo letras, máximo 50 caracteres)
    while True:
        nombre = input("Nombre (solo letras, máx 50 caracteres): ").strip()
        nombre = " ".join(nombre.split())

        if len(nombre) > 50:
            print("Error: el nombre no puede superar 50 caracteres.")
        elif not nombre.replace(" ", "").isalpha():
            print("Error: el nombre solo puede contener letras.")
        else:
            break

    # TELÉFONO (solo números)
    while True:
        telefono = input("Teléfono (solo números): ").strip()
        if telefono.isdigit():
            break
        else:
            print("Error: el teléfono solo puede contener números.")

    # TIPO ATENCIÓN
    while True:
        tipo_atencion = input("Tipo Atención (LIMPIEZA/CALZAS/EXTRACCION/DIAGNOSTICO): ").strip().upper()
        if tipo_atencion in ["LIMPIEZA", "CALZAS", "EXTRACCION", "DIAGNOSTICO"]:
            break
        print("Error: tipo de atención inválido.")

    # PRIORIDAD
    while True:
        prioridad = input("Prioridad (NORMAL/URGENTE): ").strip().upper()
        if prioridad in ["NORMAL", "URGENTE"]:
            break
        print("Error: prioridad inválida.")
    
    # FECHA
    while True:
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        try:
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
            break
        except:
            print("Error: formato de fecha inválido. Use DD/MM/AAAA.")

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_atencion": tipo_atencion,
        "prioridad": prioridad,
        "fecha": fecha,
        "fecha_obj": fecha_obj
    }

    clientes.append(cliente)

    # CLASIFICACIÓN EN COLAS
    if tipo_atencion == "EXTRACCION" and prioridad == "URGENTE":
        cola_urgente.append(cliente)
    else:
        cola_general.append(cliente)

    continuar = input("¿Otro cliente? (s/n): ").strip().lower()
    if continuar != "s":
        break


# =========================
# MENÚ
# =========================
while True:
    print("\n" + "="*40)
    print(" CONSULTORIO ODONTOLÓGICO")
    print("="*40)
    print("1. Ver urgencias (extracciones)")
    print("2. Atender siguiente")
    print("3. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        print("\n--- URGENCIAS (EXTRACCIONES) ---")

        if not cola_urgente:
            print("No hay urgencias.")
        else:
            lista = sorted(list(cola_urgente), key=lambda x: x["fecha_obj"])
            for c in lista:
                print(f"{c['cedula']} - {c['nombre']} - {c['fecha']}")

    elif opcion == "2":
        if not cola_urgente and not cola_general:
            print("No hay pacientes.")
            continue

        if cola_urgente and (contador_u < turnos_urgente or not cola_general):
            c = cola_urgente.popleft()
            contador_u += 1
            contador_g = 0
            print(f"Atendiendo URGENTE: {c['nombre']} - {c['fecha']}")
        else:
            c = cola_general.popleft()
            contador_g += 1
            contador_u = 0
            print(f"Atendiendo GENERAL: {c['nombre']} - {c['tipo_atencion']}")

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
        