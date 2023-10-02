from os import system
import random
from getPokemonInfo import getPokemonInfo

#-=-=-=-=-=-VARIABLES AND STUFFS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# Define the player's pokedex & pokemons
pokeSlot = []
pokedex = {}

# Define starter for the adventure loop
starter = 0

#-=-=-=-=-=-BAG & POKEDEX FUNCTIONS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# display the status of the pokemon that the player has
def showPokedex(pokemon):
    system("cls")
    if pokemon != {}:
        for i in pokemon:
            print(f"#{i:0>2}")
            for j in getPokemonInfo(i):
                print(f"{j}: {(getPokemonInfo(i)).get(str(j))}")
            print()
    else:
        print("You didn't catch any pokemon yet...")
    system("pause")

# add the pokemons to the pokedex and bag
def addPokemon(pokemon):
    global pokedex
    pokedex[pokemon] = getPokemonInfo(pokemon)
    pokeSlot.append(pokemon)


#-=-=-=-=-=-Biomes Functions-=-=-=-=-=-=-=-=-=-=-=-#

def bag():
    while True:
        system("cls")
        options = int(input("[1] POKEMONS\n[2] ITENS\n[3] EXIT\n"))
        match(options):
            case 1:
                system("cls")
                for i in range(len(pokeSlot)):
                    print(f"#{i+1:0>2}")
                    print(f"{(getPokemonInfo(pokeSlot[i])).get('NAME')}\n")
                system("pause")
                
            case 2:
                print("iten")
            case 3:
                break
            case _:
                system("cls")
                print("INVALID OPTION")



#-=-=-=-=-=-ADVENTURE MODE FUNCTIONS & BIOMES-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# The main loop of the game
def adventureLoop():
    global starter
    system("cls")

    # first pokemon loop
    if starter == 0:
        print("Choose your first pokemon:")
        while True:
            validPokemons = (1,2,3,88226464)
            print(f"[1] Bulbasaur\n[2] Charmander\n[3] Squirtle")
            choose = int(input())
            if choose in validPokemons and choose != 88226464:
                    system("cls")
                    print(f"Congrats, your first pokemon is {(getPokemonInfo(choose).get('NAME'))}")
                    starter = 1
                    addPokemon(choose)
                    break
            elif choose == 88226464:
                    print(f"A wild pokemon appears...\nYou get {(getPokemonInfo(10)).get('NAME')}")
                    starter = 1
                    addPokemon(10)
                    break
            else:
                print("Choose a valid option!")
        system("pause")
    
    # Biomes pickup
    elif len(pokeSlot) < 6:
        forestTypes = ("GRASS", "BUG","WATER", "FIRE", "ELETRIC")
        caveTypes = ("ROCK", "GROUND")
        oceanTypes = ["WATER"]
        while len(pokeSlot) < 6:
            print("Where you want to go?")
            try:
                adLocation = int(input("[1] Forest\n[2] Ocean\n[3] Cave\n[4] Exit\n"))
                match(adLocation):
                    case 1:
                        Biomes(forestTypes)
                    case 2:
                        Biomes(oceanTypes)
                    case 3:
                        Biomes(caveTypes)
                    case 4:
                        break
                    case _:
                        system("cls")
                        print("INVALID OPTION!")
            except ValueError:
                system("cls")
                print("INVALID OPTION!")
            system("cls")
    else:
        print("Your pokemon slots are full!")
        system("pause")


#-=-=-=-=-=-Biomes Functions-=-=-=-=-=-=-=-=-=-=-=-#

# set a list with the pokemons of determined biome
def pokeRandom(pokeBiome):
    pokeList=[]
    for j in range(1, 16):
        res = list(set(pokeBiome).intersection(getPokemonInfo(j).get("TYPE")))
        if res !=[]:
            pokeList.append(j)
    return pokeList

# choose a random pokemon of determined biome
def Biomes(pickedBiome):
    system("cls")
    pokemon = random.choice(pokeRandom(pickedBiome))
    print("A wild pokemon appears...")
    while True:
        addLocalPoke = (str(input(f"Catch {(getPokemonInfo(pokemon)).get('NAME')}?[Y/N] "))).upper()
        match(addLocalPoke):
            case 'Y':
                if random.random() < 0.70:
                    print("WIN")
                    addPokemon(pokemon)
                else:
                    print("LOSE")
                break
            case 'N':
                break
            case _:
                system("cls")
                print("INVALID OPTION!")
    system("pause")


#-=-=-=-=-=-MENU LOOP-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

# Menu loop
print("Welcome to Pokemon in terminal")
while True:
    print("Choose a option!")
    try:
        print("[1] Adventure\n[2] Battle\n[3] Pokedex\n[4] Bag\n[5] Exit")
        choose = int(input())
        match(choose):
            case 1:
                adventureLoop()
            case 2:
                print("BATTLE")
            case 3:
                showPokedex(pokedex)
            case 4:
                bag()
            case 5:
                exit()
            case _:
                system("cls")
                print("INVALID OPTION!")
    except ValueError:
        system("cls")
        print("INVALID OPTION!")
    system("cls")