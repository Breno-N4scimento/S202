from database import Database
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: Database):
        self.database = database

    # EX1
    def totalVendasDia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ]
        return list(self.database.collection.aggregate(pipeline))

    # EX2
    def produtoMaisVendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade_vendida": -1}},
            {"$limit": 1}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        return result[0] if result else {}

    # EX3
    def clienteMaisGastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        result = list(self.database.collection.aggregate(pipeline))
        return result[0] if result else {}

    # EX4
    def vendidosMaisUm(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_vendido": {"$gt": 1}}},
            {"$sort": {"total_vendido": -1}}
        ]
        return list(self.database.collection.aggregate(pipeline))

if __name__ == "__main__":

    db = Database(database="mercado", collection="vendas")
    analyzer = ProductAnalyzer(db)

    # Exemplo 1: Total de vendas por dia
    sales_per_day = analyzer.totalVendasDia()
    writeAJson(sales_per_day, "total_vendas_dia")

    # Exemplo 2: Produto mais vendido
    most_sold_product = analyzer.produtoMaisVendido()
    writeAJson(most_sold_product, "produto_mais_vendido")

    # Exemplo 3: Cliente que mais gastou
    top_spender = analyzer.clienteMaisGastou()
    writeAJson(top_spender, "cliente_mais_gastou")

    # Exemplo 4: Produtos vendidos acima de 1 unidade
    products_more_than_one = analyzer.vendidosMaisUm()
    writeAJson(products_more_than_one, "produtos_vendidos_mais_de_uma_unidade")
