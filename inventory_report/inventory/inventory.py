import csv
import json
import xmltodict
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:

    def report_type(data, type):
        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, type):
        data = []
        with open(path, 'r') as file:
            if ".csv" in path:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            elif ".json" in path:
                data = json.load(file)
            elif ".xml" in path:
                data = xmltodict.parse(file.read())["dataset"]["record"]

        return Inventory.report_type(data, type)
