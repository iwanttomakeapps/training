import random

class Pokemon:
    def __init__(self,name,type,modifiers):
        self.Name = name
        self.type = type
        self.modifiers = modifiers
        self.moves = {}
        self.health = random.randrange(85, 100)

        self.__get_type()
    
    #gets type for pokemon 
    def __get_type(self):
        pokemon_stat_type = {"Fire": { "ember": 5,
                                        "spark": 2,
                                        "lokibreath": 10
                                },
                             "Water":{"watergun": 3,
                                      "spit": 5,
                                      "bubble" : 8
                                }
                             }

        for x in pokemon_stat_type:
            if self.type == x:
                self.moves = pokemon_stat_type[x]
                break

    def attack(self):
        return list(self.moves.values())[random.randrange(0, len(self.moves))]


