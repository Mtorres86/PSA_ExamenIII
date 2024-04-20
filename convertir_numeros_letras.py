UNIDADES = ['', 'UNO', 'DOS', 'TRES', 'CUATRO', 'CINCO', 'SEIS', 'SIETE', 'OCHO', 'NUEVE']
DECENAS = ['', 'DIEZ', 'VEINTE', 'TREINTA', 'CUARENTA', 'CINCUENTA', 'SESENTA', 'SETENTA', 'OCHENTA', 'NOVENTA']
CENTENAS = ['', 'CIEN', 'DOSCIENTOS', 'TRESCIENTOS', 'CUATROCIENTOS', 'QUINIENTOS', 'SEISCIENTOS', 'SETECIENTOS', 'OCHOCIENTOS', 'NOVECIENTOS']

def convertir_unidades(numero):
    return UNIDADES[numero]

def convertir_decenas(numero):
    if numero < 10:
        return convertir_unidades(numero)
    elif numero == 10:
        return 'DIEZ'
    elif numero < 20:
        return DECENAS[numero % 10] + ' Y'
    else:
        return DECENAS[numero // 10] + ' Y ' + convertir_unidades(numero % 10)

def convertir_centenas(numero):
    if numero == 100:
        return 'CIEN'
    elif numero < 100:
        return convertir_decenas(numero)
    elif numero % 100 == 0:
        return CENTENAS[numero // 100]
    else:
        return CENTENAS[numero // 100] + ' ' + convertir_decenas(numero % 100)

def convertir_miles(numero):
    if numero < 1000:
        return convertir_centenas(numero)
    elif numero % 1000 == 0:
        return convertir_centenas(numero // 1000) + ' MIL'
    else:
        return convertir_centenas(numero // 1000) + ' MIL ' + convertir_centenas(numero % 1000)

def convertir_numero_a_palabras(numero):
    if numero == 0:
        return 'CERO'
    elif numero < 1000:
        return convertir_miles(numero)
    else:
        return 'El número es demasiado grande'

def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero < 0:
            print("Por favor ingrese un número entero positivo.")
            return
        resultado = convertir_numero_a_palabras(numero)
        print("El número", numero, "en palabras es:", resultado)
    except ValueError:
        print("Por favor ingrese un número entero válido.")


if __name__ == "__main__":
    main()

#Intente con una libreria pero me fue dificil, asi que dvide en unidades decenas y centenas,  primero verificamos que el numero sea mayor a 0 si no lo es entonces termina el proceso, PER
#Si lo es entoinces busca el numewro segun la posicion de la unidades decenas y centenas, y una vez lo convierte con la funcion (convertir numero a palabras) lo muestar en pantalla