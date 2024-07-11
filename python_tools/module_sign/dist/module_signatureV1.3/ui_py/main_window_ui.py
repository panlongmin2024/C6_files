from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_py.component import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 700)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Microsoft New Tai Lue")
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.company_name = QLabel(self.centralwidget)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setMinimumSize(QSize(0, 75))
        self.company_name.setFont(font)
        self.company_name.setStyleSheet(u"background-color:#6600FF;\n"
                                        "border-bottom:2px solid black;\n"
                                        "\n"
                                        "\n"
                                        "")
        self.verticalLayout.addWidget(self.company_name)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(25, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Microsoft New Tai Lue")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.sn = QLineEdit(self.widget)
        self.sn.setObjectName(u"sn")
        self.sn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.sn)

        self.test_state = QLabel(self.widget)
        self.test_state.setObjectName(u"test_state")
        self.test_state.setMinimumSize(QSize(250, 0))
        self.test_state.setFont(font1)
        self.test_state.setStyleSheet(u"background-color:#FF9900;\n"
                                      "border:1px solid black;")
        self.test_state.setMargin(0)

        self.horizontalLayout.addWidget(self.test_state)

        self.is_mes = QCheckBox(self.widget)
        self.is_mes.setObjectName(u"is_mes")
        self.is_mes.setFont(font1)

        self.horizontalLayout.addWidget(self.is_mes)
        self.num_widget = StatisticsWidget(self.widget)
        self.horizontalLayout.addWidget(self.num_widget)

        self.setting = QPushButton(self.widget)
        self.setting.setObjectName(u"setting")
        self.setting.setFont(font1)
        self.setting.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.setting)

        self.stop = QPushButton(self.widget)
        self.stop.setObjectName(u"stop")
        font2 = QFont()
        font2.setFamily(u"Microsoft New Tai Lue")
        font2.setBold(False)
        font2.setWeight(50)
        self.stop.setFont(font2)

        self.horizontalLayout.addWidget(self.stop)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.widget)

        self.log = TestLog(self.centralwidget)
        self.log.setObjectName(u"log")
        # self.log.setStyleSheet(u"border-bottom:1px solid black;")
        self.log.setFont(font2)
        self.verticalLayout.addWidget(self.log)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.company_name.setText(QCoreApplication.translate("MainWindow",
                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">World Elite</span></p></body></html>",
                                                             None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SN</p></body></html>",
                                       None))
        self.test_state.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">No testing</span></p></body></html>",
                                                           None))
        self.is_mes.setText(QCoreApplication.translate("MainWindow", u"MES", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))

    # retranslateUi
