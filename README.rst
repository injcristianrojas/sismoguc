SISMO-GUC JSON Data Generator
=============================

Esta bibioteca Python permite a clientes (web, moviles) obtener información
respecto de los más recientes sismos en Chile, monitoreados por el Servicio
Sismológico de la Universidad de Chile. Por razones de robustez, los datos
se obtienen desde la cuenta Twitter del servicio (http://www.twitter.com/sismoguc)
en vez de directamente desde el sitio web del mismo (http://www.sismologia.cl)

Uso
---

Para utilizar la biblioteca desde Python, primero hay que satisfacer los
requisitos de la aplicación. Ésta utiliza los eggs Python:

* Tweepy: API que permite la interacción con Twitter
* ISODate: Biblioteca que permite la transformación rápida desde objetos date/datetime a formato ISO 8601

Para instalarlos, emita el siguiente comando::

   pip install -r requirements.txt

Luego en su código, utilizar::

   from seismo_tweet import jsonize_data
   json = jsonize_data()

El JSON generado incluye una lista en la cual cada item es un diccionario
que contiene los siguientes datos:

- quake_time: Momento de ocurrencia del sismo, en hora UTC, formato ISO 8601
- publication_time: Momento de publicación del reporte en Twitter, en hora UTC, formato ISO 8601
- location: Ubicación aproximada del epicentro
- mag: Magnitud del sismo en escala de Richter
- lat: Latitud del epicentro
- lng: Longitud del epicentro

Dato de ejemplo::

   {
   "publication_time": "2012-03-22T12:37:53Z",
   "location": "15 km al O de Talca",
   "mag": 3.0,
   "lat": -35.477,
   "lng": -71.828,
   "quake_time": "2012-03-22T12:14:15Z"
   }

Aló
