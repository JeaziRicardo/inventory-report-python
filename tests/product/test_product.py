from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Chocolate",
        "Garoto",
        "11/01/2023",
        "11/01/2024",
        99999,
        "abaixo de 8°C",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Chocolate"
    assert product.nome_da_empresa == "Garoto"
    assert product.data_de_fabricacao == "11/01/2023"
    assert product.data_de_validade == "11/01/2024"
    assert product.numero_de_serie == 99999
    assert product.instrucoes_de_armazenamento == "abaixo de 8°C"
