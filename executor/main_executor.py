"""This module executes all the commands against the database."""

import sqlite3


DB = sqlite3.connect("database_data/mercearia.db")


def init():
    """Initialize the database with the given SQL script."""
    try:
        DB.executescript(open('database_data/db.sql', 'r', encoding='utf-8').read())
        DB.commit()
        return 1
    except sqlite3.OperationalError:
        return 2
    except:
        return 3

		
def insert(info):
    """Insert formatted query into the database."""
    if info['table'].lower() in ['ano', 'mes']:
        query = 'insert into ' + info['table'] + ' values(' + ','.join(info['values']) + ');'
    else:
        query = 'insert into ' + info['table'] + ' values(null,' + ','.join(info['values']) + ');'

    try:
        DB.executescript(query)
        DB.commit()
        return 1
    except sqlite3.IntegrityError:
        return 2
    except:
        return 3


def drop_all():
    """Drop all tables, DEVELOPMENT ONLY."""
    query = 'drop table if exists compra; ' \
            'drop table if exists venda; ' \
            'drop table if exists mes; ' \
            'drop table if exists ano;'

    try:
        DB.executescript(query)
        DB.commit()
        return True
    except:
        return False


def select_list(info):
    """Select the value from the given table in the given month of the given year."""
    query = "select valor from (?) inner join mes on mes.nome_mes = (?).nome_mes and " \
            "mes.nome_ano = (?).nome_ano inner join ano on ano.nome_ano = mes.nome_ano where " \
            "mes.nome_mes = (?) and ano.nome_ano = (?);"

    cursor = DB.cursor()
    return cursor.execute(
            query, [info['table'], info['table'], info['table'], info['month'], info['year']]
    ).fetchall()


def select_total(info):
    """Select the total of the given table."""
    query = "select sum(valor) from (?) inner join mes on mes.nome_mes = (?).nome_mes and " \
            "mes.nome_ano = (?).nome_ano inner join ano on ano.nome_ano = mes.nome_ano where " \
            "mes.nome_mes = (?)  and ano.nome_ano = (?);"

    cursor = DB.cursor()

    return cursor.execute(
            query, [info['table'], info['table'], info['table'], info['month'], info['year']]
    ).fetchall()[0][0]


def select_profit(info):
    """Return the profit of the given month in the given year."""
    from decimal import Decimal
    from decimal import getcontext

    getcontext().prec = 50

    query_compras = "select sum(valor) from compra inner join mes " \
                    " on mes.nome_mes = compra.nome_mes and mes.nome_ano = compra.nome_ano" \
                    " inner join ano on ano.nome_ano = mes.nome_ano" \
                    " where mes.nome_mes = (?) and ano.nome_ano = (?);"

    query_vendas = "select sum(valor) from venda inner join mes "\
                   " on mes.nome_mes = venda.nome_mes and mes.nome_ano = venda.nome_ano"\
                   " inner join ano on ano.nome_ano = mes.nome_ano" \
                   " where mes.nome_mes = (?) and ano.nome_ano = (?);"

    cursor = DB.cursor()
    try:
        return Decimal(cursor.execute(query_vendas, [info['month'], info['year']]).fetchall()[0][
                           0]) \
               - Decimal(
                cursor.execute(query_compras, [info['month'], info['year']]).fetchall()[0][0])
    except TypeError:
        return -999
    except:
        return 'Erro'


def direct_query(query):
    """Execute a formatted query direct to the database, not recommended."""
    try:
        return DB.cursor().execute(query).fetchall()[0]
    except:
        return 0


def delete_last_insert():
    """Delete the last inserted value."""
    delete_purchase = 'DELETE FROM compra WHERE id = (SELECT MAX(id) FROM compra);'
    delete_sale = 'DELETE FROM venda WHERE id = (SELECT MAX(id) FROM venda);'

    try:
        DB.executescript(delete_purchase)
        DB.executescript(delete_sale)
        return 1
    except:
        return 2


def close():
    """Close the database."""
    DB.close()
