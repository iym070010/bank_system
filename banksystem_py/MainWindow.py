# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ChuangJian_menu
import ChaXun_menu
import ChongZhi_menu
import ZhuanZhang_menu
import DaiKuan_menu
import HuanKuan_menu

from PyQt5 import QtCore, QtGui, QtWidgets
import sql
import pymysql
import sys


#这个函数主要是挂载组件与设置属性
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(783, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(90, 100, 631, 421))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DaiKuan = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.DaiKuan.setObjectName("DaiKuan")
        self.verticalLayout_3.addWidget(self.DaiKuan)
        self.HuanKuan = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.HuanKuan.setObjectName("HuanKuan")
        self.verticalLayout_3.addWidget(self.HuanKuan)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChuangJian = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ChuangJian.setObjectName("ChuangJian")
        self.verticalLayout.addWidget(self.ChuangJian)
        self.ChongZhi = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ChongZhi.setObjectName("ChongZhi")
        self.verticalLayout.addWidget(self.ChongZhi)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ChaXun = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ChaXun.setObjectName("ChaXun")
        self.verticalLayout_2.addWidget(self.ChaXun)
        self.ZhuanZhang = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ZhuanZhang.setObjectName("ZhuanZhang")
        self.verticalLayout_2.addWidget(self.ZhuanZhang)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 20, 161, 51))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #点击按钮与对应函数进行链接
        self.ChuangJian.clicked.connect(self.__onChuangJian);#创建账号
        self.ChongZhi.clicked.connect(self.__onChongZhi)#账号充值		
        self.ChaXun.clicked.connect(self.__onChaXun)#账号查询
        self.DaiKuan.clicked.connect(self.__onDaiKuan)
        self.HuanKuan.clicked.connect(self.__onHuanKuan)#账号还款
        self.ZhuanZhang.clicked.connect(self.__onZhuanZhang)#账号转账
	

    def __onChuangJian(self):
        dialog = QtWidgets.QDialog()#先实例一个Dialog对象
        ui = ChuangJian_menu.Ui_ChuangJian_menu();#得到转换的类
        ui.setupUi(dialog)#设置属性 对 这个函数只是单纯的设置属性
        dialog.show()#显示示例的对象
        dialog.exec_()#其他窗口无效但不消失
    def __onChaXun(self):
        dialog = QtWidgets.QDialog()#先实例一个Dialog对象
        ui = ChaXun_menu.Ui_ChaXun_menu();#得到转换的类
        ui.setupUi(dialog)#设置属性 对 这个函数只是单纯的设置属性
        dialog.show()#显示示例的对象
        dialog.exec_()
    def __onChongZhi(self):
        dialog = QtWidgets.QDialog()#先实例一个Dialog对象
        ui = ChongZhi_menu.Ui_ChongZhi_menu();#得到转换的类
        ui.setupUi(dialog)#设置属性 对 这个函数只是单纯的设置属性
        dialog.show()#显示示例的对象
        dialog.exec_()#其他窗口无效但不消失
    def __onZhuanZhang(self):
        dialog = QtWidgets.QDialog()#先实例一个Dialog对象
        ui = ZhuanZhang_menu.Ui_ZhuanZhang_menu();#得到转换的类
        ui.setupUi(dialog)#设置属性 对 这个函数只是单纯的设置属性
        dialog.show()#显示示例的对象
        dialog.exec_()#其他窗口无效但不消失
    def __onDaiKuan(self):
        dialog = QtWidgets.QDialog()#先实例一个Dialog对象
        ui = DaiKuan_menu.Ui_DaiKuan_menu()#得到转换的类
        ui.setupUi(dialog)#设置属性 对 这个函数只是单纯的设置属性
        dialog.show()#显示示例的对象
        dialog.exec_()#其他窗口无效但不消失
    def __onHuanKuan(self):
        dialog = QtWidgets.QDialog();#先实例一个Dialog对象
        ui = HuanKuan_menu.Ui_HuanKuan_menu();#得到转换的类
        ui.setupUi(dialog);#设置属性 对 这个函数只是单纯的设置属性
        dialog.show();#显示示例的对象
        dialog.exec_()#其他窗口无效但不消失

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我是银行"))
        self.DaiKuan.setText(_translate("MainWindow", "账户贷款"))
        self.HuanKuan.setText(_translate("MainWindow", "账户还款"))
        self.ChuangJian.setText(_translate("MainWindow", "创建账户"))
        self.ChongZhi.setText(_translate("MainWindow", "账户充值"))
        self.ChaXun.setText(_translate("MainWindow", "信息查询"))
        self.ZhuanZhang.setText(_translate("MainWindow", "转账操作"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
	"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
	"p, li { white-space: pre-wrap; }\n"
	"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
	"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#55aa7f;\">我是银行</span></p></body></html>"))
	
	

