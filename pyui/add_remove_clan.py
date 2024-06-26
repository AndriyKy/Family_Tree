# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\AddRemove_clan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os.path import join as join_path

from PyQt5 import QtCore, QtGui, QtWidgets


class UIAddRemoveClan(object):
    def setupUi(self, AddRemoveClan):
        AddRemoveClan.setObjectName("AddRemoveClan")
        AddRemoveClan.resize(470, 225)
        AddRemoveClan.setMinimumSize(QtCore.QSize(470, 225))
        AddRemoveClan.setMaximumSize(QtCore.QSize(470, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(join_path("icons", "Select.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        AddRemoveClan.setWindowIcon(icon)
        AddRemoveClan.setStyleSheet("background-color: rgb(32, 33, 37);")
        AddRemoveClan.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddRemoveClan)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_frame = QtWidgets.QFrame(AddRemoveClan)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left = QtWidgets.QFrame(self.main_frame)
        self.frame_left.setMaximumSize(QtCore.QSize(226, 16777215))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_addClan = QtWidgets.QLabel(self.frame_left)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_addClan.setFont(font)
        self.label_addClan.setMouseTracking(True)
        self.label_addClan.setStyleSheet("color: white;")
        self.label_addClan.setTextFormat(QtCore.Qt.AutoText)
        self.label_addClan.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_addClan.setObjectName("label_addClan")
        self.verticalLayout.addWidget(self.label_addClan)
        self.lineEdit_addClan = QtWidgets.QLineEdit(self.frame_left)
        self.lineEdit_addClan.setMinimumSize(QtCore.QSize(222, 29))
        self.lineEdit_addClan.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_addClan.setFont(font)
        self.lineEdit_addClan.setMouseTracking(False)
        self.lineEdit_addClan.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_addClan.setText("")
        self.lineEdit_addClan.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_addClan.setClearButtonEnabled(True)
        self.lineEdit_addClan.setObjectName("lineEdit_addClan")
        self.verticalLayout.addWidget(self.lineEdit_addClan)
        self.label_or = QtWidgets.QLabel(self.frame_left)
        self.label_or.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_or.setFont(font)
        self.label_or.setStyleSheet("color: white;")
        self.label_or.setTextFormat(QtCore.Qt.AutoText)
        self.label_or.setAlignment(QtCore.Qt.AlignCenter)
        self.label_or.setObjectName("label_or")
        self.verticalLayout.addWidget(
            self.label_or, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom
        )
        self.label_removeClan = QtWidgets.QLabel(self.frame_left)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_removeClan.setFont(font)
        self.label_removeClan.setStyleSheet("color: white;")
        self.label_removeClan.setTextFormat(QtCore.Qt.AutoText)
        self.label_removeClan.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_removeClan.setObjectName("label_removeClan")
        self.verticalLayout.addWidget(self.label_removeClan)
        self.comboBox_RemoveClan = QtWidgets.QComboBox(self.frame_left)
        self.comboBox_RemoveClan.setMinimumSize(QtCore.QSize(222, 30))
        self.comboBox_RemoveClan.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.comboBox_RemoveClan.setFont(font)
        self.comboBox_RemoveClan.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);\n"
            "selection-background-color: white;\n"
            "selection-color:rgba(21, 22, 26, 255);\n"
            ""
        )
        self.comboBox_RemoveClan.setObjectName("comboBox_RemoveClan")
        self.comboBox_RemoveClan.addItem("")
        self.comboBox_RemoveClan.setItemText(0, "")
        self.verticalLayout.addWidget(self.comboBox_RemoveClan)
        self.horizontalLayout_2.addWidget(self.frame_left)
        self.line = QtWidgets.QFrame(self.main_frame)
        self.line.setMinimumSize(QtCore.QSize(0, 160))
        self.line.setStyleSheet("Line{\n" "    color: rgb(21, 22, 26);\n" "}")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.label_note = QtWidgets.QLabel(self.main_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_note.setFont(font)
        self.label_note.setMouseTracking(True)
        self.label_note.setStyleSheet("color: white;")
        self.label_note.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_note.setWordWrap(True)
        self.label_note.setObjectName("label_note")
        self.horizontalLayout_2.addWidget(
            self.label_note, 0, QtCore.Qt.AlignVCenter
        )
        self.verticalLayout_2.addWidget(self.main_frame)
        self.pushButton_done = QtWidgets.QPushButton(AddRemoveClan)
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

        as_needed = QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        self.comboBox_RemoveClan.view().setVerticalScrollBarPolicy(as_needed)

        self.retranslateUi(AddRemoveClan)
        QtCore.QMetaObject.connectSlotsByName(AddRemoveClan)

    def retranslateUi(self, AddRemoveClan):
        _translate = QtCore.QCoreApplication.translate
        AddRemoveClan.setWindowTitle(_translate("AddRemoveClan", "Родини"))
        self.label_addClan.setText(
            _translate(
                "AddRemoveClan",
                '<html><head/><body><p>Додати рід <span style=" color:#fb4938;">*</span></p></body></html>',
            )
        )
        self.label_or.setText(_translate("AddRemoveClan", "або"))
        self.label_removeClan.setText(
            _translate("AddRemoveClan", " Видалити рід")
        )
        self.label_note.setText(
            _translate(
                "AddRemoveClan",
                '<html><head/><body><p><span style=" color:#fb4938;">* </span>Прізвище роду записується в родовому відмінку множини. Наприклад: Мельник - <span style=" font-weight:600;">Мельників</span></p></body></html>',
            )
        )
        self.pushButton_done.setText(_translate("AddRemoveClan", "Готово"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddRemoveClan = QtWidgets.QDialog()
    ui = UIAddRemoveClan()
    ui.setupUi(AddRemoveClan)
    AddRemoveClan.show()
    sys.exit(app.exec_())
