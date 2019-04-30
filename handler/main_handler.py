"""This module handles all the inputs to send to the database."""

from handler import formatter
from executor import main_executor


def load():
    """Remove the old cache and load the database."""
    try:
        import os
        os.remove('handler/_cache/cache')
    except FileNotFoundError:
        pass
    except:
        return '\nCarregamento falhou\n'

    if main_executor.init() < 3:
        return '\nCarregamento completo!\n'

    return '\nCarregamento falhou\n'


def insert(sales_value, purchases_value):
    """Insert into tables ANO, MES and COMPRA/VENDA values based on insert date and values given."""
    sales_value = str(sales_value).replace(',', '.')
    purchases_value = str(purchases_value).replace(',', '.')

    info = formatter.format_insert(sales_value, purchases_value)

    response_year = main_executor.insert(info['insert_1'])
    response_month = main_executor.insert(info['insert_2'])
    response_sale = main_executor.insert(info['insert_3'])
    response_purchase = main_executor.insert(info['insert_4'])

    if response_year < 3:
        year = info['insert_1']['values'][0]

    else:
        year = -1

    if response_month < 3:
        month = info['insert_2']['values'][0]

    else:
        month = -1

    if response_sale < 3:
        sale = info['insert_3']['values'][0]

    else:
        sale = -1

    if response_purchase < 3:
        purchase = info['insert_4']['values'][0]

    else:
        purchase = -1

    if -1 not in [sale, purchase, month, year]:
        return '\nDados inseridos com sucesso!\n'

    return '\nFalha para inserir os dados.\n'


def delete_last_insert():
    """Remove the last inserted values."""
    cache = open('handler/_cache/cache', 'w', encoding='utf-8')
    query = 'SELECT * FROM venda WHERE id = (SELECT MAX(id) FROM venda);'
    response = main_executor.direct_query(query)
    if response:
        cache.write(' - '.join([str(x) for x in response[1:]]))
        cache.write('\n')
    else:
        return 'Erro'

    query = 'SELECT * FROM compra WHERE id = (SELECT MAX(id) FROM compra);'
    response = main_executor.direct_query(query)
    if response:
        cache.write(' - '.join([str(x) for x in response[1:]]))
        cache.flush()
        cache.close()
    else:
        return 'Erro'

    response = main_executor.delete_last_insert()

    if response == 1:
        return '\nDados apagados com sucesso!\n'

    return '\nFalha para apagar os dados.\n'


def delete_from_to_period(from_date, to_date):
    """Declare future method.

    FOR I IN RANGE(DISTANCE BETWEEN DATES)
        DELETE FROM TABLE VENDA/COMPRA.
    """
    return 'Metodo ainda nao implementado'


def restore_cache():
    """Restore the cache stored from the last insert/delete."""
    try:
        cache = open('handler/_cache/cache', 'r', encoding='utf-8').read().split('\n')
        sales = cache[0].split(' - ')
        purchases = cache[1].split(' - ')

        _cache = open('handler/_cache/cache', 'w', encoding='utf-8')
        _cache.write('\n'.join(cache[2:]))
        _cache.flush()
        _cache.close()

    except FileNotFoundError:
        return '\nDados não puderam ser recuperados.\n'
    except IndexError:
        return '\nNenhum dado foi apagado para poder ser recuperado.\n'

    queries = formatter.format_cache(sales, purchases)
    query_sales = queries['insert_1']
    query_purchases = queries['insert_2']

    if main_executor.insert(query_sales) < 3 and main_executor.insert(query_purchases):
        return '\nDados recuperados com sucesso!\n'

    return '\nFalha na recuperação de dados.\n'


def consult_profit(info=None):
    """Consults the profit of the current month."""
    info = formatter.format_consult(1)

    return formatter.format_number(main_executor.select_profit(info)), info['month'], info['year']


def consult_profit_x_month():
    """Return labels by profits of the last possible months.

    Possible months are: from now, every month in the past 12 months that has any record.
    """
    x_labels = formatter.format_x_labels()
    y_consults = formatter.format_y_consult(x_labels)
    y_labels = []

    for i in y_consults:
        profit = main_executor.select_profit(y_consults[i])
        if profit != -999:
            y_labels.append(profit)
        else:
            break

    if not y_labels:
        return ['Mes\nAno'], ['Lucro'], formatter.format_number(0)

    x_labels = x_labels[:len(y_labels)]
    x_labels.reverse()
    y_labels.reverse()

    return x_labels, y_labels, formatter.format_number(
        sum([float(x) for x in y_labels]) / len(y_labels))


def drop_all():
    """Drop all tables, DEVELOPMENT ONLY."""
    return main_executor.drop_all()


def close():
    """Close the database."""
    main_executor.close()

