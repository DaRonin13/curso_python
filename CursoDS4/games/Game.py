

from Athlete import athlete
from Sport import Sport
from Team import team
class Game:
    '''Clase Game: Juego entre dos equipos'''
    sports_dict = {
        'LMP': [x for x in range(0, 11)],
        'NBA': [x for x in range(70, 121)],
        'NFL': [x for x in range(3, 56)],
        'LMX': [x for x in range(0, 9)],
        'MLB': [x for x in range(0, 11)],
        'FIFA': [x for x in range(0, 11)],
    }
    def __init__(self, A:team, B:team) -> None:
        '''Constructor de la clase Game'''
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        '''Juego simulado entre equipos'''
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

        
    def __str__(self) -> str:
        '''Método para imprimir el resultado del juego'''
        return f"""Game:{self.A.name}: {self.score[self.A.name]:3d}-{self.B.name}:{self.score[self.B.name]}"""

    def __repr__(self) -> str:
        '''Método para representar el objeto'''
        return f"Game(A={repr(self.A)}, B={repr(self.B)})"
    
    def to_json(self) -> dict:
        '''Método para presentar a la clase como diccionario'''
        return{"A":self.A.to_json(), "B":self.B.to_json(), "score":self.score}

if __name__ == '__main__':
    dt = ['Jordam','Johnson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czak', 'Pfeizer', 'Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("DreamTeam", 5, "NBA")
    t = Team("DreamTeam", players_a, basketball)
    c = Ream("Czeck Repiublic", players_b, basketball)
    game = Game(t, c)
    game.play()
    print(game)
    print(repr(game))
    print("-----")
    print(game.to_json())