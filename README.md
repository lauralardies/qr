# El QR

Este es el link del [repositorio](https://github.com/lauralardies/qr/tree/main).

### Archivos

Todos los archivos se encuentran en una carpeta llamada `qr`, la cual contiene:
- Una carpeta llamada `img`, donde encontraremos una imagen png que contiene un código QR denominado `flag.png`.
- Un archivo de Python llamado `decodificador.py` en el cual desarrollamos una función que decodifica cualquier mensaje en base64.
- Un archivo de Python llamado `main.py` que contiene el mensaje a decodificar, llama a la función del archivo anterior para decodificarla y muestra la solución en pantalla.
- Un archivo de Python llamado `run.py` que es el lanzador del programa. 

### Tarea

En esta tarea nos propusieron leer un código QR y descubrir el mensaje que escondía. 

### Resolución

Para afrontarnos a este problema hemos hecho uso de la libería `base64`, un módulo integrado que proporciona funciones para codificar y decodificar datos utilizando el esquema Base64. 

Primero hemos escaneado el código QR con nuestros propios dispositivos, lo que nos ha dado una larga cadena de caracteres, que es la que hemos denominado como data en el archivo `main.py`. Una vez obtenido el mensaje a decodificar, comenzamos el proceso. 

Se intenta decodificar los datos en base64 utilizando la función base64.b64decode(data). Luego, el resultado de la decodificación se pasa de nuevo a la función decode recursivamente. Es decir, la función se llama a sí misma con el resultado de la decodificación, de esta manera decodificamos hasta que no haya más datos para decodificar o hasta que se produzca un error. Si se produce un error durante la decodificación (capturado por la cláusula except), la función simplemente devuelve los datos originales sin decodificar (data).

> **¿Por qué hacemos la función recursiva?** Esto nos permite manejar casos en los que el mensaje base64 está codificado múltiples veces, es decir, en donde la decodificación una vez no es suficiente para obtener el mensaje original.

### Ejecución

Para poner en marcha el programa, debes ejecutar el lanzador, es decir, el archivo `run.py`. Hay varias maneras de hacer esto:

1. Puedes ejecutar el código en tu editor de código simplemente dándole al botón Run Python File del archivo `run.py`.
   
2. También puedes ejecutar el siguiente comando en la terminal: 

```
python run.py
```

Hay que tener en cuenta que para que este comando funcione, debes de estar metido en la carpeta qr, que es la que contiene nuestro lanzador `run.py`. Para acceder a la carpeta puedes escribir esto en la terminal:

```
cd qr
```
