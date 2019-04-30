"""This module contains the components to show the register screen to the user."""

from PyQt5 import QtCore, QtGui, QtWidgets
from handler import main_handler


class RegisterValuesScreen(QtWidgets.QWidget):
    """Screen that will show the options to create new registers and saves it."""

    def __init__(self):
        """Constructor."""
        super().__init__()

        # Inputs
        self.sales_text = QtWidgets.QTextEdit(self)
        self.purchases_text = QtWidgets.QTextEdit(self)

        # Label
        self.label_sales_coin = QtWidgets.QLabel(self)
        self.label_purchases = QtWidgets.QLabel(self)
        self.label_sales = QtWidgets.QLabel(self)
        self.label_purchases_coin = QtWidgets.QLabel(self)

        # Buttons
        self.register = QtWidgets.QPushButton(self)
        self.cancel = QtWidgets.QPushButton(self)
        self.back = QtWidgets.QPushButton(self)

        # Initialization
        self.open = None
        self.setup_ui()
        self.translate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components."""
        # Window
        self.resize(2109, 1141)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setStyleSheet("""
                                gridline-color: rgb(192, 255, 231);
                                selection-color: rgb(218, 255, 202);
                                background-color: #ffffff;             
                            """)

        # ======================== Inputs Stylesheet ===============================

        # Entries for the values of sales
        self.sales_text.setGeometry(QtCore.QRect(410, 320, 331, 51))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sales_text.sizePolicy().hasHeightForWidth())
        self.sales_text.setSizePolicy(size_policy)
        self.sales_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sales_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.sales_text.setStyleSheet("""
                            QTextEdit {
                                border-top: 0px solid;
                                border-left: 0px solid;
                                border-right: 0px solid;
                                border-bottom: 1px solid;
                                font-family: "Dubai";
                                font-style: normal;
                                font-size: 18pt;
                            };
                            """)
        self.sales_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sales_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sales_text.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        # Entry to the value of the purchases
        self.purchases_text.setGeometry(QtCore.QRect(1130, 320, 331, 51))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.purchases_text.sizePolicy().hasHeightForWidth())
        self.purchases_text.setSizePolicy(size_policy)
        self.purchases_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.purchases_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.purchases_text.setStyleSheet("""
                                     QTextEdit {
                                         border-top: 0px solid;
                                         border-left: 0px solid;
                                         border-right: 0px solid;
                                         border-bottom: 1px solid;
                                         font-family: "Dubai";
                                         font-size: 18pt;
                                     };
                                        """)
        self.purchases_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.purchases_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.purchases_text.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        # ======================== Labels Stylesheet ===============================

        # Label of the purchases
        self.label_purchases.setGeometry(QtCore.QRect(1060, 220, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_purchases.setFont(font)

        # Label of the purchases with the correct coin
        self.label_purchases_coin.setGeometry(QtCore.QRect(1070, 310, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.label_purchases_coin.setFont(font)

        # Label of the sales
        self.label_sales.setGeometry(QtCore.QRect(330, 220, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_sales.setFont(font)

        # Label to the sales with the correct coin
        self.label_sales_coin.setGeometry(QtCore.QRect(350, 310, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.label_sales_coin.setFont(font)

        # ======================== Buttons Stylesheet ===============================

        # Button to register the data to the database
        self.register.setGeometry(QtCore.QRect(80, 860, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.register.setFont(font)
        self.register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.register.setStyleSheet("QPushButton\n"
                                    "{\n"
                                    "  background-color: white;\n"
                                    "  color: black; \n"
                                    "  margin: 4px 2px;\n"
                                    "  text-align: center;\n"
                                    "  font-size: 24px;\n"
                                    "  border: 2px solid #4CAF50;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover:!pressed\n"
                                    "{\n"
                                    "background-color: #4CAF50;\n"
                                    "color: white;\n"
                                    "font-weight: bold;\n"
                                    "}"
                                    "QPushButton:pressed"
                                    "{"
                                    "background-color: #4CAF50;\n"
                                    "color: white;\n"
                                    "font-weight: bold;\n"
                                    "}")

        # Button to cancel the last register
        self.cancel.setGeometry(QtCore.QRect(420, 860, 231, 111))
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "  background-color: white;\n"
                                  "  color: black; \n"
                                  "  margin: 4px 2px;\n"
                                  "  text-align: center;\n"
                                  "  font-size: 24px;\n"
                                  "  border: 2px solid #ff6b6b;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover:!pressed\n"
                                  "{\n"
                                  "  background-color: #ff6b6b;\n"
                                  "  color: white;\n"
                                  "  font-weight: bold;\n"
                                  "}"
                                  "QPushButton:pressed"
                                  "{"
                                  "background-color: #ff6b6b;\n"
                                  "color: white;\n"
                                  "font-weight: bold;\n"
                                  "}")

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
                                "}")

        self.sales_text.acceptRichText()
        self.purchases_text.acceptRichText()

    def translate_ui(self):
        """Assign names and formats to the components."""
        # Window
        self.setWindowTitle("Dois Irmãos")

        # ======================== Inputs Stylesheet ===============================

        self.sales_text.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Dubai\'; font-size:18pt; "
            "font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
            "font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"
        )

        self.purchases_text.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Dubai\'; font-size:18pt; "
            "font-weight:400; font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
            "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; "
            "font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"
        )

        # ======================== Labels Stylesheet ===============================

        self.label_sales_coin.setText("<html><head/><body><p>R$</p></body></html>")
        self.label_purchases.setText(
            "<html><head/><body><p>Insira o valor <span style=\" "
            "color:#e86464;\">gasto</span> no dia</p></body></html>"
        )
        self.label_sales.setText(
            "<html><head/><body><p>Insira o valor <span style=\" "
            "color:#66bd57;\">ganho</span> no dia</p><p><br/></p></body></html>"
        )
        self.label_purchases_coin.setText("<html><head/><body><p>R$</p></body></html>")

        # ======================== Buttons Stylesheet ===============================

        self.cancel.setText("Cancelar")
        self.back.setText("Voltar")
        self.register.setText("Cadastrar")

    def set_functions(self):
        """Assign functions to the buttons."""
        self.register.clicked.connect(self.register_function)
        self.cancel.clicked.connect(self.cancel_function)
        self.back.clicked.connect(self.back_function)

    def register_function(self):
        """Show the result of the insertion to the user."""
        self.show_message(
            main_handler.insert(self.sales_text.toPlainText(), self.purchases_text.toPlainText()))

    def cancel_function(self):
        """Remove the last inserted register."""
        self.show_message(main_handler.delete_last_insert())

    def back_function(self):
        """Go back one screen."""
        self.close()

    def show_message(self, message):
        """Show the returned result to the user."""
        message = "\n" + message + "\t\t\n"
        aux = QtWidgets.QMessageBox(self)
        aux.setText(message)
        aux.exec()
