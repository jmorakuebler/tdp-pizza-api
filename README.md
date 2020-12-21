# tdp-pizza-api
Proyecto de prueba para aplicar al puesto de programador en Technologies Development Paraguay. El proyecto consiste en una API para una pizzeria.


## Requisitos para la ejecucion del proyecto
* Docker (19.03 o superior)
* Docker Compose (1.26.2 o superior)

## Compilar la imagen del proyecto
* Ejecutar el comando `docker-compose build`

## Iniciar los servicios
* Para iniciar en primer plano: ejecutar el comando `docker-compose up`
* Para iniciar en segundo plano: ejecutar el comando `docker-compose up -d`

## Cargar datos inciales
* Ejecutar el comando `docker-compose run --rm app sh -c "./manage.py loaddata ../initial_data.json"`
* El fixture contiene algunas pizzas e ingredientes creadas, junto con los siguientes usuarios:
  * Usuario `admin`, con la contraseña `pass123456`. Es `staff` y `superusuario`.
  * Usuario `supernotstaff`, con la contraseña `pass123456`. Es `superusuario` pero no `staff`.
  * Usuario `cliente`, con la contraseña `cli123456`. No es `superusuario` ni `staff`.

## Otros comandos de Compose
* Visualizar los logs de la ejecucion en segundo plano: ejecutar el comando `docker-compose logs -f`
* Detener los servicios: `CTRL+C` si esta en primer plano y luego ejecutar el comando `docker-compose down`