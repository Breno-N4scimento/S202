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

# Exemplo de uso
if __name__ == "__main__":
    db = Database(database="pokedex", collection="pokemons")
    pokedex = Pokedex(db)

    # Exemplo 1: Consultar por ID
    charmander = pokedex.get_pokemon_by_id(4)  # Charmander tem ID 4
    writeAJson(charmander, "charmander_id")

    # Exemplo 2: Consultar por Fraqueza (Weakness)
    pokemons_weak_to_water = pokedex.get_pokemon_by_weakness("Water")
    writeAJson(pokemons_weak_to_water, "pokemons_weak_to_water")

    # Exemplo 3: Consultar por Chance de Aparição (Spawn Chance)
    pokemons_common = pokedex.get_pokemon_by_spawn_chance(0.5, 1.0)  # Pokémons com spawn chance entre 0.5 e 1.0
    writeAJson(pokemons_common, "pokemons_common_spawn_chance")

    # Exemplo 4: Consultar Pokémons com Evolução
    pokemons_with_evolution = pokedex.get_pokemon_with_next_evolution()
    writeAJson(pokemons_with_evolution, "pokemons_with_evolution")
