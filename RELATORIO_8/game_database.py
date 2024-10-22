from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:Player {player_id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {player_id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.player_id AS player_id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"player_id": result["player_id"], "name": result["name"]} for result in results]

    def create_match(self, match_id, player_ids, results):
        query = """
        CREATE (m:Match {match_id: $match_id})
        WITH m
        UNWIND $players AS player
        MATCH (p:Player {player_id: player.player_id})
        CREATE (p)-[:PARTICIPATES]->(m)
        SET m.result = $results
        """
        parameters = {"match_id": match_id, "players": [{"player_id": pid} for pid in player_ids], "results": results}
        self.db.execute_query(query, parameters)

    def update_match_result(self, match_id, results):
        query = "MATCH (m:Match {match_id: $match_id}) SET m.result = $results"
        parameters = {"match_id": match_id, "results": results}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {match_id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def get_match(self, match_id):
        query = """
        MATCH (m:Match {match_id: $match_id})<-[:PARTICIPATES]-(p:Player)
        RETURN m.match_id AS match_id, m.result AS result, collect(p.name) AS players
        """
        results = self.db.execute_query(query, {"match_id": match_id})
        return {"match_id": results[0]["match_id"], "result": results[0]["result"], "players": results[0]["players"]}

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player {player_id: $player_id})-[:PARTICIPATES]->(m:Match)
        RETURN m.match_id AS match_id, m.result AS result
        """
        results = self.db.execute_query(query, {"player_id": player_id})
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]
