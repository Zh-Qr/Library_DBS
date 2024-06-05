# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'return.ui'
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


class Ui_return_book(object):
    def setupUi(self, MainWindow, main_window, stu_id, username, password):
        self.main_window = main_window
        self.current_window = MainWindow
        self.stu_id = stu_id
        self.username = username
        self.password = password
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 1097)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(800, 900, 421, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(770, 210, 16, 551))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(850, 340, 321, 41))
        self.lineEdit_2.setStyleSheet("font: 15pt")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 480, 281, 61))
        self.label_3.setStyleSheet("font: 12pt")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 780, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 110, 331, 81))
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
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(100, 900, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 80, 20, 831))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(790, 80, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(150, 210, 631, 661))
        self.tableView.setObjectName("tableView")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 780, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 120, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1200, 80, 20, 831))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 70, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(790, 70, 421, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        # 添加 no_books_label 标签
        self.no_books_label = QtWidgets.QLabel(self.centralwidget)
        self.no_books_label.setGeometry(QtCore.QRect(300, 220, 331, 81))
        font.setPointSize(18)
        self.no_books_label.setFont(font)
        self.no_books_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.no_books_label.setAutoFillBackground(False)
        self.no_books_label.setTextFormat(QtCore.Qt.RichText)
        self.no_books_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_books_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.no_books_label.setObjectName("no_books_label")
        self.no_books_label.setText("没有未归还的书籍")
        self.no_books_label.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 建立连接
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.return_book)

        # 设置模型
        self.model = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model)

        # 初始化表头
        self.model.setHorizontalHeaderLabels(['Borrow ID', 'Book Name', 'Author', 'Lend Time'])

        # 连接滚动条
        self.tableView.verticalScrollBar().rangeChanged.connect(self.update_scrollbar)
        self.verticalScrollBar.valueChanged.connect(self.tableView.verticalScrollBar().setValue)
        self.tableView.verticalScrollBar().valueChanged.connect(self.verticalScrollBar.setValue)

        # 显示未归还的书籍
        self.display_books()

    def display_books(self):
        # 获取未归还的书籍列表
        student = utils.Student(self.stu_id[0], self.username, self.password)
        result = student.show_borrowed_books(db)
        self.update_table(result)

    def update_table(self, books):
        self.model.setRowCount(0)  # 清除现有内容
        if not books:
            self.no_books_label.show()
            self.tableView.hide()
            self.verticalScrollBar.hide()
        else:
            self.no_books_label.hide()
            self.tableView.show()
            self.verticalScrollBar.show()
            for book in books:
                items = [
                    QtGui.QStandardItem(str(book[0])),
                    QtGui.QStandardItem(str(book[1])),
                    QtGui.QStandardItem(str(book[2])),
                    QtGui.QStandardItem(book[3].strftime('%Y-%m-%d %H:%M:%S'))
                ]
                self.model.appendRow(items)

    def update_scrollbar(self, min, max):
        self.verticalScrollBar.setMinimum(min)
        self.verticalScrollBar.setMaximum(max)

    def return_book(self):
        borrow_id = self.lineEdit_2.text()
        self.label_3.setText("您归还的书籍借阅编号是：{}".format(borrow_id))
        student = utils.Student(self.stu_id, self.username, self.password)
        result = student.return_book(db, borrow_id)
        if result:
            self.label_3.setText("归还成功！")
            self.display_books()  # 重新显示未归还的书籍
        else:
            self.label_3.setText("归还失败，请检查借阅编号。")
        self.display_books()
        db.commit()

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "请输出您要归还的书籍借阅编号"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.label.setText(_translate("MainWindow", "未归还书籍查询"))
        self.pushButton_4.setText(_translate("MainWindow", "归还"))
        self.label_2.setText(_translate("MainWindow", "书籍归还"))

# 在本模块内测试
if __name__ == "__main__":
    import sys
    from datetime import datetime

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()  # 假设这是你的主窗口

    # 模拟用户登录信息
    stu_id = 1
    username = '张三'
    password = 'password'

    # 模拟未归还的书籍信息
    result = [
        (12, '西游记', '吴承恩', datetime(2024, 6, 2, 22, 1, 7)),
        (15, '三国演义', '罗贯中', datetime(2024, 6, 3, 10, 15, 30)),
        (18, '红楼梦', '曹雪芹', datetime(2024, 6, 4, 11, 45, 20))
    ]

    ui = Ui_return_book()
    ui.setupUi(MainWindow, main_window, stu_id, username, password)
    MainWindow.show()
    sys.exit(app.exec_())
