def getPokemonInfo(pokemon):
    pokemonStatus = {
        1:{
            "NAME":"BULBASAUR",
            "TYPE":["GRASS","POISON"],
            "HEALTH":45,
            "ABILITIES":"OVERGROW"
        },
        2:{
            "NAME":"CHARMANDER",
            "TYPE":["FIRE"],
            "HEALTH":39,
            "ABILITIES":"BLAZE"
        },
        3:{
            "NAME":"SQUIRTLE",
            "TYPE":["WATER"],
            "HEALTH":44,
            "ABILITIES":"TORRENT"
        
        },
        4:{
            "NAME":"CATERPIE",
            "TYPE":["BUG"],
            "HEALTH":45,
            "ABILITIES":"SHIELD DUST"
        },
        5:{
            "NAME":"WEEDLE",
            "TYPE":["BUG","POISON"],
            "HEALTH":40,
            "ABILITIES":"SHIELD DUST"
        },
        6:{
            "NAME":"PIDGEY",
            "TYPE":["NORMAL","FLYING"],
            "HEALTH":40,
            "ABILITIES":"TANGED FEET"
        },
        7:{
            "NAME":"RATTATA",
            "TYPE":["NORMAL"],
            "HEALTH":30,
            "ABILITIES":"KEEN EYE"
        },
        8:{
            "NAME":"SPEAROW",
            "TYPE":["NORMAL","FLYING"],
            "HEALTH":40,
            "ABILITIES":"KEEN EYE"
        },
        9:{
            "NAME":"EKANS",
            "TYPE":["POISON"],
            "HEALTH":35,
            "ABILITIES":"INTIMIDATE"
        },
        10:{
            "NAME":"PIKACHU",
            "TYPE":["ELETRIC"],
            "HEALTH":35,
            "ABILITIES":"STATIC"
        },
        11:{
            "NAME":"SANDSHREW",
            "TYPE":["GROUND"],
            "HEALTH":35,
            "ABILITIES":"SAND VEIL"
        },
        12:{
            "NAME":"NIDORAN",
            "TYPE":["POISON"],
            "HEALTH":55,
            "ABILITIES":"POISON POINT"
        },
        13:{
            "NAME":"CLEFAIRY",
            "TYPE":["NORMAL"],
            "HEALTH":70,
            "ABILITIES":"CUTE CHARM"
        },
        14:{
            "NAME":"VULPIX",
            "TYPE":["FIRE"],
            "HEALTH":38,
            "ABILITIES":"FLASH FIRE"
        },
        15:{
            "NAME":"JIGLYPUFF",
            "TYPE":["NORMAL"],
            "HEALTH":115,
            "ABILITIES":"CUTE CHARM"
        }
    }
    return pokemonStatus[pokemon]