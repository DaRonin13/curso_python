class Sport:
    '''Clase para representar un deporte
    '''
    def __init__(self, name:str, players:int, league:str):
        """Constructor de sport"""
        self.name = name
        if isinstance(players, int):
            self.players = players
        else:
            self.players = int(players)
        self.league = league

    def __str__(self):
        """Representación en String de sport"""
        return f"Sport('{self.name}', {self.players}, '{self.league}')"
    
    def __repr__(self)->str:
        """Representación en stinr de sport"""
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        """Convertir Sport a JSON"""
        return {
            "name": self.name,
            "players": self.players,
            "league": self.league
        }

if __name__ == '__main__':
    s = Sport('Soccer', 11, 'FIFA')
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = Sport('Football', 11, 'NFL')
    lmp = Sport('Baseball', 9, 'LMP')
    mlb = Sport('Baseball', 9, 'MLB')
    lmx = Sport('Soccer', 11, 'Liga MX')
    nba = Sport('Basketball', 5, 'NBA')
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    archivo_deportes = 'deportes.txt'
    with open(archivo_deportes, 'w') as file:
        for d in lista_deportes:
            file.write(str(d) + '\n')
    sport_list = []
    with open(archivo_deportes, 'r') as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    #Escribiremos en el archivo formato JSON
    print(sport_list[0].to_json())
    import json
    archivo_json = 'deportes.json'
    #convert all sports to json
    sports_json = [s.to_json() for s in sport_list]
    #write the entire list as a single json array
    with open(archivo_json, 'w') as file:
        json.dump(sports_json, file, indent=4)

    #read the json file
    sport_list_json = []
    with open(archivo_json, 'r') as file:
        sport_list_json = json.load(file)
    print(sport_list_json)
