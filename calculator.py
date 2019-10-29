def binari(num):
    #convierte el numero a binario
    return int(str(bin(num))[2:])
def decimal_to_bin(num):
    #convierte el numero de binario a decimal
    return int(str(num),2)
def hexadecimal(num):
    #convierte el numero a hexadecimal
    return hex(num)[2:]
def decimal_to_hex(num):
    #convierte el numero de hexadecial a decimal
    return str(int(num,16))
def suma_bin(num1,num2):
    #suma dos binarios
    return binari(num1 + num2)
def resta_bin(num1,num2):
    #resta dos binarios
    x = num1 - num2
    if x<=0:
        print('Número negativo.')
    else:
        return binari(x)   
def multiplicacion_bin(num1, num2):
    #multiplica dos binarios
    return binari(num1 * num2)
def division_bin(num1, num2):
    #divide dos binarios
    return binari(int(num1 / num2))

def suma_hex(num1,num2):
    #suma dos hexadecimales
    return hexadecimal(int(decimal_to_hex(num1)) + int(decimal_to_hex(num2)))
def resta_hex(num1,num2):
    #resta dos hexadecimales
    x = int(decimal_to_hex(num1)) - int(decimal_to_hex(num2))
    if x<=0:
        print('Número negativo.')
    else:
        return hexadecimal(x)
     
def multiplicacion_hex(num1,num2):
    #multiplica dos hexadecimales
    return hexadecimal(int(decimal_to_hex(num1)) * int(decimal_to_hex(num2)))
def division_hex(num1,num2):
    #divide dos hexadecimales
    return hexadecimal(int(int(decimal_to_hex(num1)) / int(decimal_to_hex(num2))))

def math_operation(base_operation):
    #menu para seleccionar tipo de base de las operaciones
    if base_operation==1:
        num_bin1 = int(str(input('\nIngrese número binario 1: ')),2)
        num_bin2 = int(str(input('Ingrese número binario 2: ')),2)
        print('\nSuma: ', suma_bin(num_bin1,num_bin2), '\nResta: ', resta_bin(num_bin1,num_bin2), '\nMultiplicación: ', multiplicacion_bin(num_bin1,num_bin2
        ), '\nDivisión: ', division_bin(num_bin1,num_bin2), '\n')
        pass
    elif base_operation==2:
        num_hex1 = input('\nIngrese número hexadecimal 1: ')
        num_hex2 = input('Ingrese número hexadecimal 2: ')
        print('\nSuma: ', suma_hex(num_hex1,num_hex2), '\nResta: ', resta_hex(num_hex1,num_hex2), '\nMultiplicación: ', multiplicacion_hex(num_hex1,num_hex2
        ), '\nDivisión: ', division_hex(num_hex1,num_hex2), '\n')
        pass
    else:
        print('¡Opción no valida0!')
    return
def menu_operation(num_option):
    if num_option==1:
        #Hace el llamado a las funciones de conversión del binario a decimal y hexadecimal.
        num_bin = int(input('\nIngrese número binario: '))
        print('\n--> BINARIO: ', num_bin, '\n Decimal: ', decimal_to_bin(num_bin), '\n Hexadecimal: ', hexadecimal(int(str(num_bin), 2)), '\n')
        pass
    elif num_option==2:
        #Hace el llamado a las funciones de conversión del decimal a binario y hexadecimal.
        num_dec = int(input('\nIngrese número decimal: '))
        print('\n--> DECIMAL', num_dec, '\n Binario: ', binari(num_dec), '\n Hexadecimal: ', hexadecimal(num_dec), '\n')
        pass
    elif num_option==3:
        #Hace el llamado a las funciones de conversión del hexadecimal a binario y decimal.
        num_hex = input('\nIngrese número hexadecimal: ')
        print('\n--> HEXADECIMAL:', num_hex, '\n Binario: ', binari(int(num_hex,16)), '\n Decimal: ', decimal_to_hex(num_hex), '\n')
        pass
    elif num_option==4:
        base_operation = int(input('\n1. Binarios. \n2. Hexadecimales. \n\nIngrese número de opción: '))
        math_operation(base_operation)
        pass
    else:
        print('¡Opción no valida!')
    return
#Ingresa una opción por consonal.
num_option = int(input('\n\n1. Binario. \n2. Decimal. \n3. Hexadecimal. \n4. Operaciones matematicas. \n\nIngrese número de opción:'))
menu_operation(num_option)
