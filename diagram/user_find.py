# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DBMS\ui\user_find.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設定查詢按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 80, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        # 設定返回按鈕
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 140, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        
        # 設定群組框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 30, 491, 201))
        self.groupBox.setObjectName("groupBox")
        
        # 設定網格佈局小工具
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 441, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        # 設定網格佈局
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 設定密碼標籤
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 設定帳號標籤
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 設定帳號輸入框
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        # 設定密碼輸入框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
        # 設定用戶資料群組框
        self.user_info_group = QtWidgets.QGroupBox(self.centralwidget)
        self.user_info_group.setGeometry(QtCore.QRect(100, 250, 600, 150))
        self.user_info_group.setTitle("用戶資料")
        
        # 設定用戶資料標籤
        self.user_info_label = QtWidgets.QLabel(self.user_info_group)
        self.user_info_label.setGeometry(QtCore.QRect(10, 20, 280, 120))
        self.user_info_label.setWordWrap(True)
        self.user_info_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.user_info_label.setStyleSheet("font-size: 12pt; color: #333;")
        self.user_info_label.setObjectName("user_info_label")
        
        # 設定用戶車輛群組框
        self.vehicle_info_group = QtWidgets.QGroupBox(self.centralwidget)
        self.vehicle_info_group.setGeometry(QtCore.QRect(100, 410, 600, 150))
        self.vehicle_info_group.setTitle("用戶的車輛")
        
        # 設定用戶車輛標籤
        self.vehicle_info_label = QtWidgets.QLabel(self.vehicle_info_group)
        self.vehicle_info_label.setGeometry(QtCore.QRect(10, 20, 280, 120))
        self.vehicle_info_label.setWordWrap(True)
        self.vehicle_info_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.vehicle_info_label.setStyleSheet("font-size: 12pt; color: #333;")
        self.vehicle_info_label.setObjectName("vehicle_info_label")
        
        # 設定主視窗的中央小工具
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設定選單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設定狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 重新翻譯UI文字
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設定UI文字的翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "查詢"))
        self.pushButton_4.setText(_translate("MainWindow", "返回"))
        self.groupBox.setTitle(_translate("MainWindow", "登入"))
        self.label_2.setText(_translate("MainWindow", "密碼："))
        self.label.setText(_translate("MainWindow", "帳號："))


if __name__ == "__main__":
    import sys
    # 創建應用程式
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 執行應用程式
    sys.exit(app.exec_())
