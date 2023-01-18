from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path_file):
        if ".json" in path_file:
            with open(path_file, 'r') as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")
