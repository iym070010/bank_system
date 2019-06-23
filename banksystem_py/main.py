#main.py
import MainWindow   #管理界面
import ChuangJian_menu     #发布修改界面
import ChaXun_menu
import ChongZhi_menu
import ZhuanZhang_menu
import DaiKuan_menu
import HuanKuan_menu
import pymysql

import sql;         #自己编写的sql类
import sys;         

from PyQt5 import QtCore, QtGui, QtWidgets;
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv); 
    mMainWindow = QMainWindow (); #实例一个QMainWindow
    ui=MainWindow.Ui_MainWindow(); #这里使用了comments里的Ui_mainWindow类
    ui.setupUi(mMainWindow); #把实例的MainWindow传参进去，进行属性设置..

    mySql = sql.getMySql().connect(); #实例自己编写的sql链接类
    if(mySql):
        mySql.close();
    else:
        QtWidgets.QMessageBox.information(None,"提示:","数据库连接失败，请确定服务器是否开启;"); 

    mMainWindow.show(); 
    sys.exit(app.exec_());