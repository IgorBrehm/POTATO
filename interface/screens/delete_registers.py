"""This module contains the components to show the delete screen to the user."""

from PyQt5 import QtCore, QtGui, QtWidgets
from handler import main_handler


class DeleteRegistersScreen(QtWidgets.QWidget):
    """Screen that will show the options to delete register from database."""

    def __init__(self):
        """Constructor."""
        super().__init__()

        # Inputs
        self.to_date = QtWidgets.QCalendarWidget(self)
        self.from_date = QtWidgets.QCalendarWidget(self)

        # Label
        self.label_from_date = QtWidgets.QLabel(self)
        self.label_to_date = QtWidgets.QLabel(self)

        # Buttons
        self.delete = QtWidgets.QPushButton(self)
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
        self.resize(2050, 1119)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Inputs Stylesheet ===============================

        # Calendar that will have the start date of the period
        self.from_date.setGeometry(QtCore.QRect(340, 200, 441, 321))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.from_date.setFont(font)
        self.from_date.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.from_date.setStyleSheet("QCalendarWidget QWidget { \n"
                                     "    alternate-background-color: rgb(222, 222, 222);\n"
                                     "    \n"
                                     "}\n"
                                     "\n"
                                     "QCalendarWidget QToolButton {\n"
                                     "    height: 35px;\n"
                                     "      width: 150px;\n"
                                     "      color: white;\n"
                                     "      font-size: 18px;\n"
                                     "      icon-size: 36px, 36px;\n"
                                     "    icon-color: white;\n"
                                     "      background-color: qlineargradient(x1:0, y1:0, x2:0, "
                                     "y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
                                     "  }\n"
                                     "\n"
                                     "  QCalendarWidget QMenu {\n"
                                     "      width: 150px;\n"
                                     "      left: 20px;\n"
                                     "      color: white;\n"
                                     "      font-size: 18px;\n"
                                     "      background-color: rgb(100, 100, 100);\n"
                                     "  }\n"
                                     "\n"
                                     "  QCalendarWidget QSpinBox { \n"
                                     "      width: 100px; \n"
                                     "      font-size:24px; \n"
                                     "      color: white; \n"
                                     "      background-color: rgb(167, 167, 167);\n"
                                     "      selection-background-color: rgb(136, 136, 136);\n"
                                     "      selection-color: rgb(255, 255, 255);\n"
                                     "  }\n"
                                     "\n"
                                     "QCalendarWidget QAbstractItemView:disabled \n"
                                     "{ \n"
                                     "color: rgb(64, 64, 64); \n"
                                     "}")
        self.from_date.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.from_date.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.from_date.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.from_date.setNavigationBarVisible(True)

        # Calendar that will have the end date of the period
        self.to_date.setGeometry(QtCore.QRect(1110, 200, 431, 311))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.to_date.setFont(font)
        self.to_date.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.to_date.setStyleSheet("QCalendarWidget QWidget { \n"
                                   "    alternate-background-color: rgb(222, 222, 222);\n"
                                   "    \n"
                                   "}\n"
                                   "\n"
                                   "QCalendarWidget QToolButton {\n"
                                   "    height: 35px;\n"
                                   "      width: 150px;\n"
                                   "      color: white;\n"
                                   "      font-size: 18px;\n"
                                   "      icon-size: 36px, 36px;\n"
                                   "    icon-color: white;\n"
                                   "      background-color: qlineargradient(x1:0, y1:0, x2:0, "
                                   "y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
                                   "  }\n"
                                   "\n"
                                   "  QCalendarWidget QMenu {\n"
                                   "      width: 150px;\n"
                                   "      left: 20px;\n"
                                   "      color: white;\n"
                                   "      font-size: 18px;\n"
                                   "      background-color: rgb(100, 100, 100);\n"
                                   "  }\n"
                                   "\n"
                                   "  QCalendarWidget QSpinBox { \n"
                                   "      width: 100px; \n"
                                   "      font-size:24px; \n"
                                   "      color: white; \n"
                                   "      background-color: rgb(167, 167, 167);\n"
                                   "      selection-background-color: rgb(136, 136, 136);\n"
                                   "      selection-color: rgb(255, 255, 255);\n"
                                   "  }")
        self.to_date.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.to_date.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.to_date.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.to_date.setNavigationBarVisible(True)

        # ======================== Label Stylesheet ===============================

        # Label of the calendar containing the start date of the period
        self.label_from_date.setGeometry(QtCore.QRect(310, 150, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_from_date.setFont(font)

        # Label of the calendar containing the end date of the period
        self.label_to_date.setGeometry(QtCore.QRect(1080, 150, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_to_date.setFont(font)

        # ======================== Button Stylesheet ===============================

        # Button to delete the registers
        self.delete.setGeometry(QtCore.QRect(120, 860, 231, 111))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.delete.sizePolicy().hasHeightForWidth())
        self.delete.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.delete.setFont(font)
        self.delete.setStyleSheet("QPushButton\n"
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
                                  "background-color: #ff6b6b;\n"
                                  "color: white;\n"
                                  "font-weight:bold;\n"
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

        # Button to cancel the registration
        self.cancel.setGeometry(QtCore.QRect(420, 860, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton\n"
                                  "{\n"
                                  "  background-color: white;\n"
                                  "  color: black; \n"
                                  "  border: none;\n"
                                  "  margin: 4px 2px;\n"
                                  "  text-align: center;\n"
                                  "  font-size: 24px;\n"
                                  "  border: 2px solid #eb9e02;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover:!pressed\n"
                                  "{\n"
                                  "background-color: #eb9e02;\n"
                                  "color: white;\n"
                                  "font-weight: bold;\n"
                                  "}"
                                  "QPushButton:pressed"
                                  "{"
                                  "background-color: #eb9e02;\n"
                                  "color: white;\n"
                                  "font-weight: bold;\n"
                                  "}")

    def translate_ui(self):
        """Assign names and formats to the components."""
        # Window
        self.setWindowTitle("Dois Irmãos")

        # ======================== Label Stylesheet ===============================

        self.label_from_date.setText(
            "<html><head/><body><p>Selecione o início da data que deve ser "
            "apagada</p><p><br/></p></body></html>"
        )
        self.label_to_date.setText(
            "<html><head/><body><p>Selecione o fim da data que deve ser "
            "apagada</p><p><br/></p></body></html>"
        )

        # ======================== Button Stylesheet ===============================

        self.delete.setText("Apagar Registros")
        self.back.setText("Voltar")
        self.cancel.setText("Cancelar")

    def set_functions(self):
        """Assign functions to the buttons."""
        self.delete.clicked.connect(self.delete_function)
        self.cancel.clicked.connect(self.cancel_function)
        self.back.clicked.connect(self.back_function)

    def delete_function(self):
        """Delete the register from the selected date."""
        start = self.from_date.selectedDate().toString('dd/MM/yyyy')
        end = self.to_date.selectedDate().toString('dd/MM/yyyy')
        self.show_message(main_handler.delete_from_to_period(start, end))

    def cancel_function(self):
        """Restore the deleted register."""
        self.show_message(main_handler.restore_cache())

    def back_function(self):
        """Go back one screen."""
        self.close()

    def show_message(self, message):
        """Show the returned result to the user."""
        message = "\n" + message + "\t\t\n"
        aux = QtWidgets.QMessageBox(self)
        aux.setText(message)
        aux.exec()
