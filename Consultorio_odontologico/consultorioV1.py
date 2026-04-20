# Programa Consultorio Odontológico

clientes = []

total_clientes = 0
total_ingresos = 0
total_extracciones = 0

# Valores
valor_cita = {
    "PARTICULAR": 80000,
    "EPS": 5000,
    "PREPAGADA": 30000
}

valor_atencion = {
    "PARTICULAR": {
        "LIMPIEZA": 60000,
        "CALZAS": 80000,
        "EXTRACCION": 100000,
        "DIAGNOSTICO": 50000
    },
    "EPS": {
        "LIMPIEZA": 0,
        "CALZAS": 40000,
        "EXTRACCION": 40000,
        "DIAGNOSTICO": 0
    },
    "PREPAGADA": {
        "LIMPIEZA": 0,
        "CALZAS": 10000,
        "EXTRACCION": 10000,
        "DIAGNOSTICO": 0
    }
}

tipos_clientes_validos = ["PARTICULAR", "EPS", "PREPAGADA"]
tipos_atencion_validos = ["LIMPIEZA", "CALZAS", "EXTRACCION", "DIAGNOSTICO"]

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

    # TIPO CLIENTE
    tipo_cliente = input("Tipo Cliente (PARTICULAR/EPS/PREPAGADA): ").strip().upper()
    while tipo_cliente not in tipos_clientes_validos:
        print("Tipo de cliente inválido.")
        tipo_cliente = input("Ingrese nuevamente (PARTICULAR/EPS/PREPAGADA): ").strip().upper()

    # TIPO ATENCIÓN
    tipo_atencion = input("Tipo Atención (LIMPIEZA/CALZAS/EXTRACCION/DIAGNOSTICO): ").strip().upper()
    while tipo_atencion not in tipos_atencion_validos:
        print("Tipo de atención inválido.")
        tipo_atencion = input("Ingrese nuevamente (LIMPIEZA/CALZAS/EXTRACCION/DIAGNOSTICO): ").strip().upper()

    # CANTIDAD
    if tipo_atencion in ["LIMPIEZA", "DIAGNOSTICO"]:
        cantidad = 1
    else:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                cantidad = 1
        except:
            cantidad = 1

    # PRIORIDAD
    prioridad = input("Prioridad (NORMAL/URGENTE): ").strip().upper()
    while prioridad not in ["NORMAL", "URGENTE"]:
        print("Prioridad inválida.")
        prioridad = input("Ingrese nuevamente (NORMAL/URGENTE): ").strip().upper()
    
    fecha = input("Fecha (DD/MM/AAAA): ").strip()

    # CÁLCULO
    cita = valor_cita.get(tipo_cliente, 0)
    atencion = valor_atencion.get(tipo_cliente, {}).get(tipo_atencion, 0)

    total = cita + (atencion * cantidad)

    # REGISTRO
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha": fecha,
        "total": total
    }

    clientes.append(cliente)

    # ACUMULADORES
    total_clientes += 1
    total_ingresos += total

    if tipo_atencion == "EXTRACCION":
        total_extracciones += 1

    continuar = input("¿Otro cliente? (s/n): ").strip().lower()
    if continuar != "s":
        break

# ORDENAR CLIENTES
clientes.sort(key=lambda x: x["total"], reverse=True)

# RESULTADOS
print("\n" + "="*40)
print("         RESUMEN FINAL")
print("="*40)
print(f"Total clientes atendidos: {total_clientes}")
print(f"Ingresos totales: ${total_ingresos:,}")
print(f"Total extracciones: {total_extracciones}")

print("\n" + "="*40)
print("    LISTA DE CLIENTES (por ingreso)")
print("="*40)
print(f"{'Cédula':<12} {'Nombre':<20} {'Teléfono':<12} {'Total':>10}")
print("-"*40)
for c in clientes:
    print(f"{c['cedula']:<12} {c['nombre']:<20} {c['telefono']:<12} ${c['total']:>8,}")

# BÚSQUEDA
buscar = input("\nIngrese cédula a buscar: ").strip()
while not buscar.isdigit():
    print("Error: la cédula solo puede contener números.")
    buscar = input("Ingrese nuevamente: ").strip()

encontrado = False
for c in clientes:
    if c["cedula"] == buscar:
        print("\n" + "="*40)
        print("         CLIENTE ENCONTRADO")
        print("="*40)
        print(f"Cédula:      {c['cedula']}")
        print(f"Nombre:      {c['nombre']}")
        print(f"Teléfono:    {c['telefono']}")
        print(f"Tipo:        {c['tipo_cliente']}")
        print(f"Atención:    {c['tipo_atencion']}")
        print(f"Cantidad:    {c['cantidad']}")
        print(f"Prioridad:   {c['prioridad']}")
        print(f"Fecha:       {c['fecha']}")
        print(f"Total:       ${c['total']:,}")
        encontrado = True
        break

if not encontrado:
    print("\nCliente no encontrado.")