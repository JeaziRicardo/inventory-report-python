from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        simple_report = SimpleReport.generate(products)
        companies = []

        for product in products:
            companies.append(product["nome_da_empresa"])

        companies_counter = Counter(companies)
        products_by_company = ""
        for company, qty in companies_counter.most_common():
            products_by_company += f"- {company}: {qty}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{products_by_company}"
        )
