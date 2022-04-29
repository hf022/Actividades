"""
CLASIFICACION PILOTOS FORMULA UNO

Como siempre, recuerden que no es imprescindible completar el ejercicio al 100%, sino tratar de realizar 
el mejor esfuerzo y entender las distintas etapas aunque no se logre completar todas. Fragmenten el enunciado
 paso por paso, y les resultará mucho más limpio ir armando el algoritmo.


Comentarios:

En la siguiente url, se cuenta con datos de la clasificación actualizada de pilotos en la F1:

https://ergast.com/api/f1/2022/driverStandings.json

Recuerden que estos datos se encuentran en formato JSON, puede utilizar cualquier herramienta online 
(como https://jsonbeautifier.org/) para visualizarlos de manera cómoda.


Consignas:

1) Copiar los datos manualmente a un archivo JSON ubicado en el mismo directorio (carpeta) del archivo Python del ejercicio.

2) En el código, realizar lo siguiente:

a) Crear función que recupere los datos desde el archivo local. Se le deberá pasar como parámetro la ruta del archivo, 
y deberá retornar un diccionario con el contenido recuperado (ver ejemplo ya realizado en el repositorio del curso).

4) Recorrer el contenido recuperado y mostrar solamente puntos (points), victorias (wins) y nombre completo 
(familyName y givenName), solo de los 3 primeros pilotos en la clasificación, preferentemente, esta rutina de muestra de 
datos, separarla también en su  propia función.


Atención!:

1) Recordar utilizar el control mediante la macro __name__ para verificar si el código está siendo ejecutado de forma 
directa o insertado en otro, y comenzar el flujo principal de código desde allí.

2) Subir de ser posible el trabajo directamente a su repositorio de Github, para que podamos verlo desde allí.

"""





import json



RUTA = "Actividad_clase_11/driverStandings.json" 

def recuperarConfigJson(direccion):
	archivo = open(direccion, "r") 
	config = json.load(archivo)
	archivo.close()
	return config


def pos1():
    CONFIG = recuperarConfigJson(RUTA)
    print ("PRIMER PUESTO:")
    print("PUNTOS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"]) 
    print("VICTORIAS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["wins"])   
    print("PILOTO:" , CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"] , 
    CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["familyName"])
   
    print ("---------------")

def pos2():
    CONFIG = recuperarConfigJson(RUTA)
    print ("SEGUNDO PUESTO:")
    print("PUNTOS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["points"]) 
    print("VICTORIAS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["wins"])   
    print("PILOTO:" , CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["Driver"]["givenName"] , 
    CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][1]["Driver"]["familyName"])

    print ("---------------")

def pos3():
    CONFIG = recuperarConfigJson(RUTA)
    print ("TERCER PUESTO:")
    print("PUNTOS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["points"]) 
    print("VICTORIAS:", CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["wins"])   
    print("PILOTO:" , CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["Driver"]["givenName"] , 
    CONFIG["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][2]["Driver"]["familyName"])
  


if (__name__ == "__main__"):
	pos1() ,pos2(), pos3()

