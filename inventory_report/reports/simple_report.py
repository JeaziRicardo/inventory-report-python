from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        earliest_date = None
        closest_expiration_date = None
        companies = []

        for product in products:
            if (
                earliest_date is None
                or product["data_de_fabricacao"] < earliest_date
            ):
                earliest_date = product["data_de_fabricacao"]

            if (
                closest_expiration_date is None
                or product["data_de_validade"] > str(date.today())
                and product["data_de_validade"] < closest_expiration_date
            ):
                closest_expiration_date = product["data_de_validade"]

            companies.append(product['nome_da_empresa'])

        companies_counter = Counter(companies)
        most_products_company = companies_counter.most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {earliest_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {most_products_company}"
        )
