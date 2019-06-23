# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DaiKuan_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


class Ui_DaiKuan_menu(object):
    def setupUi(self, DaiKuan_menu):
        DaiKuan_menu.setObjectName("DaiKuan_menu")
        DaiKuan_menu.resize(504, 417)
        self.horizontalLayoutWidget = QtWidgets.QWidget(DaiKuan_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 401, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.DaiKuan_JinE = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.DaiKuan_JinE.setObjectName("DaiKuan_JinE")
        self.verticalLayout.addWidget(self.DaiKuan_JinE)
        self.DaiKuan_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.DaiKuan_Hao.setObjectName("DaiKuan_Hao")
        self.verticalLayout.addWidget(self.DaiKuan_Hao)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_DaiKuan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_DaiKuan.setObjectName("Btn_DaiKuan")
        self.horizontalLayout.addWidget(self.Btn_DaiKuan)

        self.retranslateUi(DaiKuan_menu)
        QtCore.QMetaObject.connectSlotsByName(DaiKuan_menu)

        self.Btn_DaiKuan.clicked.connect(self.__onCommit)

    def __onCommit(self):
        try:
            price = int(self.DaiKuan_Hao.toPlainText())
            Hao = self.DaiKuan_JinE.toPlainText()
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.execute("insert into loan(loan_number,branch_number,amount,PayOverDate) \
                     values ('%s','Cbank',%d,'0000-00-00 00:00:00')" % (Hao, price))
                    QtWidgets.QMessageBox.about(None, "提示:","贷款成功")#消息盒子必须写出这三个，其他两个可选
                except:
                    QtWidgets.QMessageBox.information(None, "提示:", "操作失败;")
                cur.close()
                mySql.commit()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")


    def retranslateUi(self, DaiKuan_menu):
        _translate = QtCore.QCoreApplication.translate
        DaiKuan_menu.setWindowTitle(_translate("DaiKuan_menu", "账户贷款"))
        self.DaiKuan_JinE.setPlainText(_translate("DaiKuan_menu", "输入你的贷款号"))
        self.DaiKuan_Hao.setPlainText(_translate("DaiKuan_menu", "输入你的贷款金额\n"
                                                             ""))
        self.Btn_DaiKuan.setText(_translate("DaiKuan_menu", "确认贷款"))
