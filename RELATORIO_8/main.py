from database import Database
from game_database import GameDatabase

db = Database("bolt://3.235.168.48:7687", "neo4j", "badge-aid-strips")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player(1, "João")
game_db.create_player(2, "Maria")
game_db.create_player(3, "José")

game_db.update_player(1, "Pedro")

print("Jogadores:")
print(game_db.get_players())

game_db.create_match(101, [1, 2], {"1": 10, "2": 8})
game_db.create_match(102, [2, 3], {"2": 15, "3": 12})

game_db.update_match_result(101, {"1": 12, "2": 10})

print("Informações da Partida 101:")
print(game_db.get_match(101))

print("Partidas do Jogador 2:")
print(game_db.get_player_matches(2))

game_db.delete_player(3)

game_db.delete_match(102)

db.close()
