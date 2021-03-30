# EJERCICIO 7 - TAREA
# Crear un sistema de logue donde te pidan que ingreses tu contraseña previamente guardada
# Si la contraseña esta correctamente cargada, el sistema te dará la bienvenida. Si la contraseña es incorecta,
# el  sistema te dira que ingreses nuevamente la contraseña. Tendras hasta tres intentos, si al 3º intento
# no colocas  la contraseña correcta el sistema te informara que ya no tienes mas intentos y que debes aguardar
# 5 horas pàra volver a intentar

print('welcome...')

passwd = 'python'
passwdEntered = input('Ingresa tu contraseña:\n')
i = 1

while i < 3:
    if passwdEntered == passwd:
        print('La contraseña es correcta, podes entrar capo B)')
    else: 
        print('try again')
        passwdEntered = input('Ingresa tu contraseña:\n')
        i += 1

print('Quien te conoce papa, tomatela que sos poio')
