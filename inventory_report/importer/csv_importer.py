from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path_file):
        if ".csv" in path_file:
            with open(path_file, "r") as file:
                return list(csv.DictReader(file))

        raise ValueError("Arquivo inválido")
