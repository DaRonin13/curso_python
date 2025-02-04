import random


def dibuja_tablero(simbolos:dict):
    '''
    tablero.py: Dibuja el tablero del juego del gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    '''juega la maquina'''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    '''Juega el usuario''' 
    Lista_numeros = [str(i) for i in range (1,10)]
    ocupado = True
    while ocupado == True:
        x = input('Ingresa el numero de la casilla: ')
        if(x in numeros):
            if simbolos[x] not in ['X', 'O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Número incorrecto')

if __name__ == '__main__':
    numeros = [str(x) for x in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)

    def juego (simbolos:dict):
        '''Juego del gato'''

        lista_6combinaciones = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['1','4','7'],
            ['2','5','8'],
            ['3','6','9'],
        ]

        def checa_winner(simbolos:dict, combinaciones:list):
            '''Checa si hay un ganador'''
            for c in combinaciones:
                if simbolos[c[0]] == simbolos[c[1]] == simbolos [c[2]]:
                    return simbolos[combinacion[0]]
                return None

    '''
    x  = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero[dsimbolos]
    print(numeros)
    '''