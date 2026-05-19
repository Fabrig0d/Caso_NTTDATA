import urllib.request
import json

class ServicioPersonas:
    def __init__(self):
        # URL de la API de RandomUser para obtener 10 resultados
        self.url_api = "https://randomuser.me/api/?results=10"

    def obtener_y_limpiar_datos(self):
        try:
            # Conexion de la API y lecura de datos
            print("Conectando con el servicio de datos de RandomUser...")
            with urllib.request.urlopen(self.url_api) as respuesta:
                data_cruda = respuesta.read().decode('utf-8')
            
            # Carga de datos crudos en un diccionario utilizando libreria JSON
            data_diccionario = json.loads(data_cruda)
            lista_personas_cruda = data_diccionario["results"]
            
            personas_limpias = []
            n = 0
            
            # Formateo de cada persona con los campos requeridos y limpieza de datos
            for persona in lista_personas_cruda:
                n += 1
                # Construcción del nombre completo y ubicación completa
                nombre_completo = f"{persona['name']['title']} {persona['name']['first']} {persona['name']['last']}"
                # Construcción de la ubicación completa (ciudad y país)
                ubicacion_completa = f"{persona['location']['city']}, {persona['location']['country']}"
                
                # Formateo de la persona con los campos requeridos y limpieza de datos
                persona_formateada = {
                    "Registro N°": n,
                    "Nombre": nombre_completo,
                    "Género": persona["gender"].capitalize(),
                    "id": persona["id"]["value"],
                    "Ubicación": ubicacion_completa,
                    "Correo electrónico": persona["email"],
                    "Fecha de nacimiento": persona["dob"]["date"][:10],
                    "Fotografía": persona["picture"]["large"]
                }
                
                personas_limpias.append(persona_formateada)

            # Generación del documento JSON con los datos limpios y formateados
            json_final = json.dumps(personas_limpias, indent=4, ensure_ascii=False)
            
            # Guardado del documento JSON en un archivo local
            with open("api_documento.json", "w", encoding="utf-8") as archivo:
                archivo.write(json_final)
            print("Documento  ('api_documento.json') generado con exito")
            
            return json_final

        # Manejo de excepciones para errores de conexión, lectura, procesamiento y escritura
        except Exception as e:
            return json.dumps({"error": f"No se pudo procesar la API debido a: {str(e)}"})

# Instancia del servicio y obtención de datos limpios
procesador = ServicioPersonas()
resultado_api = procesador.obtener_y_limpiar_datos()

# Impresión del resultado final de la API RESTful JSON (entrega backend)
print("\n--- RESPUESTA API RESTFUL JSON (ENTREGA BACKEND) ---")
print(resultado_api)