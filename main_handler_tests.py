from handler import main_handler


def test_load():
    assert main_handler.load() == '\nCarregamento completo!\n'


def test_insert():
    sales_value = '200'
    purchases_value = '100'
    assert main_handler.insert(sales_value, purchases_value) == '\nDados inseridos com sucesso!\n'


def test_delete_last_insert_fail():
    main_handler.delete_last_insert()
    assert main_handler.delete_last_insert() == 'Erro'


def test_delete_last_insert_success():
    main_handler.insert('100', '100')
    assert main_handler.delete_last_insert() == '\nDados apagados com sucesso!\n'


def test_restore_cache_success():
    assert main_handler.restore_cache() == '\nDados recuperados com sucesso!\n'


def test_restore_cache_fail():
    assert main_handler.restore_cache() == '\nNenhum dado foi apagado para poder ser recuperado.\n'


def test_consult_profit():
    assert main_handler.consult_profit() == ('0,00', '5', '2019')


def test_consult_profit_x_month():
    result = main_handler.consult_profit_x_month()
    month = result[0]
    value = result[2]
    assert month == ['Mai\n2019'] and value == '0,00'


def test_drop_all():
    assert main_handler.drop_all()
