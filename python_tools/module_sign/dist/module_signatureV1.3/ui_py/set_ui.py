# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mes_configlXvkgc.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 430)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tenant_id = QLineEdit(Dialog)
        self.tenant_id.setObjectName(u"tenant_id")

        self.gridLayout.addWidget(self.tenant_id, 1, 1, 1, 1)

        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.scope = QLineEdit(Dialog)
        self.scope.setObjectName(u"scope")

        self.gridLayout.addWidget(self.scope, 3, 1, 1, 1)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)

        self.machineCode = QLineEdit(Dialog)
        self.machineCode.setObjectName(u"machineCode")

        self.gridLayout.addWidget(self.machineCode, 5, 3, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.grant_type = QLineEdit(Dialog)
        self.grant_type.setObjectName(u"grant_type")

        self.gridLayout.addWidget(self.grant_type, 2, 3, 1, 1)

        self.typing = QLineEdit(Dialog)
        self.typing.setObjectName(u"typing")

        self.gridLayout.addWidget(self.typing, 3, 3, 1, 1)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.Authorization = QLineEdit(Dialog)
        self.Authorization.setObjectName(u"Authorization")

        self.gridLayout.addWidget(self.Authorization, 0, 3, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 1, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.stationCode = QLineEdit(Dialog)
        self.stationCode.setObjectName(u"stationCode")

        self.gridLayout.addWidget(self.stationCode, 4, 3, 1, 1)

        self.workOrderNo = QLineEdit(Dialog)
        self.workOrderNo.setObjectName(u"workOrderNo")

        self.gridLayout.addWidget(self.workOrderNo, 4, 1, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.routeCode = QLineEdit(Dialog)
        self.routeCode.setObjectName(u"routeCode")

        self.gridLayout.addWidget(self.routeCode, 5, 1, 1, 1)

        self.web_url = QLineEdit(Dialog)
        self.web_url.setObjectName(u"web_url")

        self.gridLayout.addWidget(self.web_url, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.pi_url = QLineEdit(Dialog)
        self.pi_url.setObjectName(u"pi_url")

        self.horizontalLayout_2.addWidget(self.pi_url)

        self.cert_layout = QHBoxLayout()
        self.cert_layout.setObjectName(u"cert_layout")

        self.cert_label = QLabel(Dialog)
        self.cert_label.setObjectName("cert_label")
        self.cert_label.setText("证书路径")
        self.cert_layout.addWidget(self.cert_label)

        self.cert_path = QLineEdit(Dialog)
        self.cert_path.setObjectName("cert_path")
        self.cert_layout.addWidget(self.cert_path)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.cert_layout)
        self.cert_gridLayout = QGridLayout(Dialog)
        self.cert_gridLayout.setObjectName(u"gridLayout")
        self.cert_gridLayout.setContentsMargins(0, 0, 0, 0)

        self.cert_label_3 = QLabel(Dialog)
        self.cert_label_3.setObjectName(u"cert_label_3")
        self.cert_label_3.setText('用户名：')
        self.cert_gridLayout.addWidget(self.cert_label_3, 0, 0, 1, 1)

        self.pi_user_name = QLineEdit(Dialog)
        self.pi_user_name.setObjectName(u"pi_user_name")

        self.cert_gridLayout.addWidget(self.pi_user_name, 0, 1, 1, 1)

        self.cert_label = QLabel(Dialog)
        self.cert_label.setObjectName(u"cert_label")
        self.cert_label.setText("密码：")
        self.cert_gridLayout.addWidget(self.cert_label, 1, 0, 1, 1)

        self.pi_password = QLineEdit(Dialog)
        self.pi_password.setObjectName(u"pi_password")

        self.cert_gridLayout.addWidget(self.pi_password, 1, 1, 1, 1)

        self.cert_label_2 = QLabel(Dialog)
        self.cert_label_2.setObjectName(u"lcert_abel_2")
        self.cert_label_2.setText('模块名：')
        self.cert_gridLayout.addWidget(self.cert_label_2, 2, 0, 1, 1)

        self.product_model_name = QLineEdit(Dialog)
        self.product_model_name.setObjectName(u"product_model_name")

        self.cert_gridLayout.addWidget(self.product_model_name, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.cert_gridLayout)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.sn_length = QSpinBox(Dialog)
        self.sn_length.setObjectName(u"sn_length")

        self.horizontalLayout_3.addWidget(self.sn_length)

        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_3.addWidget(self.label_18)

        self.delay = QDoubleSpinBox(Dialog)
        self.delay.setObjectName(u"delay")

        self.horizontalLayout_3.addWidget(self.delay)

        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_3.addWidget(self.label_19)

        self.port = QComboBox(Dialog)
        self.port.setObjectName(u"port")

        self.horizontalLayout_3.addWidget(self.port)

        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_3.addWidget(self.label_20)

        self.baud = QSpinBox(Dialog)
        self.baud.setObjectName(u"baud")
        self.baud.setMaximum(999999)

        self.horizontalLayout_3.addWidget(self.baud)

        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_3.addWidget(self.label_21)

        self.stop_bit = QSpinBox(Dialog)
        self.stop_bit.setObjectName(u"stop_bit")

        self.horizontalLayout_3.addWidget(self.stop_bit)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_font_set = QFrame(Dialog)
        self.line_font_set.setObjectName(u"line_3")
        self.line_font_set.setFrameShape(QFrame.HLine)
        self.line_font_set.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.line_font_set)
        self.font_set_label = QLabel(Dialog)
        self.font_set_label.setText("界面设置")
        self.verticalLayout.addWidget(self.font_set_label)
        # 标题layout
        self.titlelayout = QHBoxLayout()

        self.title_label = QLabel(Dialog)
        self.title_label.setText('Window title')
        self.titlelayout.addWidget(self.title_label)

        self.title_line = QLineEdit(Dialog)
        self.title_line.setObjectName("title_line")
        self.titlelayout.addWidget(self.title_line)

        self.company_label = QLabel(Dialog)
        self.company_label.setText('公司名')

        self.titlelayout.addWidget(self.company_label)

        self.company_line = QLineEdit(Dialog)
        self.company_line.setObjectName("company_line")
        self.titlelayout.addWidget(self.company_line)
        self.verticalLayout.addLayout(self.titlelayout)

        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"confirm")

        self.horizontalLayout.addWidget(self.confirm)

        self.resect = QPushButton(Dialog)
        self.resect.setObjectName(u"resect")

        self.horizontalLayout.addWidget(self.resect)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate(
            "Dialog", u"MES\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate(
            "Dialog", u"\u5de5\u5355\u53f7\uff1a", None))
        self.label_10.setText(QCoreApplication.translate(
            "Dialog", u"\u7c7b\u578b\uff1a", None))
        self.label_11.setText(QCoreApplication.translate(
            "Dialog", u"\u5de5\u4f4d\u7f16\u53f7\uff1a", None))
        self.label_4.setText(QCoreApplication.translate(
            "Dialog", u"\u5de5\u5e8f\u7f16\u53f7\uff1a", None))
        self.label_8.setText(QCoreApplication.translate(
            "Dialog", u"\u8d26\u53f7\uff1a", None))
        self.label_12.setText(QCoreApplication.translate(
            "Dialog", u"\u8bbe\u5907\u7f16\u53f7\uff1a", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"\u5bc6\u7801:", None))
        self.label_5.setText(QCoreApplication.translate(
            "Dialog", u"\u6388\u6743\u7801\uff1a", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"\u8303\u56f4\uff1a", None))
        self.label_9.setText(QCoreApplication.translate(
            "Dialog", u"\u6388\u6743\u65b9\u5f0f\uff1a", None))
        self.label_6.setText(QCoreApplication.translate(
            "Dialog", u"ip\u5730\u5740\uff1a", None))
        self.label_7.setText(QCoreApplication.translate(
            "Dialog", u"\u79df\u6237\uff1a", None))
        self.label_14.setText(QCoreApplication.translate(
            "Dialog", u"\u6811\u8393\u6d3e\u8bbe\u7f6e", None))
        self.label_15.setText(QCoreApplication.translate(
            "Dialog", u"ip\u5730\u5740\uff1a", None))
        self.label_16.setText(QCoreApplication.translate(
            "Dialog", u"\u6d4b\u8bd5\u8bbe\u7f6e", None))
        self.label_17.setText(QCoreApplication.translate(
            "Dialog", u"sn\u7801\u957f\u5ea6\uff1a", None))
        self.label_18.setText(QCoreApplication.translate(
            "Dialog", u"\u6d4b\u8bd5\u5ef6\u65f6\uff1a", None))
        self.label_19.setText(QCoreApplication.translate(
            "Dialog", u"\u4e32\u53e3\uff1a", None))
        self.label_20.setText(QCoreApplication.translate(
            "Dialog", u"\u6ce2\u7279\u7387\uff1a", None))
        self.label_21.setText(QCoreApplication.translate(
            "Dialog", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.confirm.setText(QCoreApplication.translate(
            "Dialog", u"\u786e\u5b9a", None))
        self.resect.setText(QCoreApplication.translate(
            "Dialog", u"\u91cd\u7f6e", None))
    # retranslateUi
