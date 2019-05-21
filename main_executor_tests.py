from executor import main_executor
import sqlite3
import pathlib


def start_fresh_db(func):
    db_path = pathlib.Path(__file__).parent / 'tests' / f'{func}_test_db.db'
    import os
    if os.path.exists(db_path):
        os.remove(db_path)

    sql_path = pathlib.Path(__file__).parent / 'tests' / 'db.sql'
    main_executor.sql_path = sql_path
    main_executor.DB = sqlite3.connect(str(db_path.absolute()))
    main_executor.init()

    return main_executor


def test_init_1():
    db_path = pathlib.Path(__file__).parent / 'test_db.db'

    import os
    if os.path.exists(str(db_path.absolute())):
        os.remove(str(db_path.absolute()))

    main_executor.DB = sqlite3.connect(str(db_path.absolute()))
    assert main_executor.init() == 1


def test_init_2():
    db_path = pathlib.Path(__file__).parent / 'test_db.db'
    import os
    if not os.path.exists(str(db_path.absolute())):
        main_executor.DB = sqlite3.connect(str(db_path.absolute()))
        main_executor.init()

    assert main_executor.init() == 2


def test_init_3():
    db_path = pathlib.Path(__file__).parent / 'tests' / 'test_db.db'
    main_executor.sql_path = 'nothing'

    main_executor.DB = sqlite3.connect(str(db_path.absolute()))
    assert main_executor.init() == 3


def test_insert_1():
    x = start_fresh_db('insert1')

    info = {
        'table': 'ano',
        'values': ['2002']
    }

    assert x.insert(info) == 1


def test_insert_2():
    x = start_fresh_db('insert2')

    info = {
        'table': 'ano',
        'values': ['2002']
    }

    x.insert(info)
    assert x.insert(info) == 2


def test_insert_3():
    x = start_fresh_db('insert3')

    info = {
        'table': 'batata',
        'values': []
    }

    assert x.insert(info) == 3


def test_drop_all_true():
    x = start_fresh_db('dropall')

    assert x.drop_all()


def test_select_list_empty():
    x = start_fresh_db('selectempty')

    info = {
        'table': 'compra',
        'month': '2',
        'year': '2019'
    }

    assert x.select_list(info) == []


def test_select_list_not_empty():
    x = start_fresh_db('selectnotempty')

    info = {
        'table': 'ano',
        'values': ['2019']
    }

    x.insert(info)

    info = {
        'table': 'mes',
        'values': ['2', '2019']
    }

    x.insert(info)

    info = {
        'table': 'compra',
        'values': ['100', '2', '2019']
    }

    x.insert(info)

    info = {
        'table': 'compra',
        'month': '2',
        'year': '2019'
    }

    assert x.select_list(info) == [(100,)]


def test_select_total_empty():
    x = start_fresh_db('selecttotalempty')

    info = {
        'table': 'compra',
        'month': '2',
        'year': '2019'
    }

    assert not x.select_total(info)


def test_select_total_not_empty():
    x = start_fresh_db('selecttotalnotempty')

    info = {
        'table': 'ano',
        'values': ['2019']
    }

    x.insert(info)

    info = {
        'table': 'mes',
        'values': ['2', '2019']
    }

    x.insert(info)

    info = {
        'table': 'compra',
        'values': ['100', '2', '2019']
    }

    x.insert(info)

    info = {
        'table': 'compra',
        'month': '2',
        'year': '2019'
    }

    assert x.select_total(info) == 100


def test_select_profit_empty():
    x = start_fresh_db('selectprofitempty')

    info = {
        'month': '2',
        'year': '2019'
    }

    assert x.select_profit(info) == -999


def test_delete_last_insert1():
    x = start_fresh_db('deletelastinsert1')

    info = {
        'table': 'ano',
        'values': ['2002']
    }

    x.insert(info)
    assert x.delete_last_insert() == 1
