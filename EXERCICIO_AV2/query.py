from database import Database

class Query:
    def __init__(self, db):
        self.db = db

    # Questão 01
    def get_teacher_renzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        return self.db.execute_query(query)

    def get_teachers_starting_with_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        return self.db.execute_query(query)

    def get_all_cities(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        return self.db.execute_query(query)

    def get_schools_in_number_range(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
        return self.db.execute_query(query)

    # Questão 02
    def get_oldest_and_youngest_teacher_year(self):
        query = """
        MATCH (t:Teacher)
        RETURN max(t.ano_nasc) AS youngest, min(t.ano_nasc) AS oldest
        """
        return self.db.execute_query(query)

    def get_average_city_population(self):
        query = "MATCH (c:City) RETURN avg(c.population) AS average_population"
        return self.db.execute_query(query)

    def get_city_by_cep(self, cep):
        query = "MATCH (c:City {cep: $cep}) RETURN replace(c.name, 'a', 'A') AS name"
        parameters = {"cep": cep}
        return self.db.execute_query(query, parameters)

    def get_third_char_from_teacher_names(self):
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS third_char"
        return self.db.execute_query(query)
