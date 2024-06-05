# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrbook.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='exp3',
                     charset='utf8')

class Ui_lrbook(object):
    def setupUi(self, MainWindow, main_window, result):
        self.main_window = main_window
        self.current_window = MainWindow
        self.result = result  # 保存查询结果

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 1094)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(140, 220, 1000, 551))
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 800, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 120, 331, 81))
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

        # 建立联系
        self.pushButton_2.clicked.connect(self.back)

        # 设置模型
        self.model = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model)

        # 初始化表头
        self.model.setHorizontalHeaderLabels(['ID', 'Student ID', 'Book ID', 'Lend Time', 'Return Time'])

        # 显示数据
        self.update_table(result)

    def update_table(self, records):
        self.model.setRowCount(0)  # 清除现有内容
        for record in records:
            items = [QtGui.QStandardItem(str(field)) for field in record]
            self.model.appendRow(items)

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "借阅记录查询"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))

# 在本模块内测试
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()  # 假设这是你的主窗口

    # 执行SQL查询
    cur = db.cursor()
    get_lrbook_sql = "SELECT * FROM lrbook"
    cur.execute(get_lrbook_sql)
    result = cur.fetchall()
    cur.close()

    ui = Ui_lrbook()
    ui.setupUi(MainWindow, main_window, result)
    MainWindow.show()
    sys.exit(app.exec_())
