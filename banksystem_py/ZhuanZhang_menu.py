# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZhuanZhang_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


class Ui_ZhuanZhang_menu(object):
    def setupUi(self, ZhuanZhang_menu):
        ZhuanZhang_menu.setObjectName("ZhuanZhang_menu")
        ZhuanZhang_menu.resize(751, 609)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ZhuanZhang_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 240, 541, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ZhuanZhang_JinE = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ZhuanZhang_JinE.setObjectName("ZhuanZhang_JinE")
        self.verticalLayout.addWidget(self.ZhuanZhang_JinE)
        self.ZhuanZhang_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ZhuanZhang_Hao.setObjectName("ZhuanZhang_Hao")
        self.verticalLayout.addWidget(self.ZhuanZhang_Hao)
        self.ZhuanZhang_DuiFang = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.ZhuanZhang_DuiFang.setObjectName("ZhuanZhang_DuiFang")
        self.verticalLayout.addWidget(self.ZhuanZhang_DuiFang)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_ZhuanZhang = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_ZhuanZhang.setObjectName("Btn_ZhuanZhang")
        self.horizontalLayout.addWidget(self.Btn_ZhuanZhang)

        self.retranslateUi(ZhuanZhang_menu)
        QtCore.QMetaObject.connectSlotsByName(ZhuanZhang_menu)

        self.Btn_ZhuanZhang.clicked.connect(self.__onCommit2)

    def __onCommit2(self):
        try:
            Hao = self.ZhuanZhang_Hao.toPlainText()
            DuiFang = self.ZhuanZhang_DuiFang.toPlainText()
            price = int(self.ZhuanZhang_JinE.toPlainText())
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.callproc('PTransfer', (Hao, DuiFang, price, 0))
                    result = cur.fetchone()
                    QtWidgets.QMessageBox.about(None, "提示:", "转账成功")
                    mySql.commit()
                except:
                    mySql.rollback()
                    QtWidgets.QMessageBox.information(None, "提示:", "转账失败")
                cur.close()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")


    def retranslateUi(self, ZhuanZhang_menu):
        _translate = QtCore.QCoreApplication.translate
        ZhuanZhang_menu.setWindowTitle(_translate("ZhuanZhang_menu", "转账操作"))
        self.ZhuanZhang_JinE.setPlainText(_translate("ZhuanZhang_menu", "请输入转账金额"))
        self.ZhuanZhang_Hao.setPlainText(_translate("ZhuanZhang_menu", "输入你的账号"))
        self.ZhuanZhang_DuiFang.setPlainText(_translate("ZhuanZhang_menu", "输入对方的账号\n"
                                                                       ""))
        self.Btn_ZhuanZhang.setText(_translate("ZhuanZhang_menu", "确认转账"))
