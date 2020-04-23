def fizz(num):
    '''
    Comprueba si el numero es múltiplo de 3
    calculando si el resto de número/3 es 0 o no
    '''
    if num % 3 == 0 or "3" in str(num):
        return True
    return False

def buzz(num):
    '''
    Comprueba si el numero es múltiplo de 5
    calculando si el resto de número/5 es 0 o no
    '''
    if num % 5 == 0 or "5" in str(num):
        return True
    return False

def fizz_buzz(num):
    '''
    Comprueba si el numero es múltiplo de 3 y 5 simultáneamente
    calculando si el resto de número/3 es 0 o no, y si el resto de número/5 es 0 o no
    '''
    if fizz(num) and buzz(num):
        return True
    return False

def comprobar_rango(num):
    '''
    Comprueba si el numero cumple los requisitos para devolver Fizz, Buzz, o FizzBuzz
    '''
    if fizz(num):
        return 'Fizz'
    elif buzz(num): 
        return 'Buzz'
    elif fizz_buzz(num):
        return 'Fizz Buzz'
    else:
        return num

def comprobar_numero(num):
    '''
    Comprueba si el numero es un entero
    '''
    if isinstance(num, int):
        return True
    return False

if __name__ == "__main__":
    for num in range(1, 100):
        print(comprobar_rango(num))