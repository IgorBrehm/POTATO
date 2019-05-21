"""Project developed to manage the profits, expenses and earnings of a store. Lines: 1442."""

import sys
from PyQt5 import QtWidgets
from interface import InitialScreen
from handler import main_handler


def wrapper():
    """
    Wrap others to execute properly.

    Wraps the execution of the program and the function that closes the connection to the database,
    so both will be executed on program exit.
    """
    APP.exec()
    main_handler.close()


if __name__ == '__main__':
    # main_handler.drop_all()
    main_handler.load()

    APP = QtWidgets.QApplication(sys.argv)
    i = InitialScreen()
    i.showFullScreen()
    sys.exit(wrapper())
