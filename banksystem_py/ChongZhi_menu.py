# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChongZhi_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


class Ui_ChongZhi_menu(object):
    def setupUi(self, ChongZhi_menu):
        ChongZhi_menu.setObjectName("ChongZhi_menu")
        ChongZhi_menu.resize(594, 415)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ChongZhi_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 150, 541, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChongZhi_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ChongZhi_Hao.setObjectName("ChongZhi_Hao")
        self.verticalLayout.addWidget(self.ChongZhi_Hao)
        self.ChongZhi_JinE = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ChongZhi_JinE.setObjectName("ChongZhi_JinE")
        self.verticalLayout.addWidget(self.ChongZhi_JinE)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_ChongZhi = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_ChongZhi.setObjectName("Btn_ChongZhi")
        self.horizontalLayout.addWidget(self.Btn_ChongZhi)

        # self.dialog = ChongZhi_menu;#弹出提示消息

        self.retranslateUi(ChongZhi_menu)
        QtCore.QMetaObject.connectSlotsByName(ChongZhi_menu)

        self.Btn_ChongZhi.clicked.connect(self.__onCommit4)

    def __onCommit4(self):
        try:
            Hao = self.ChongZhi_Hao.toPlainText()
            price = int(self.ChongZhi_JinE.toPlainText())
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.execute("update account set balance=balance+%d WHERE account_number='%s';"% (price, Hao))
                    QtWidgets.QMessageBox.about(None, "提示:","充值成功")
                except:
                    QtWidgets.QMessageBox.information(None, "提示:", "操作失败;")
                cur.close()
                mySql.commit()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")


    def retranslateUi(self, ChongZhi_menu):
        _translate = QtCore.QCoreApplication.translate
        ChongZhi_menu.setWindowTitle(_translate("ChongZhi_menu", "账户充值"))
        self.ChongZhi_Hao.setPlainText(_translate("ChongZhi_menu", "输入你的账户号"))
        self.ChongZhi_JinE.setPlainText(_translate("ChongZhi_menu", "输入你的充值金额\n"
                                                                ""))
        self.Btn_ChongZhi.setText(_translate("ChongZhi_menu", "确认充值"))
