import requests

API_KEY = "1eda8dd5-3ccb-4da1-a83b-f87305a941d4"

def obtener_coordenadas(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    
    parametros = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }

    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()

    if len(datos["hits"]) == 0:
        return None

    punto = datos["hits"][0]["point"]

    return punto["lat"], punto["lng"]


def calcular_ruta(origen, destino, vehiculo):

    url = "https://graphhopper.com/api/1/route"

    parametros = {
        "point": [
            f"{origen[0]},{origen[1]}",
            f"{destino[0]},{destino[1]}"
        ],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    respuesta = requests.get(url, params=parametros)

    return respuesta.json()


print("========================================")
print(" CALCULADORA DE RUTAS GRAPHHOPPER")
print("========================================")


while True:

    ciudad_origen = input("\nCiudad de Origen (Chile) o 's' para salir: ")

    if ciudad_origen.lower() == "s":
        print("Programa finalizado.")
        break


    ciudad_destino = input("Ciudad de Destino (Argentina): ")

    transporte = input("Medio de transporte (car, bike o foot): ")


    origen = obtener_coordenadas(ciudad_origen)
    destino = obtener_coordenadas(ciudad_destino)


    if origen is None or destino is None:
        print("No se encontró alguna ciudad.")
        continue


    ruta = calcular_ruta(origen, destino, transporte)


    distancia_km = ruta["paths"][0]["distance"] / 1000
    distancia_millas = distancia_km * 0.621371

    tiempo = ruta["paths"][0]["time"] / 3600000


    print("\n========== RESULTADO ==========")
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Distancia: {distancia_millas:.2f} millas")
    print(f"Duración aproximada: {tiempo:.2f} horas")


    print("\nNarrativa del viaje:")

    for instruccion in ruta["paths"][0]["instructions"]:
        print("-", instruccion["text"])
