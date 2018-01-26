# Directorio docker

En este directorio se encontrarán definidos los `Dockerfile` que permitirán la creación de las imágenes que se usarán como microservicios.

* Flask

# Flask

Para crear un contenedor con Python y Flask se usará como base el contenedor de Docker creado a partir de este [Dockerfile](https://github.com/frol/docker-alpine-python2/blob/master/Dockerfile).

Para el caso de este proyecto el Dockerfile se llamará `Dockerfile.flaskv2`. La creación del contenedor se hará a través del comando:

```
docker build -f Dockerfile.flaskv2 -t <tutag> .
```

`<tutag>` lo define usted. 
En mi caso es `josanabr/minflask:v2`. 
El `v2` porque hace referencia a Python 2.

## Probando el contenedor

Una vez se tiene creado el contenedor, se puede ejecutar una prueba de la siguiente manera:

```
docker run -p 5000:5000 --rm -v $(pwd):/shared josanabr/minflask:v2 /shared/app.py
```

Se asume que en el sitio donde ejecute el contenedor, se encuentra disponible el archivo `app.py` provisto en este directorio.
