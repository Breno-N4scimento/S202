from database import Database
from writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")
