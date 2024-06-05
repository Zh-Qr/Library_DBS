# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_main.ui'
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

class Ui_adminmain(object):
    def setupUi(self, MainWindow,main_window,admin,db):
        self.main_window = main_window
        self.current_window = MainWindow
        self.admin = admin
        self.db = db
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 1097)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(340, 900, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(330, 80, 20, 831))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(330, 70, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1030, 80, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 110, 331, 81))
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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 220, 471, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
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

        #添加联系
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.add_book)
        self.pushButton_4.clicked.connect(self.change)
        self.pushButton_5.clicked.connect(self.lrbook)
        self.pushButton_6.clicked.connect(self.more)

    def more(self):
        from more import Ui_more
        self.more_window = QtWidgets.QMainWindow()
        self.ui = Ui_more()
        self.ui.setupUi(self.more_window,self.current_window,self.admin)
        self.more_window.show()
        self.current_window.close()

    def lrbook(self):
        # 执行SQL查询
        cur = db.cursor()
        get_lrbook_sql = "SELECT * FROM lrbook"
        cur.execute(get_lrbook_sql)
        result = cur.fetchall()
        cur.close()

        from lrbook import Ui_lrbook
        self.lrbook_window = QtWidgets.QMainWindow()
        self.ui = Ui_lrbook()
        self.ui.setupUi(self.lrbook_window,self.current_window,result)
        self.lrbook_window.show()
        self.current_window.close()

    def change(self):
        db.commit()
        from change import Ui_change
        self.change_window = QtWidgets.QMainWindow()
        self.ui = Ui_change()
        self.ui.setupUi(self.change_window,self.current_window)
        self.change_window.show()
        self.current_window.close()

    def add_book(self):
        from add import Ui_addbook
        self.add_window = QtWidgets.QMainWindow()
        self.ui = Ui_addbook()
        self.ui.setupUi(self.add_window,self.current_window,self.admin,self.db)
        self.add_window.show()
        self.current_window.close()

    def search(self):
        result = utils.search_book(db)
        from search import Ui_search
        self.search_window = QtWidgets.QMainWindow()
        self.ui = Ui_search()
        self.ui.setupUi(self.search_window,self.current_window,result)
        self.search_window.show()
        self.current_window.close()

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "管理员操作界面"))
        self.pushButton.setText(_translate("MainWindow", "添加书籍"))
        self.pushButton_4.setText(_translate("MainWindow", "修改书籍信息"))
        self.pushButton_2.setText(_translate("MainWindow", "查询书籍"))
        self.pushButton_5.setText(_translate("MainWindow", "查看借阅表"))
        self.pushButton_6.setText(_translate("MainWindow", "更多"))
        self.pushButton_3.setText(_translate("MainWindow", "返回"))
