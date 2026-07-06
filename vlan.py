print("===================================")
print(" CLASIFICACIÓN DE VLAN")
print("===================================")

vlan = input("Ingrese el número de VLAN (o 's' para salir): ")

if vlan.lower() == "s":
    print("Programa finalizado.")
else:
    vlan = int(vlan)

    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} corresponde al rango NORMAL.")

    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} corresponde al rango EXTENDIDO.")

    else:
        print("Número de VLAN no válido.")
