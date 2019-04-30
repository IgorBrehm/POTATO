"""This module formats inputs/outputs to properly use them."""

from datetime import datetime
import json


# ================================ Patterns ====================================
# insert       = {'table': table_name, 'values'  : [field1, field2, etc]}
# select list  = {'table': table_name, 'month'   : month_name, 'year': year_name}
# select total = {'table': table_name, 'month'   : month_name, 'year': year_name}
# select lucro = {'month': month_name, 'year'    : year_name}

MONTH_LABELS = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


def format_insert(sales, purchases, month=None, year=None):
    """Format the inputs to use them in a SQL insert command."""
    if not month:
        month = str(datetime.now().month)
    if not year:
        year = str(datetime.now().year)

    info = {
        'insert_1': {
            'table': 'Ano',
            'values': [str(year)]
        },
        'insert_2': {
            'table': 'Mes',
            'values': [str(month), str(year)]
        },
        'insert_3': {
            'table': 'Compra',
            'values': [str(purchases), str(month), str(year)]
        },
        'insert_4': {
            'table': 'Venda',
            'values': [str(sales), str(month), str(year)]
        }
    }

    return info


def format_cache(sales, purchases):
    """Format the inputs to use them as two SQL insert commands.

    The first command will insert in the table 'Compra'
    The second command will insert in the table 'Venda'

    It is useful to restore a cache where the tables 'Ano' and 'Mes' already have the value
    registered.
    """
    info = {
        'insert_1': {
            'table': 'Compra',
            'values': [purchases[0], purchases[1], purchases[2]]
        },
        'insert_2': {
            'table': 'Venda',
            'values': [sales[0], sales[1], sales[2]]
        }
    }

    return info


def format_consult(profit, table=None):
    """Format the inputs to use them as SQL select command."""
    if profit:
        info = {
            'month': str(datetime.now().month),
            'year': str(datetime.now().year)
        }

    else:
        info = {
            'table': table,
            'month': str(datetime.now().month),
            'year': str(datetime.now().year)
        }

    return info


def format_x_labels():
    """Return the last 12 months from now concatenated with the correct year in descending order."""
    current_month = datetime.now().month
    current_year = datetime.now().year

    months = []

    for _ in range(12):
        label = MONTH_LABELS[current_month - 1] + '\n' + str(current_year)
        months.append(label)

        if current_month - 1 == 0:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1

    return months


def format_y_consult(x_labels):
    """Format as many consults as x_labels.

    Each consult will get the values of month and year possible
    Possible months are: from now, every month in the past 12 months that has any record.
    """
    # Get all the indexes of months
    months = [MONTH_LABELS.index(x_label.split('\n')[0]) + 1 for x_label in x_labels]

    # Get the possible years (cannot be more than two years since the limit of time is 12 months)
    years = list((x_labels[0].split('\n')[1], x_labels[-1].split('\n')[1]))

    query = "{"

    for i in range(12):
        if months[i] == 12:
            years.pop()

        query += "\"consult_" + str(i + 1) + "\":"
        query += "{\"month\":\"" + str(months[i]) + "\","
        query += "\"year\":\"" + str(years[0]) + "\"},"

    query = query[:-1]
    query += "}"

    return json.loads(query)


def format_number(number):
    """Format the number to show as R$ 100.000,00."""
    coins = str(0)
    number = str(number)
    try:
        decimals = list(number.split('.')[0])
        coins = number.split('.')[1]
    except:
        decimals = list(str(number))

    formatted_number = []

    # If it is necessary to add . separating the thousands
    if len(decimals) > 3:
        decimals.reverse()
        for i, _ in enumerate(decimals):
            if i % 3 == 0 and i != 0:
                formatted_number.append('.')
            formatted_number.append(decimals[i])
        formatted_number.reverse()
    else:
        formatted_number.extend(decimals)

    # If any coin were caught
    if coins:
        # Format to a minimum of two decimals
        if len(coins) == 1:
            coins += str(0)
        formatted_number.append(',')
        formatted_number.append(coins)
    else:
        formatted_number.append(',00')

    return ''.join(formatted_number)
