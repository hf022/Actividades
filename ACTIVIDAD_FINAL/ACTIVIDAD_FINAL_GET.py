""" 
CODIGO PEDIDOS RAPIDOS

LEER con tranquilidad el enunciado y analizar los pasos lógicos a seguir. Apoyarse en un diagrama de flujo simplificado y luego 
comenzar a desarrollar el código.

En esta actividad final, se debe generar un sistema sencillo de pedidos, que verifique existencias, permita cargar el pedido, 
calcule el total y notifique esos datos vía Telegram. La API a utilizar se encuentra en http://pad19.com:3030, retorna resultados 
en formato JSON, estará habilitada desde el miércoles 08jun2022.

Endpoints de la API:

- http://pad19.com:3030/productos/10: permite obtener el listado de productos disponibles mediante una solicitud GET. Este listado 
indica nombre, precio unitario y unidades en stock de cada producto.

- http://pad19.com:3030/pedidos/10: permite cargar un pedido mediante una solicitud POST. En esta solicitud se debe enviar un JSON 
en el que cada elemento contenga id y cantidad requerida de producto. Precisamente los nombres de los parámetros deben ser "id" y 
"cantidad" (sin las comillas, por supuesto).

Al ejecutar el código, se debe mostrar inicialmente un listado de los productos disponibles, junto a su precio y cantidad, 
formateado de manera amigable. Debajo se debe permitir ingresar código y cantidad de producto, repitiendo todas las veces que se 
desee. Para cerrar el pedido, puede utilizarse por ejemplo el código 0, solicitando confirmación antes de realmente terminar.

Luego se enviará un JSON con el contenido del pedido al endpoint correspondiente. Si el formato del pedido es válido, el endpoint
 responderá con un mensaje favorable y un id de pedido, esto significa que la orden ha quedado registrada bajo ese número.

Se deberá evaluar en el codigo el resultado de la solicitud, y mostrar un mensaje amigable al usuario indicando si todo estuvo 
ok o hubo algún problema.


Consideraciones:

- Atención!: se necesitará un token (credencial) para poder hacer las consultas a la API en pad19.com, deberá enviarse en la misma 
url con el nombre "token" (sin las comillas). Utilizar el siguiente:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8

- El código debe contener la rutina de verificación para determinar si está siendo ejecutado de forma directa o no. De ser así, 
debe comenzar ejecutando una función llamada main().

- La lógica básica que contacta a la API, deberá estar encapsulada en una función, recibiendo como argumento el tipo de conexión 
(GET o POST), el endpoint y un listado de parámetros (solo para POST). La propia función deberá agregar a la consulta el token de
 identificación, enviarla y chequear el status_code del resultado. De ser satisfactorio (200) deberá retornar el contenido en 
 formato JSON, caso contrario retornar falso. Opcionalmente podrán utilizarse otras funciones si se desea.

- El estilo de nomenclatura para variables, funciones y demás elementos, deberá ajustarse a las nuevas convenciones establecidas
 en https://www.python.org/dev/peps/pep-0008/.

- Los parámetros generales (token, url de la API, etc), se deben guardar en archivo de configuración por separado.


"""

import json
import requests
import pprint



TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8"
RUTA = f"http://pad19.com:3030/productos/10?token={TOKEN}"


def main ():

	solicitud = requests.get(RUTA)
	solicitud_json = solicitud.json()
	pprint.pprint(solicitud_json)
	

if (__name__ == "__main__"):
	main() 


