# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\Review.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os.path import join as join_path

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Review(object):
    def setupUi(self, Review):
        Review.setObjectName("Review")
        Review.resize(837, 531)
        Review.setMinimumSize(QtCore.QSize(640, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(join_path("icons", "Review.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        Review.setWindowIcon(icon)
        Review.setStyleSheet("background-color: rgb(32, 33, 37);\n" "")
        Review.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Review)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(Review)
        self.main_frame.setMinimumSize(QtCore.QSize(400, 400))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(self.main_frame)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_choiceClan = QtWidgets.QLabel(self.frame_top)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_choiceClan.setFont(font)
        self.label_choiceClan.setStyleSheet("color: white;")
        self.label_choiceClan.setTextFormat(QtCore.Qt.AutoText)
        self.label_choiceClan.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_choiceClan.setObjectName("label_choiceClan")
        self.horizontalLayout.addWidget(self.label_choiceClan)
        self.comboBox_choiceClan = QtWidgets.QComboBox(self.frame_top)
        self.comboBox_choiceClan.setMinimumSize(QtCore.QSize(222, 30))
        self.comboBox_choiceClan.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.comboBox_choiceClan.setFont(font)
        self.comboBox_choiceClan.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);\n"
            "selection-background-color: white;\n"
            "selection-color: rgba(21, 22, 26, 255);\n"
            ""
        )
        self.comboBox_choiceClan.setObjectName("comboBox_choiceClan")
        self.horizontalLayout.addWidget(self.comboBox_choiceClan)
        self.verticalLayout_2.addWidget(
            self.frame_top, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.line = QtWidgets.QFrame(self.main_frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.tableWidget = QtWidgets.QTableWidget(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "gridline-color: rgb(255, 255, 255);"
        )
        self.tableWidget.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel
        )
        self.tableWidget.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel
        )
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(21, 22, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton_done = QtWidgets.QPushButton(self.main_frame)
        self.pushButton_done.setMinimumSize(QtCore.QSize(135, 35))
        self.pushButton_done.setMaximumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_done.setFont(font)
        self.pushButton_done.setStyleSheet(
            "QPushButton {\n"
            "    text-align: center;\n"
            "    background-color: rgb(80, 80, 85);\n"
            "    border-bottom: 2px solid rgba(70, 70, 70, 150);\n"
            "    border-radius: 8px;\n"
            "    padding: 5px;\n"
            "    color: rgb(32, 33, 37);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #00c580;\n"
            "    color: white;\n"
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
        self.pushButton_done.setObjectName("pushButton_done")
        self.verticalLayout_2.addWidget(
            self.pushButton_done, 0, QtCore.Qt.AlignHCenter
        )
        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(Review)
        QtCore.QMetaObject.connectSlotsByName(Review)

    def retranslateUi(self, Review):
        _translate = QtCore.QCoreApplication.translate
        Review.setWindowTitle(_translate("Review", "Перегляд списку роду"))
        self.label_choiceClan.setText(_translate("Review", "Рід"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Review", "Стать"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Review", "Прізвище"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Review", "Ім'я"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Review", "Ім'я по батькові"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Review", "Місце народження"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Review", "Місце смерті"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Review", "Рік народження"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Review", "Рік смерті"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Review", "Додаткова інформація"))
        self.pushButton_done.setText(_translate("Review", "Ок"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Review = QtWidgets.QDialog()
    ui = Ui_Review()
    ui.setupUi(Review)
    Review.show()
    sys.exit(app.exec_())
