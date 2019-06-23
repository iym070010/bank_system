# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HuanKuan_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


class Ui_HuanKuan_menu(object):
    def setupUi(self, HuanKuan_menu):
        HuanKuan_menu.setObjectName("HuanKuan_menu")
        HuanKuan_menu.resize(711, 585)
        self.horizontalLayoutWidget = QtWidgets.QWidget(HuanKuan_menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 170, 541, 279))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.HuanKuan_Dai = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.HuanKuan_Dai.setObjectName("HuanKuan_Dai")
        self.verticalLayout.addWidget(self.HuanKuan_Dai)
        self.HuanKuan_JinE = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.HuanKuan_JinE.setObjectName("HuanKuan_JinE")
        self.verticalLayout.addWidget(self.HuanKuan_JinE)
        self.HuanKuan_Hao = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.HuanKuan_Hao.setObjectName("HuanKuan_Hao")
        self.verticalLayout.addWidget(self.HuanKuan_Hao)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Btn_HuanKuan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Btn_HuanKuan.setObjectName("Btn_HuanKuan")
        self.horizontalLayout.addWidget(self.Btn_HuanKuan)

        self.retranslateUi(HuanKuan_menu)
        QtCore.QMetaObject.connectSlotsByName(HuanKuan_menu)

        self.Btn_HuanKuan.clicked.connect(self.__onCommit)

    def __onCommit(self):
        try:
            Hao = self.HuanKuan_Hao.toPlainText()
            Dai = self.HuanKuan_Dai.toPlainText()
            price = int(self.HuanKuan_JinE.toPlainText())
            mySql = sql.getMySql().connect()
            if mySql:
                cur = mySql.cursor()
                try:
                    cur.callproc('HuanQian_02', (Hao, Dai, price,0,0))
                    result = cur.fetchone()
                    QtWidgets.QMessageBox.about(None, "提示:", "你一共还款%s元，还剩%s元未还清" %(result[0],result[1]))
                    mySql.commit()
                except:
                    QtWidgets.QMessageBox.information(None, "提示:", "还款失败")
                    mySql.rollback()
                cur.close()
                mySql.close()
        except:
            QtWidgets.QMessageBox.information(None, "提示:", "操作失败，请检查文本输入是否正确;")


    def retranslateUi(self, HuanKuan_menu):
        _translate = QtCore.QCoreApplication.translate
        HuanKuan_menu.setWindowTitle(_translate("HuanKuan_menu", "账户还款"))
        self.HuanKuan_Dai.setPlainText(_translate("HuanKuan_menu", "输入你的贷款号"))
        self.HuanKuan_JinE.setPlainText(_translate("HuanKuan_menu", "输入你的还款金额"))
        self.HuanKuan_Hao.setPlainText(_translate("HuanKuan_menu", "输入你的还款号\n"
                                                               ""))
        self.Btn_HuanKuan.setText(_translate("HuanKuan_menu", "确认还款"))
