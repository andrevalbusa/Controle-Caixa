
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Layout_Controle_CaixaLrlmuf.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(982, 564)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Left_container = QFrame(self.centralwidget)
        self.Left_container.setObjectName(u"Left_container")
        self.Left_container.setMaximumSize(QSize(200, 16777215))
        self.Left_container.setStyleSheet(u"Qlabel{\n"
"	color: rgb(255,255,255);\n"
"}")
        self.Left_container.setFrameShape(QFrame.StyledPanel)
        self.Left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.Left_container)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label)

        self.Toolbox = QToolBox(self.Left_container)
        self.Toolbox.setObjectName(u"Toolbox")
        self.Toolbox.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setBold(False)
        font.setKerning(False)
        self.Toolbox.setFont(font)
        self.Toolbox.setStyleSheet(u"")
        self.Toolbox.setLineWidth(0)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 180, 444))
        self.menu.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_home = QPushButton(self.menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"\n"
"background-color: rgb(229, 229, 229);")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_despesas = QPushButton(self.menu)
        self.btn_despesas.setObjectName(u"btn_despesas")
        self.btn_despesas.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.verticalLayout_3.addWidget(self.btn_despesas)

        self.btn_receitas = QPushButton(self.menu)
        self.btn_receitas.setObjectName(u"btn_receitas")
        self.btn_receitas.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.verticalLayout_3.addWidget(self.btn_receitas)

        self.btn_consultar = QPushButton(self.menu)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.verticalLayout_3.addWidget(self.btn_consultar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.Toolbox.addItem(self.menu, u" Menu")
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(0, 0, 98, 28))
        self.informacoes = QLabel(self.info)
        self.informacoes.setObjectName(u"informacoes")
        self.informacoes.setGeometry(QRect(10, 30, 161, 361))
        self.Toolbox.addItem(self.info, u"Informa\u00e7\u00f5es")

        self.verticalLayout_2.addWidget(self.Toolbox)


        self.horizontalLayout.addWidget(self.Left_container)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Pages = QStackedWidget(self.frame)
        self.Pages.setObjectName(u"Pages")
        self.pag_despesas = QWidget()
        self.pag_despesas.setObjectName(u"pag_despesas")
        self.horizontalLayout_3 = QHBoxLayout(self.pag_despesas)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(self.pag_despesas)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_boletas = QWidget()
        self.tab_boletas.setObjectName(u"tab_boletas")
        self.gridLayout = QGridLayout(self.tab_boletas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fornecedor = QLineEdit(self.tab_boletas)
        self.fornecedor.setObjectName(u"fornecedor")
        self.fornecedor.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.fornecedor, 6, 0, 1, 3)

        self.label_6 = QLabel(self.tab_boletas)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_boletas)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.btn_extrair = QPushButton(self.tab_boletas)
        self.btn_extrair.setObjectName(u"btn_extrair")
        self.btn_extrair.setMinimumSize(QSize(0, 30))
        self.btn_extrair.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.btn_extrair, 1, 3, 1, 1)

        self.vencimento_boleta = QDateEdit(self.tab_boletas)
        self.vencimento_boleta.setObjectName(u"vencimento_boleta")
        self.vencimento_boleta.setMinimumSize(QSize(0, 30))
        self.vencimento_boleta.setMaximumSize(QSize(120, 16777215))
        self.vencimento_boleta.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout.addWidget(self.vencimento_boleta, 6, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 8, 3, 1, 1)

        self.widget_3 = QWidget(self.tab_boletas)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(30, 60))
        self.widget_3.setMaximumSize(QSize(12551, 60))

        self.gridLayout.addWidget(self.widget_3, 2, 0, 2, 4)

        self.cod_boleta = QLineEdit(self.tab_boletas)
        self.cod_boleta.setObjectName(u"cod_boleta")
        self.cod_boleta.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.cod_boleta, 1, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.label_8 = QLabel(self.tab_boletas)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 3, 1, 1)

        self.btn_adicionar = QPushButton(self.tab_boletas)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.btn_adicionar, 8, 2, 1, 1)

        self.valor_boleta = QLineEdit(self.tab_boletas)
        self.valor_boleta.setObjectName(u"valor_boleta")
        self.valor_boleta.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.valor_boleta, 8, 0, 1, 1)

        self.label_9 = QLabel(self.tab_boletas)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.tabWidget.addTab(self.tab_boletas, "")
        self.tab_outros = QWidget()
        self.tab_outros.setObjectName(u"tab_outros")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_outros)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.tab_outros)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.btn_adicionar_outros = QPushButton(self.frame_3)
        self.btn_adicionar_outros.setObjectName(u"btn_adicionar_outros")
        self.btn_adicionar_outros.setMinimumSize(QSize(100, 30))
        self.btn_adicionar_outros.setMaximumSize(QSize(80, 125))

        self.gridLayout_3.addWidget(self.btn_adicionar_outros, 7, 0, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 7, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 5, 1, 1)

        self.valor_outros = QLineEdit(self.frame_3)
        self.valor_outros.setObjectName(u"valor_outros")
        self.valor_outros.setMinimumSize(QSize(0, 30))
        self.valor_outros.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_3.addWidget(self.valor_outros, 3, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 3, 4, 1, 1)

        self.data_outros = QDateEdit(self.frame_3)
        self.data_outros.setObjectName(u"data_outros")
        self.data_outros.setMinimumSize(QSize(0, 30))
        self.data_outros.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.data_outros, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)

        self.descricao_outros = QLineEdit(self.frame_3)
        self.descricao_outros.setObjectName(u"descricao_outros")
        self.descricao_outros.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.descricao_outros, 1, 0, 1, 4)

        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 3, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_outros, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pag_despesas)
        self.pag_receitas = QWidget()
        self.pag_receitas.setObjectName(u"pag_receitas")
        self.verticalLayout_4 = QVBoxLayout(self.pag_receitas)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.pag_receitas)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.origem_receita = QComboBox(self.pag_receitas)
        self.origem_receita.addItem("")
        self.origem_receita.addItem("")
        self.origem_receita.addItem("")
        self.origem_receita.addItem("")
        self.origem_receita.setObjectName(u"origem_receita")
        self.origem_receita.setMinimumSize(QSize(250, 30))

        self.gridLayout_2.addWidget(self.origem_receita, 1, 0, 1, 1)

        self.valor_receita = QLineEdit(self.pag_receitas)
        self.valor_receita.setObjectName(u"valor_receita")
        self.valor_receita.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.valor_receita, 1, 1, 1, 1)

        self.label_12 = QLabel(self.pag_receitas)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_11 = QLabel(self.pag_receitas)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.data_receita = QDateEdit(self.pag_receitas)
        self.data_receita.setObjectName(u"data_receita")
        self.data_receita.setMinimumSize(QSize(100, 30))
        self.data_receita.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.data_receita, 1, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.pag_receitas)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.label_13 = QLabel(self.pag_receitas)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)

        self.descricao_receita = QTextEdit(self.pag_receitas)
        self.descricao_receita.setObjectName(u"descricao_receita")
        self.descricao_receita.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_4.addWidget(self.descricao_receita)

        self.salvar_receita = QPushButton(self.pag_receitas)
        self.salvar_receita.setObjectName(u"salvar_receita")
        self.salvar_receita.setMinimumSize(QSize(100, 30))

        self.verticalLayout_4.addWidget(self.salvar_receita, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.Pages.addWidget(self.pag_receitas)
        self.pag_consultar = QWidget()
        self.pag_consultar.setObjectName(u"pag_consultar")
        self.horizontalLayout_4 = QHBoxLayout(self.pag_consultar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.pag_consultar)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.calendario_consulta = QCalendarWidget(self.widget)
        self.calendario_consulta.setObjectName(u"calendario_consulta")
        self.calendario_consulta.setGeometry(QRect(20, 10, 256, 190))
        self.btn_buscar = QPushButton(self.widget)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(110, 250, 75, 24))
        self.descricao_consulta = QComboBox(self.widget)
        self.descricao_consulta.addItem("")
        self.descricao_consulta.addItem("")
        self.descricao_consulta.addItem("")
        self.descricao_consulta.addItem("")
        self.descricao_consulta.addItem("")
        self.descricao_consulta.addItem("")
        self.descricao_consulta.setObjectName(u"descricao_consulta")
        self.descricao_consulta.setGeometry(QRect(20, 210, 261, 22))

        self.horizontalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.pag_consultar)
        self.widget_2.setObjectName(u"widget_2")
        self.tabela_consulta = QTableWidget(self.widget_2)
        if (self.tabela_consulta.columnCount() < 4):
            self.tabela_consulta.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_consulta.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_consulta.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_consulta.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_consulta.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_consulta.setObjectName(u"tabela_consulta")
        self.tabela_consulta.setGeometry(QRect(5, 11, 461, 421))

        self.horizontalLayout_4.addWidget(self.widget_2)

        self.Pages.addWidget(self.pag_consultar)
        self.pag_home = QWidget()
        self.pag_home.setObjectName(u"pag_home")
        self.verticalLayout_5 = QVBoxLayout(self.pag_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Dash = QWidget(self.pag_home)
        self.Dash.setObjectName(u"Dash")

        self.verticalLayout_5.addWidget(self.Dash)

        self.Pages.addWidget(self.pag_home)

        self.horizontalLayout_2.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Toolbox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"          Controle Financeiro", None))
#if QT_CONFIG(whatsthis)
        self.Toolbox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_despesas.setText(QCoreApplication.translate("MainWindow", u"Despesas", None))
        self.btn_receitas.setText(QCoreApplication.translate("MainWindow", u"Receitas", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.Toolbox.setItemText(self.Toolbox.indexOf(self.menu), QCoreApplication.translate("MainWindow", u" Menu", None))
        self.informacoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Controle de Contas</span></p><p align=\"center\"><span style=\" font-weight:700;\">Andr\u00e9 Vergilio Valbusa</span></p><p align=\"center\"><span style=\" font-weight:700;\">@andrevalbusa</span></p><p align=\"center\">Descri\u00e7\u00e3o: </p><p align=\"center\">Software de controle de</p><p align=\"center\">contas com interpretador de</p><p align=\"center\">codigo de barras e </p><p align=\"center\">dashboard para </p><p align=\"center\">acompanhamento financeiro.</p></body></html>", None))
        self.Toolbox.setItemText(self.Toolbox.indexOf(self.info), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Codigo de Barras:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.btn_extrair.setText(QCoreApplication.translate("MainWindow", u"Extrair", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Vencimento: </span></p></body></html>", None))
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Valor:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_boletas), QCoreApplication.translate("MainWindow", u"Boletas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.btn_adicionar_outros.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Data:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Valor:</span></p></body></html>", None))
        self.valor_outros.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Hoje", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_outros), QCoreApplication.translate("MainWindow", u"Outros", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Origem:</span></p></body></html>", None))
        self.origem_receita.setItemText(0, QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.origem_receita.setItemText(1, QCoreApplication.translate("MainWindow", u"Farmacia popular", None))
        self.origem_receita.setItemText(2, QCoreApplication.translate("MainWindow", u"Cart\u00e3o", None))
        self.origem_receita.setItemText(3, QCoreApplication.translate("MainWindow", u"Prefeitura", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Data:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Valor:</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Hoje", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Descri\u00e7\u00e3o:</span></p></body></html>", None))
        self.salvar_receita.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.descricao_consulta.setItemText(0, QCoreApplication.translate("MainWindow", u"Panpharma", None))
        self.descricao_consulta.setItemText(1, QCoreApplication.translate("MainWindow", u"Profarma", None))
        self.descricao_consulta.setItemText(2, QCoreApplication.translate("MainWindow", u"Oriente", None))
        self.descricao_consulta.setItemText(3, QCoreApplication.translate("MainWindow", u"Medtem", None))
        self.descricao_consulta.setItemText(4, QCoreApplication.translate("MainWindow", u"Emis Minas", None))
        self.descricao_consulta.setItemText(5, QCoreApplication.translate("MainWindow", u"F&F", None))

        ___qtablewidgetitem = self.tabela_consulta.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem1 = self.tabela_consulta.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem2 = self.tabela_consulta.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem3 = self.tabela_consulta.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cod Barras", None));
    # retranslateUi

