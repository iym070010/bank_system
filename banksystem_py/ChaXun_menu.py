# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChaXun_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


class Ui_ChaXun_menu(object):
    def setupUi(self, ChaXun_menu):
        ChaXun_menu.setObjectName("ChaXun_menu")
        ChaXun_menu.resize(610, 451)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ChaXun_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 180, 531, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChaXun_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ChaXun_Hao.setObjectName("ChaXun_Hao")
        self.verticalLayout.addWidget(self.ChaXun_Hao)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_ChaXun = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_ChaXun.setObjectName("Btn_ChaXun")
        self.horizontalLayout.addWidget(self.Btn_ChaXun)

        self.retranslateUi(ChaXun_menu)
        QtCore.QMetaObject.connectSlotsByName(ChaXun_menu)

        self.Btn_ChaXun.clicked.connect(self.__onCommit3)

    def __onCommit3(self):
        try:
            Hao = self.ChaXun_Hao.toPlainText()
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.execute("SELECT balance FROM account WHERE account_number='%s'" % (Hao))
                    result = cur.fetchone()
                    QtWidgets.QMessageBox.about(None, "查询成功", \
                                                "你的账户号是:'%s',余额:'%d'"% (Hao,result[0]))
                except:
                    QtWidgets.QMessageBox.information(None, "提示:", "操作失败;")
                cur.close()
                mySql.commit()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")

    def retranslateUi(self, ChaXun_menu):
        _translate = QtCore.QCoreApplication.translate
        ChaXun_menu.setWindowTitle(_translate("ChaXun_menu", "信息查询"))
        self.ChaXun_Hao.setPlainText(_translate("ChaXun_menu", "输入你的账号"))
        self.Btn_ChaXun.setText(_translate("ChaXun_menu", "确认查询"))
