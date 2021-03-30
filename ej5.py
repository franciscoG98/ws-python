# EJERCICIO 5
# Para una liga de futbol solo pueden inscribirse adolescentes entre 12 y 18 años

edad = int( input('Ingresa tu edad:\n') )

if edad <= 18 and edad >= 12:
    print('estas inscripto capo dale corre la bola')
elif edad < 12:
    print('te falta sopita pibe')
elif edad > 18:
    print('esta viejo papaaaaa a vos te parece robarle a los pibes?')
