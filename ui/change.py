# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
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


class Ui_change(object):
    def setupUi(self, MainWindow, main_window):
        self.main_window = main_window
        self.current_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1287, 1100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(780, 90, 421, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 130, 361, 81))
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
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(140, 230, 631, 661))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(840, 140, 331, 81))
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
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(90, 920, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 100, 20, 831))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1190, 100, 20, 831))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(760, 230, 16, 551))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 850, 281, 61))
        self.label_3.setStyleSheet("font: 12pt")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 780, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 90, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(780, 100, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(850, 230, 101, 41))
        self.lineEdit_2.setStyleSheet("font： 15pt")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(790, 920, 421, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 780, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(850, 350, 321, 41))
        self.lineEdit_3.setStyleSheet("font： 15pt")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, 290, 281, 61))
        self.label_4.setStyleSheet("font: 12pt")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(850, 410, 281, 61))
        self.label_5.setStyleSheet("font: 12pt")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(850, 470, 321, 41))
        self.lineEdit_4.setStyleSheet("font： 15pt")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(850, 590, 321, 41))
        self.lineEdit_5.setStyleSheet("font： 15pt")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(850, 530, 281, 61))
        self.label_6.setStyleSheet("font: 12pt")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(850, 710, 321, 41))
        self.lineEdit_6.setStyleSheet("font： 15pt")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(850, 650, 281, 61))
        self.label_7.setStyleSheet("font: 12pt")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1000, 230, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1287, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 建立连接
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.delete_book)

        # 设置模型
        self.model = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model)

        # 初始化表头
        self.model.setHorizontalHeaderLabels(['Book ID', 'Book Name', 'Author', 'Publisher', 'Quantity'])

        # 连接滚动条
        self.tableView.verticalScrollBar().rangeChanged.connect(self.update_scrollbar)
        self.verticalScrollBar.valueChanged.connect(self.tableView.verticalScrollBar().setValue)
        self.tableView.verticalScrollBar().valueChanged.connect(self.verticalScrollBar.setValue)

        # 显示所有书籍信息
        self.display_books()

    def display_books(self):
        db.commit()
        cur = db.cursor()
        get_books_sql = "SELECT * FROM book"
        cur.execute(get_books_sql)
        result = cur.fetchall()
        self.update_table(result)
        cur.close()

    def update_table(self, books):
        self.model.setRowCount(0)  # 清除现有内容
        for book in books:
            items = [
                QtGui.QStandardItem(str(book[0])),
                QtGui.QStandardItem(str(book[1])),
                QtGui.QStandardItem(str(book[2])),
                QtGui.QStandardItem(str(book[3])),
                QtGui.QStandardItem(str(book[4]))
            ]
            self.model.appendRow(items)

    def update_scrollbar(self, min, max):
        self.verticalScrollBar.setMinimum(min)
        self.verticalScrollBar.setMaximum(max)

    def confirm(self):
        book_id = self.lineEdit_2.text()

        if not book_id:
            print("Please enter a book ID")
            return

        cur = db.cursor()

        # 获取当前书籍信息
        get_book_sql = "SELECT * FROM book WHERE book_id = %s"
        cur.execute(get_book_sql, (book_id,))
        current_book = cur.fetchone()

        if not current_book:
            print("Book not found")
            return

        # 使用现有信息填充缺失的字段
        book_name = self.lineEdit_3.text() if self.lineEdit_3.text() else current_book[1]
        author = self.lineEdit_4.text() if self.lineEdit_4.text() else current_book[2]
        publisher = self.lineEdit_5.text() if self.lineEdit_5.text() else current_book[3]
        quantity = self.lineEdit_6.text() if self.lineEdit_6.text() else current_book[4]

        update_book_sql = """
        UPDATE book
        SET bookname = %s, author = %s, publisher = %s, num = %s
        WHERE book_id = %s
        """
        try:
            cur.execute(update_book_sql, (book_name, author, publisher, quantity, book_id))
            db.commit()
            print("Book information updated successfully!")
            self.display_books()
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
        finally:
            cur.close()

    def delete_book(self):
        book_id = self.lineEdit_2.text()
        if book_id:
            cur = db.cursor()
            delete_book_sql = "DELETE FROM book WHERE book_id = %s"
            try:
                cur.execute(delete_book_sql, (book_id,))
                db.commit()
                print("Book deleted successfully!")
                self.display_books()
            except Exception as e:
                print(f"Error: {e}")
                db.rollback()
            finally:
                cur.close()
        else:
            print("Please enter a book ID")

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "选择需要修改的书籍"))
        self.label_2.setText(_translate("MainWindow", "书籍编号选择"))
        self.label_3.setText(_translate("MainWindow", "请谨慎填写"))
        self.pushButton_4.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.label_4.setText(_translate("MainWindow", "书名"))
        self.label_5.setText(_translate("MainWindow", "作者"))
        self.label_6.setText(_translate("MainWindow", "出版社"))
        self.label_7.setText(_translate("MainWindow", "数量"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))

# 在本模块内测试
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()  # 假设这是你的主窗口

    ui = Ui_change()
    ui.setupUi(MainWindow, main_window)
    MainWindow.show()
    sys.exit(app.exec_())