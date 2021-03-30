# EJERCICIO 4
# Crear un programa que le de la bienvenida a un usuario y le informe que podra calcular la distancia entre
# buenos aires y bariloche. Distancia entre bs as y brc 1593 km

name = input('Ingresa tu nombre:\n')
print('bienvenido ' + name)

km = int(input('Ingresa la distancia que quieres recorrer en kilometros:\n'))
speed = int(input('Ingresa la velocidad promedio:\n'))

time = km / speed
print(name + ' vas a tardar ' + str(time) + ' horas en llegar a tu destino')

