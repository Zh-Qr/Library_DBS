from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='exp3',
                     charset='utf8')

class Ui_check_admin(object):
    def setupUi(self, MainWindow, main_window, result):
        self.main_window = main_window
        self.current_window = MainWindow
        self.result = result  # 保存查询结果

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 1076)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(160, 220, 631, 661))
        self.tableView.setObjectName("tableView")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(800, 80, 421, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1060, 790, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(800, 90, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(110, 910, 701, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(100, 90, 20, 831))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 120, 331, 81))
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
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(810, 910, 421, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 130, 331, 81))
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 80, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1210, 90, 20, 831))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 790, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(860, 350, 321, 41))
        self.lineEdit_2.setStyleSheet("font： 15")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 220, 16, 661))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 490, 281, 61))
        self.label_3.setStyleSheet("font: 12pt")
        self.label_3.setObjectName("label_3")
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

        #建立联系
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.confirm_admin)

        # 设置模型
        self.model = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model)

        # 初始化表头
        self.model.setHorizontalHeaderLabels(['ID', 'Username', 'Password', 'Created At'])

        # 设置列宽
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.setColumnWidth(0, 50)
        self.tableView.setColumnWidth(1, 150)
        self.tableView.setColumnWidth(2, 150)
        self.tableView.setColumnWidth(3, 200)

        # 显示数据
        self.update_table(result)

    def update_table(self, admins):
        self.model.setRowCount(0)  # 清除现有内容
        for admin in admins:
            items = [QtGui.QStandardItem(str(field)) for field in admin]
            self.model.appendRow(items)

    def confirm_admin(self):
        selected_id = self.lineEdit_2.text()
        cur = db.cursor()
        try:
            # 从admin_wait表中获取指定ID的管理员信息
            get_admin_sql = "SELECT username, password, created_at FROM admin_wait WHERE admin_id = %s"
            cur.execute(get_admin_sql, (selected_id,))
            admin_info = cur.fetchone()

            if admin_info:
                username, password,time = admin_info
                # 将管理员信息插入到admin表中，自动设置created_at字段为当前时间
                insert_admin_sql = """
                INSERT INTO admin (username, password, created_at)
                VALUES (%s, %s, %s)
                """
                cur.execute(insert_admin_sql, (username, password,time))

                # 从admin_wait表中删除该管理员信息
                delete_admin_sql = "DELETE FROM admin_wait WHERE admin_id = %s"
                cur.execute(delete_admin_sql, (selected_id,))

                db.commit()
                print("Admin confirmed and added successfully!")

                # 更新表格数据
                self.update_table([admin for admin in self.result if str(admin[0]) != selected_id])
            else:
                print("Admin ID not found.")
        except Exception as e:
            self.label_3.setText("已经重复注册")
            print(f"Error: {e}")
            db.rollback()
        finally:
            cur.close()

    def update_scrollbar(self, min, max):
        self.verticalScrollBar.setMinimum(min)
        self.verticalScrollBar.setMaximum(max)

    def back(self):
        self.main_window.show()
        self.current_window.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.label.setText(_translate("MainWindow", "待审核管理员"))
        self.label_2.setText(_translate("MainWindow", "审核确认"))
        self.pushButton_4.setText(_translate("MainWindow", "确认"))
        self.label_3.setText(_translate("MainWindow", "输入确认的编号"))

# 在本模块内测试
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()  # 假设这是你的主窗口

    # 执行SQL查询
    cur = db.cursor()
    get_admin_wait_sql = "SELECT admin_id, username, password, email FROM admin_wait"
    cur.execute(get_admin_wait_sql)
    result = cur.fetchall()
    cur.close()

    ui = Ui_check_admin()
    ui.setupUi(MainWindow, main_window, result)
    MainWindow.show()
    sys.exit(app.exec_())
