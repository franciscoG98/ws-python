# OPERADORES ARITMETICOS
#  +, -, *, /

# ** POTENCIA
# // raiz

# Operador incemento
edad = 22
edad = edad + 1
# es lo mismo que decir
edad += 1


# OPERADORES CONDICIONALES

# print('10 es MAYOR que 4')
# print( 10 > 4 )

# print('10 es MENOR que 3')
# print( 10 < 3 )

# print('2 es MENOR O IGUAL que 6')
# print( 2 <= 6 )

# print('20 es MAYOR O IGUAL que 6')
# print( 20 >= 6 )

# print('5 es IGUAL que 5')
# print( 5 == 5 )

# print('25 es DISTINTO que 5')
# print( 25 != 5 )


# OPERADORES LOGICOS (and - or - not)

# print(True and True)    # True
# print(True and False)   # False

# print(True or True)    #True
# print(True or False)    #True
# print(False or True)    #True
# print(False or False)    #False

# print(not True)    # False
# print(not False)   # True


# CONDICIONALES ESTRUCTURA IF/ELSE

print('Iniciando el sistema para que ingreses...')


passwd = 'python'
passwdEntered = input('Ingresa tu contraseña:\n')

if passwdEntered == passwd:
    print('La contraseña es correcta, podes entrar capo')
else: 
    print('Quien te conoce papa, tomatela que sos poio')

