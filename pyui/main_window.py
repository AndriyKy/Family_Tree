# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os.path import join as join_path

from PyQt5 import QtCore, QtGui, QtWidgets


class UIMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 600)
        MainWindow.setMinimumSize(QtCore.QSize(845, 600))
        MainWindow.showMaximized()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(join_path("icons", "family_tree.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QMainWindow {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.682, y2:0.0340909, stop:0.465909 rgba(21, 22, 26, 255), stop:1 rgba(34, 35, 42, 255));\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setMinimumSize(QtCore.QSize(205, 300))
        self.verticalGroupBox.setMaximumSize(QtCore.QSize(0, 300))
        self.verticalGroupBox.setStyleSheet(
            "QGroupBox {\n"
            "    background-color: rgb(32, 33, 37);\n"
            "    border-radius: 10px;\n"
            "    border: none;\n"
            "}"
        )
        self.verticalGroupBox.setTitle("")
        self.verticalGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint
        )
        self.verticalLayout.setContentsMargins(10, 10, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_myCard = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_myCard.setEnabled(True)
        self.pushButton_myCard.setMinimumSize(QtCore.QSize(185, 50))
        self.pushButton_myCard.setMaximumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        font.setItalic(True)
        self.pushButton_myCard.setFont(font)
        self.pushButton_myCard.setStyleSheet(
            "QPushButton {\n"
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
            "}"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(join_path("icons", "Avatar.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_myCard.setIcon(icon1)
        self.pushButton_myCard.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_myCard.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_myCard)
        self.pushButton_addRemoveClan = QtWidgets.QPushButton(
            self.verticalGroupBox
        )
        self.pushButton_addRemoveClan.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_addRemoveClan.setFont(font)
        self.pushButton_addRemoveClan.setStyleSheet(
            "QPushButton {\n"
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
            "    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 136, 86);\n"
            "}"
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(join_path("icons", "Select.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_addRemoveClan.setIcon(icon2)
        self.pushButton_addRemoveClan.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_addRemoveClan.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_addRemoveClan)
        self.pushButton_addEdit = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_addEdit.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_addEdit.setFont(font)
        self.pushButton_addEdit.setStyleSheet(
            "QPushButton {\n"
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
            "    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 136, 86);\n"
            "}"
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(join_path("icons", "Edit.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_addEdit.setIcon(icon3)
        self.pushButton_addEdit.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_addEdit.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_addEdit)
        self.pushButton_familyTies = QtWidgets.QPushButton(
            self.verticalGroupBox
        )
        self.pushButton_familyTies.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_familyTies.setFont(font)
        self.pushButton_familyTies.setStyleSheet(
            "QPushButton {\n"
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
            "    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 136, 86);\n"
            "}"
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(join_path("icons", "Family.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_familyTies.setIcon(icon4)
        self.pushButton_familyTies.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_familyTies.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_familyTies)
        self.pushButton_review = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_review.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_review.setFont(font)
        self.pushButton_review.setStyleSheet(
            "QPushButton {\n"
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
            "    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 136, 86);\n"
            "}"
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(join_path("icons", "Review.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_review.setIcon(icon5)
        self.pushButton_review.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_review.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_review)
        self.pushButton_graph = QtWidgets.QPushButton(self.verticalGroupBox)
        self.pushButton_graph.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.pushButton_graph.setFont(font)
        self.pushButton_graph.setStyleSheet(
            "QPushButton {\n"
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
            "    border-bottom: 2px solid rgba(38, 127, 51, 130);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 136, 86);\n"
            "}"
        )
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(join_path("icons", "Generate.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_graph.setIcon(icon6)
        self.pushButton_graph.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_graph.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_graph)
        self.horizontalLayout.addWidget(self.verticalGroupBox)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setStyleSheet("")
        self.label_logo.setText("")
        self.label_logo.setPixmap(
            QtGui.QPixmap(join_path("icons", "family_tree.png"))
        )
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Family Tree"))
        self.pushButton_myCard.setText(
            _translate("MainWindow", "Рід: прізвище роду\n" "Ім'я Прізвище")
        )
        self.pushButton_addRemoveClan.setText(
            _translate("MainWindow", "Родини")
        )
        self.pushButton_addEdit.setText(
            _translate("MainWindow", "Додати/змінити ")
        )
        self.pushButton_familyTies.setText(
            _translate("MainWindow", "Сімейні зв'язки")
        )
        self.pushButton_review.setText(
            _translate("MainWindow", "Переглянути ")
        )
        self.pushButton_graph.setText(_translate("MainWindow", "Дерево"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
