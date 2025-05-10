'''Programa principal de games'''
from Athlete import athlete
from Sport import Sport
from Team import team
from Game import Game
import json

def main(archivo_torneo:str):
    '''Función principal de games'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r", encoding="UTF8") as f:
            torneo = json.load(archivo_torneo)
    else:
        players_mexico = ['Chicharito','Chucky','Ochoa','Guardado','Herrera','Jimenez','Tecatito','Gallardo','Salcedo','Moreno','Layun']
        players_españa = ['Ramos','Iniesta','Casillas','Xavi','Torres','Villa','Pique','Alba','Busquets','Pedro','Silva']
        lista_mexico = [athlete(x) for x in players_mexico]
        lista_españa = [athlete(x) for x in players_españa]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = team("Mexico", soccer, lista_mexico)
        españa = team("España", soccer, lista_españa)
        juego = Game(mexico, españa)
        torneo = [juego.to_json()]
        archivo = "torneo.json"
        with open(archivo, "w", encoding="UTF8") as f:
            json.dump(torneo, f, ensure_ascii=False ,indent=4)
        print(f"Se escribió el archivo {archivo} Satistactoriamente")