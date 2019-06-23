# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChuangJian_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys
import datetime


class Ui_ChuangJian_menu(object):
    def setupUi(self, ChuangJian_menu):
        ChuangJian_menu.setObjectName("ChuangJian_menu")
        ChuangJian_menu.resize(618, 411)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ChuangJian_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 521, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChuangJian_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ChuangJian_Hao.setObjectName("ChuangJian_Hao")
        self.verticalLayout.addWidget(self.ChuangJian_Hao)
        self.ChuangJian_JinE = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ChuangJian_JinE.setObjectName("ChuangJian_JinE")
        self.verticalLayout.addWidget(self.ChuangJian_JinE)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_ChuangJian = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_ChuangJian.setObjectName("Btn_ChuangJian")
        self.horizontalLayout.addWidget(self.Btn_ChuangJian)

        self.retranslateUi(ChuangJian_menu)
        QtCore.QMetaObject.connectSlotsByName(ChuangJian_menu)

        self.Btn_ChuangJian.clicked.connect(self.__onCommit1)

    def __onCommit1(self):
        try:
            Hao = self.ChuangJian_Hao.toPlainText()
            price = int(self.ChuangJian_JinE.toPlainText())
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.execute("insert into account(account_number,balance,Create_time) values('%s','%d','%s')"\
                                %(Hao, price, datetime.datetime.now()));
                    QtWidgets.QMessageBox.about(None, "提示:","创建成功")
                except:
                    QtWidgets.QMessageBox.information(None, "提示:", "操作失败，该账户已存在;")
                cur.close()
                mySql.commit()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")

    def retranslateUi(self, ChuangJian_menu):
        _translate = QtCore.QCoreApplication.translate
        ChuangJian_menu.setWindowTitle(_translate("ChuangJian_menu", "创建账户"))
        self.ChuangJian_Hao.setPlainText(_translate("ChuangJian_menu", "输入你的姓名"))
        self.ChuangJian_JinE.setPlainText(_translate("ChuangJian_menu", "输入你初始金额\n"
                                                                        ""))
        self.Btn_ChuangJian.setText(_translate("ChuangJian_menu", "确认创建"))
