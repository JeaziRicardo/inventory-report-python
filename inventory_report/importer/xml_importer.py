from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path_file):
        if ".xml" in path_file:
            with open(path_file, 'r') as file:
                return xmltodict.parse(file.read())["dataset"]["record"]

        raise ValueError("Arquivo inválido")
