# Directorio docker

En este directorio se encontrarán definidos los `Dockerfile` que permitirán la creación de las imágenes que se usarán como microservicios.

# Flask

Para crear un contenedor con Flask se usará como base el contenedor de Docker creado por el usuario *nikos* en github. 
[Aquí](https://github.com/nikos/python3-alpine-flask-docker) el repositorio original. 

Para el caso de este proyecto el Dockerfile se llamará `Dockerfile.flask`. La creación del contenedor se hará a través del comando:

```
docker build -f Dockerfile.flask -t <tutag> .
```

`<tutag>` lo define usted. 
En mi caso es `josanabr/minflask`.

## Probando el contenedor

Una vez se tiene creado el contenedor, se puede ejecutar una prueba de la siguiente manera:

```
docker run --rm -v $(pwd):/shared /shared/app.py
```

Se asume que en el sitio donde ejecute el contenedor, se encuentra disponible el archivo `app.py` provisto en este directorio.
