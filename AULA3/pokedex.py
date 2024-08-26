from database import Database
from writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def get_pokemon_by_id(self, pokemon_id: int):
        return self.database.collection.find({"id": pokemon_id})

    def get_pokemon_by_weakness(self, weakness: str):
        return self.database.collection.find({"weaknesses": weakness})

    def get_pokemon_by_spawn_chance(self, min_chance: float, max_chance: float):
        return self.database.collection.find({"spawn_chance": {"$gte": min_chance, "$lte": max_chance}})

    def get_pokemon_with_next_evolution(self):
        return self.database.collection.find({"next_evolution": {"$exists": True, "$ne": None}})

if __name__ == "__main__":
    db = Database(database="pokedex", collection="pokemons")
    pokedex = Pokedex(db)

    #exemplo 1: consultar por ID
    charmander = pokedex.get_pokemon_by_id(4)  # charmander tem ID 4
    writeAJson(charmander, "charmander_id")

    #exemplo 2: consultar por fraqueza (Weakness)
    pokemons_weak_to_water = pokedex.get_pokemon_by_weakness("Water")
    writeAJson(pokemons_weak_to_water, "pokemons_weak_to_water")

    #exemplo 3: consultar por chance de eparição (Spawn Chance)
    pokemons_common = pokedex.get_pokemon_by_spawn_chance(0.5, 1.0)  # pokémons com spawn chance entre 0.5 e 1.0
    writeAJson(pokemons_common, "pokemons_common_spawn_chance")

    #exemplo 4: consultar pokémons com evolução
    pokemons_with_evolution = pokedex.get_pokemon_with_next_evolution()
    writeAJson(pokemons_with_evolution, "pokemons_with_evolution")
