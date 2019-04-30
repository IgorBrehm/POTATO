"""This module contains the components to show the profit screen to the user."""

from PyQt5 import QtCore, QtGui, QtWidgets
from handler import main_handler


class ProfitScreen(QtWidgets.QWidget):
    """Screen that will show the profit of the month."""

    def __init__(self):
        """Constructor."""
        super().__init__()

        # Dynamic Text
        self.profit_text = QtWidgets.QLabel(self)

        # Label
        self.profit_label = QtWidgets.QLabel(self)
        self.label_coin = QtWidgets.QLabel(self)

        # Buttons
        self.back = QtWidgets.QPushButton(self)

        # Initializations
        self.open = None
        response = main_handler.consult_profit()
        self.profit = response[0]
        self.custom_label = [response[1], response[2]]
        self.setup_ui()
        self.translate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components."""
        # Window
        self.setWindowOpacity(3.0)
        font = QtGui.QFont()
        font.setFamily('Arial')
        self.setFont(font)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Dynamic Label Stylesheet ===============================

        # Dynamic label containing the year and month requested
        self.profit_text.setGeometry(QtCore.QRect(910, 395, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.profit_text.setFont(font)

        # ======================== Label Stylesheet ===============================

        # Label of the dynamic label
        self.profit_label.setGeometry(QtCore.QRect(690, 130, 761, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(19)
        self.profit_label.setFont(font)

        # Label of the dynamic label with the correct coin
        self.label_coin.setGeometry(QtCore.QRect(840, 400, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(20)
        self.label_coin.setFont(font)

        # ======================== Button Stylesheet ===============================

        # Button to go back one window
        self.back.setGeometry(QtCore.QRect(1550, 860, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
                                "{\n"
                                "  background-color: white;\n"
                                "  color: black; \n"
                                "  border: none;\n"
                                "  margin: 4px 2px;\n"
                                "  text-align: center;\n"
                                "  font-size: 24px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover:!pressed\n"
                                "{\n"
                                "background-color: #989898;\n"
                                "color: white;\n"
                                "font-weight: bold;\n"
                                "}"
                                "QPushButton:pressed"
                                "{"
                                "background-color: #989898;\n"
                                "color: white;\n"
                                "font-weight: bold;\n"
                                "}"
                                )

    def translate_ui(self):
        """Assign names and formats to the components."""
        # Window
        self.setWindowTitle("Dois irmãos")

        # ======================== Dynamic Label Stylesheet ===============================

        self.profit_text.setText(self.profit)

        # ======================== Label Stylesheet ===============================

        self.profit_label.setText(
            "Lucro obtido no mês de " + self.custom_label[0] + " de " + self.custom_label[1])
        self.label_coin.setText("<html><head/><body><p>R$</p></body></html>")

        # ======================== Button Stylesheet ===============================

        self.back.setText("Voltar")

    def set_functions(self):
        """Assign functions to the buttons."""
        self.back.clicked.connect(self.back_function)

    def back_function(self):
        """Go back one screen."""
        self.close()
