from Athlete import athlete
from Sport import Sport

class team:
    '''Clase Team: Representa un equipo de jugadores'''
    def __init__(self, name:str, players:list, sport:Sport) -> None:
        '''Constructor de la clase Team'''
        self.name = name
        self.players = players
        self.sport = sport

    def add_player(self, player:athlete) -> None:
        '''Método para agregar un jugador al equipo'''
        self.players.append(player)

    def __str__(self) -> str:
        '''Método para imprimir el objeto'''
        return f"Team:{self.name}, {self.sport}"

    def __repr__(self) -> str:
        return f"Team(name={self.name}, sport={self.sport})"

    def to_json(self) -> dict:
        '''Método para presentar a la clase como diccionario'''
        return {"name":self.name, "sport":self.sport.to_json(), "players":[x.to_json() for x in self.players]}
    
if __name__ == '__main__':
    a1 = athlete("Jordan")
    a2 = athlete("Johnson")
    a3 = athlete("Pipen")
    a4 = athlete("Bird")
    a5 = athlete("Kobe")
    s = Sport("Basketball", 5, "NBA")
    lakers = team("Lakers",s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))