# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'more.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import utils
import pymysql
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='exp3',
                     charset='utf8')



class Ui_more(object):
    def setupUi(self, MainWindow,main_window,admin):
        self.main_window = main_window
        self.current_window = MainWindow
        self.admin = admin
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 1098)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(300, 910, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 80, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 120, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(290, 90, 20, 831))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(990, 90, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 800, 201, 61))
        self.label_2.setStyleSheet("font: 12pt")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(400, 220, 491, 511))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #建立连接
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.admin_check)
        self.pushButton_5.clicked.connect(self.user_check)
        self.pushButton_6.clicked.connect(self.addall)

    def addall(self):
        from add_all import Ui_addall
        self.addall_window = QtWidgets.QMainWindow()
        self.ui = Ui_addall()
        self.ui.setupUi(self.addall_window,self.current_window,self.admin)
        self.addall_window.show()
        self.current_window.close()


    def user_check(self):
        db.commit()
        cur = db.cursor()
        get_result_sql = "select * from stu_wait"
        cur.execute(get_result_sql)
        result = cur.fetchall()
        cur.close()
        print(result)
        from check_user import Ui_checkuser
        self.user_check_window = QtWidgets.QMainWindow()
        self.ui = Ui_checkuser()
        self.ui.setupUi(self.user_check_window,self.current_window,result)
        self.user_check_window.show()
        self.current_window.close()

    def admin_check(self):
        db.commit()
        cur = db.cursor()
        get_result_sql = "select * from admin_wait"
        cur.execute(get_result_sql)
        result = cur.fetchall()
        cur.close()
        from check_admin import Ui_check_admin
        self.admin_check_window = QtWidgets.QMainWindow()
        self.ui = Ui_check_admin()
        self.ui.setupUi(self.admin_check_window,self.current_window,result)
        self.admin_check_window.show()
        self.current_window.close()

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "更       多"))
        self.label_2.setText(_translate("MainWindow", "更多功能，敬请期待"))
        self.pushButton_4.setText(_translate("MainWindow", "管理员审核"))
        self.pushButton_5.setText(_translate("MainWindow", "用户审核"))
        self.pushButton_6.setText(_translate("MainWindow", "批量导入"))
        self.pushButton_3.setText(_translate("MainWindow", "返回"))
