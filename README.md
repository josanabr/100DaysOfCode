# Desafío 100 días de Codificación

## Día 1
Para una descripción de la motivación para la aplicación de este desafío visitar este [enlace](http://anecdotesofaprofessor.blogspot.com.co/2018/01/desafio-100-dias-de-codificacion.html)

## Día 2
En el segundo día se preparó el contenedor de Flask. 
Más detalles en el directorio [docker](./docker).

## Día 3

En este día se decide investigar sobre mecanismos para validar el ingreso a la plataforma a través de OAuth2. 
OAuth2 es un protocolo de autenticación usado por Google en sus productos centrados en la web.

Se encontraron los siguientes enlaces:

* [flask-oauth2-login](https://github.com/marksteve/flask-oauth2-login) es una librería para el micro-framework que soporta la autenticación usando el login de usuario de la plataforma Google
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* [Add Google Oauth2 login in your flask web app](http://bitwiser.in/2015/09/09/add-google-login-in-flask.html)

Se intentará el último enlace.

## Día 4

En este día se re-estructuró un poco los archivos que estaban en el repositorio para mantener el orden y se comienza a estudiar lo relativo a la persistencia de datos con Flask.
La info usada es la que se encuentra en el capítulo 3 del libro [Flask Framework Cookbook](https://www.packtpub.com/mapt/book/web_development/9781783983407).
