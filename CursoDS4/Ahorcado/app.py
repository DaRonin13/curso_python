import os
import string
import unicodedata
import argparse
from random import choice

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    #Cargamos las plantillas
    plantilla = fn.carga_plantillas('layout')
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.Obten_Palabras(lista_oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra: letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantilla,o)
        fn.adivina_letra(abcdario,p,adivinadas,o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
    print(f'La palabra era: {p}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ahorcado')
    parser.add_argument('archivo', help='Archivo de texto con palabras', default='./datos/pg15532.txt')
    args = parser.parse_args() 
    archivo = './datos/pg15532.txt'
    if os.stat(archivo) == False:
        print('El archivo no existe')
    main(archivo)