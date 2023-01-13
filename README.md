# Asegurarse Software

Puede descargar docker desde el siguiente link: [docker-desktop](https://www.docker.com/products/docker-desktop/)

## Comandos para la ejecucion

Para correr el proyecto ejecute el comando

```shell
 docker-compose -f docker-compose.yml up -d 
```

## Accesos

## Sobre los directorios

En el proyecto se encuentran los siguientes directorios

- app: Incluye todos los archivos para el funcionamiento de la api rest 

## Sobre el desarrollo

## Comandos utiles Docker

```shell
docker build -t api_image .
docker run -d --name api_docker -p 80:80 api_image
```

### Base de datos

```shell
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

Acceder por consola

```shell
docker ps
docker exec -i -t d83c525a65b3  /bin/bash
```

### Consideraciones a tener en cuenta
