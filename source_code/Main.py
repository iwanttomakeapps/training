import Pokemon
import random


def main():
    Loki = Pokemon.Pokemon("Loki","Water",{})
    
    Brian = Pokemon.Pokemon("Brian","Fire",{})

    pokemon = [Brian, Loki]
    first = pokemon[random.randrange(0,len(pokemon))]
    for x in pokemon:
        if first != x:
            second = x
    while(True):
        firstdamage = first.attack()
        second.health = second.health - firstdamage

        seconddamage = second.attack()
        first.health = first.health - seconddamage
           
        if first.health <= 0:
            print(first.Name + ' died')
            break
        elif second.health <=0:
            print(second.Name + ' died')
            break

if __name__== "__main__":
    main()