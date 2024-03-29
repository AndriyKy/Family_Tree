# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 600)
        MainWindow.setMinimumSize(QtCore.QSize(845, 600))
        MainWindow.showMaximized()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/family_tree.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.682, y2:0.0340909, stop:0.465909 rgba(21, 22, 26, 255), stop:1 rgba(34, 35, 42, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setMinimumSize(QtCore.QSize(205, 300))
        self.verticalGroupBox.setMaximumSize(QtCore.QSize(0, 300))
        self.verticalGroupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(32, 33, 37);\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}")
        self.verticalGroupBox.setTitle("")
        self.verticalGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setMinimumSize(QtCore.QSize(185, 50))
        self.pushButton_1.setMaximumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setItalic(True)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: rgb(80, 80, 85);\n"
"    border-bottom: 2px solid rgba(70, 70, 70, 110);\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/Avatar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon1)
        self.pushButton_1.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgb(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/Select.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgb(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/Edit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgb(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/Family.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgb(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/Review.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    text-align: left;\n"
"    background-color: none;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00c580;\n"
"    border: none;\n"
"    float: right;\n"
"    padding: 5px;\n"
"    border-bottom: 2px solid rgb(38, 127, 51, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 136, 86);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/Generate.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout.addWidget(self.verticalGroupBox)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setStyleSheet("")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("Icons/family_tree.png"))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Family Tree"))
        self.pushButton_1.setText(_translate("MainWindow", "Рід: прізвище роду\n"
"Ім\'я Прізвище"))
        self.pushButton_2.setText(_translate("MainWindow", "Родини"))
        self.pushButton_3.setText(_translate("MainWindow", "Додати/змінити "))
        self.pushButton_4.setText(_translate("MainWindow", "Сімейні зв\'язки"))
        self.pushButton_5.setText(_translate("MainWindow", "Переглянути "))
        self.pushButton_6.setText(_translate("MainWindow", "Діаграма"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
