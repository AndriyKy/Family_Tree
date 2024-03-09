# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\Family_ties.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FamilyTies(object):
    def setupUi(self, FamilyTies):
        FamilyTies.setObjectName("FamilyTies")
        FamilyTies.resize(875, 590)
        FamilyTies.setMinimumSize(QtCore.QSize(875, 590))
        FamilyTies.setMaximumSize(QtCore.QSize(875, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("Icons/Family.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        FamilyTies.setWindowIcon(icon)
        FamilyTies.setStyleSheet("background-color: rgb(32, 33, 37);")
        FamilyTies.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FamilyTies)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(FamilyTies)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_choiceClan = QtWidgets.QFrame(self.main_frame)
        self.frame_choiceClan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_choiceClan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_choiceClan.setObjectName("frame_choiceClan")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_choiceClan)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_clan = QtWidgets.QLabel(self.frame_choiceClan)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_clan.setFont(font)
        self.label_clan.setStyleSheet("color: white;")
        self.label_clan.setTextFormat(QtCore.Qt.AutoText)
        self.label_clan.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_clan.setObjectName("label_clan")
        self.horizontalLayout_3.addWidget(self.label_clan)
        self.comboBox_choiceClan = QtWidgets.QComboBox(self.frame_choiceClan)
        self.comboBox_choiceClan.setMinimumSize(QtCore.QSize(221, 32))
        self.comboBox_choiceClan.setMaximumSize(QtCore.QSize(221, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
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
            "selection-color:rgba(21, 22, 26, 255);\n"
            ""
        )
        self.comboBox_choiceClan.setObjectName("comboBox_choiceClan")
        self.horizontalLayout_3.addWidget(self.comboBox_choiceClan)
        spacerItem = QtWidgets.QSpacerItem(
            30, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(
            self.frame_choiceClan,
            0,
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
        )
        self.line_horCenter_2 = QtWidgets.QFrame(self.main_frame)
        self.line_horCenter_2.setStyleSheet(
            "Line{\n" "    color: rgb(21, 22, 26);\n" "}"
        )
        self.line_horCenter_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horCenter_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horCenter_2.setObjectName("line_horCenter_2")
        self.verticalLayout_2.addWidget(self.line_horCenter_2)
        self.frame_top = QtWidgets.QFrame(self.main_frame)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame_1 = QtWidgets.QFrame(self.frame_top)
        self.left_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame_1.setObjectName("left_frame_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_frame_1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_father = QtWidgets.QLabel(self.left_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_father.setFont(font)
        self.label_father.setStyleSheet("color: white;")
        self.label_father.setTextFormat(QtCore.Qt.AutoText)
        self.label_father.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_father.setObjectName("label_father")
        self.verticalLayout_3.addWidget(self.label_father)
        self.comboBox_choiceFather = QtWidgets.QComboBox(self.left_frame_1)
        self.comboBox_choiceFather.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choiceFather.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choiceFather.setFont(font)
        self.comboBox_choiceFather.setStyleSheet(
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
        self.comboBox_choiceFather.setObjectName("comboBox_choiceFather")
        self.verticalLayout_3.addWidget(self.comboBox_choiceFather)
        self.horizontalLayout.addWidget(self.left_frame_1)
        self.right_frame_1 = QtWidgets.QFrame(self.frame_top)
        self.right_frame_1.setMaximumSize(QtCore.QSize(412, 16777215))
        self.right_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame_1.setObjectName("right_frame_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.right_frame_1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_mother = QtWidgets.QLabel(self.right_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_mother.setFont(font)
        self.label_mother.setStyleSheet("color: white;")
        self.label_mother.setTextFormat(QtCore.Qt.AutoText)
        self.label_mother.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_mother.setObjectName("label_mother")
        self.verticalLayout_4.addWidget(self.label_mother)
        self.comboBox_choiceMother = QtWidgets.QComboBox(self.right_frame_1)
        self.comboBox_choiceMother.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choiceMother.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choiceMother.setFont(font)
        self.comboBox_choiceMother.setStyleSheet(
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
        self.comboBox_choiceMother.setObjectName("comboBox_choiceMother")
        self.verticalLayout_4.addWidget(self.comboBox_choiceMother)
        self.horizontalLayout.addWidget(self.right_frame_1)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.line_horTop = QtWidgets.QFrame(self.main_frame)
        self.line_horTop.setStyleSheet(
            "Line{\n" "    color: rgb(21, 22, 26);\n" "}"
        )
        self.line_horTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horTop.setObjectName("line_horTop")
        self.verticalLayout_2.addWidget(self.line_horTop)
        self.frame_center = QtWidgets.QFrame(self.main_frame)
        self.frame_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_frame_2 = QtWidgets.QFrame(self.frame_center)
        self.left_frame_2.setMaximumSize(QtCore.QSize(16777215, 180))
        self.left_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame_2.setObjectName("left_frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.left_frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_BS = QtWidgets.QLabel(self.left_frame_2)
        self.label_BS.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_BS.setFont(font)
        self.label_BS.setStyleSheet("color: white;")
        self.label_BS.setTextFormat(QtCore.Qt.AutoText)
        self.label_BS.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_BS.setObjectName("label_BS")
        self.verticalLayout_6.addWidget(self.label_BS)
        self.comboBox_choiceBS = QtWidgets.QComboBox(self.left_frame_2)
        self.comboBox_choiceBS.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choiceBS.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choiceBS.setFont(font)
        self.comboBox_choiceBS.setStyleSheet(
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
        self.comboBox_choiceBS.setObjectName("comboBox_choiceBS")
        self.verticalLayout_6.addWidget(self.comboBox_choiceBS)
        self.pushButton_addBS = QtWidgets.QPushButton(self.left_frame_2)
        self.pushButton_addBS.setMinimumSize(QtCore.QSize(30, 45))
        self.pushButton_addBS.setMaximumSize(QtCore.QSize(30, 45))
        self.pushButton_addBS.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.pushButton_addBS.setStyleSheet(
            "QPushButton {\n"
            "    background-image: url(:/newPrefix/Icons/Add.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-image: url(:/newPrefix/Icons/Add_color.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-image: url(:/newPrefix/Icons/Add_color_pressed.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}"
        )
        self.pushButton_addBS.setText("")
        self.pushButton_addBS.setObjectName("pushButton_addBS")
        self.verticalLayout_6.addWidget(
            self.pushButton_addBS, 0, QtCore.Qt.AlignHCenter
        )
        self.tableWidget_BS = QtWidgets.QTableWidget(self.left_frame_2)
        self.tableWidget_BS.setMaximumSize(QtCore.QSize(410, 73))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableWidget_BS.setFont(font)
        self.tableWidget_BS.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "gridline-color: rgb(255, 255, 255);"
        )
        self.tableWidget_BS.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn
        )
        self.tableWidget_BS.setRowCount(0)
        self.tableWidget_BS.setColumnCount(1)
        self.tableWidget_BS.setObjectName("tableWidget_BS")
        self.tableWidget_BS.horizontalHeader().setVisible(False)
        self.tableWidget_BS.horizontalHeader().setDefaultSectionSize(375)
        self.verticalLayout_6.addWidget(self.tableWidget_BS)
        self.horizontalLayout_2.addWidget(
            self.left_frame_2, 0, QtCore.Qt.AlignTop
        )
        self.line_vertCenter = QtWidgets.QFrame(self.frame_center)
        self.line_vertCenter.setMinimumSize(QtCore.QSize(20, 0))
        self.line_vertCenter.setStyleSheet(
            "Line{\n" "    color: rgb(21, 22, 26);\n" "}"
        )
        self.line_vertCenter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertCenter.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertCenter.setObjectName("line_vertCenter")
        self.horizontalLayout_2.addWidget(self.line_vertCenter)
        self.right_frame_2 = QtWidgets.QFrame(self.frame_center)
        self.right_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame_2.setObjectName("right_frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.right_frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_petson = QtWidgets.QLabel(self.right_frame_2)
        self.label_petson.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_petson.setFont(font)
        self.label_petson.setStyleSheet("color: white;")
        self.label_petson.setTextFormat(QtCore.Qt.AutoText)
        self.label_petson.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_petson.setObjectName("label_petson")
        self.verticalLayout_5.addWidget(self.label_petson)
        self.comboBox_choicePerson = QtWidgets.QComboBox(self.right_frame_2)
        self.comboBox_choicePerson.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choicePerson.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choicePerson.setFont(font)
        self.comboBox_choicePerson.setStyleSheet(
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
        self.comboBox_choicePerson.setObjectName("comboBox_choicePerson")
        self.comboBox_choicePerson.addItem("")
        self.comboBox_choicePerson.setItemText(0, "")
        self.verticalLayout_5.addWidget(self.comboBox_choicePerson)
        self.pushButton_disable = QtWidgets.QPushButton(self.right_frame_2)
        self.pushButton_disable.setEnabled(False)
        self.pushButton_disable.setMinimumSize(QtCore.QSize(30, 37))
        self.pushButton_disable.setMaximumSize(QtCore.QSize(30, 37))
        self.pushButton_disable.setStyleSheet(
            "background-image: url(:/newPrefix/Icons/Add.ico);\n"
            "background-position: center bottom;\n"
            "background-repeat: no-repeat;\n"
            "background-attachment: fixed;\n"
            "background-size: cover;\n"
            "border: none;"
        )
        self.pushButton_disable.setText("")
        self.pushButton_disable.setObjectName("pushButton_disable")
        self.verticalLayout_5.addWidget(
            self.pushButton_disable, 0, QtCore.Qt.AlignHCenter
        )
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout_5.addItem(spacerItem1)
        self.label_partner = QtWidgets.QLabel(self.right_frame_2)
        self.label_partner.setMinimumSize(QtCore.QSize(0, 30))
        self.label_partner.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_partner.setFont(font)
        self.label_partner.setStyleSheet("color: white;")
        self.label_partner.setTextFormat(QtCore.Qt.AutoText)
        self.label_partner.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_partner.setObjectName("label_partner")
        self.verticalLayout_5.addWidget(self.label_partner)
        self.comboBox_choicePartner = QtWidgets.QComboBox(self.right_frame_2)
        self.comboBox_choicePartner.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choicePartner.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choicePartner.setFont(font)
        self.comboBox_choicePartner.setStyleSheet(
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
        self.comboBox_choicePartner.setObjectName("comboBox_choicePartner")
        self.verticalLayout_5.addWidget(self.comboBox_choicePartner)
        self.horizontalLayout_2.addWidget(self.right_frame_2)
        self.verticalLayout_2.addWidget(self.frame_center)
        self.line_horCenter = QtWidgets.QFrame(self.main_frame)
        self.line_horCenter.setStyleSheet(
            "Line{\n" "    color: rgb(21, 22, 26);\n" "}"
        )
        self.line_horCenter.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horCenter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horCenter.setObjectName("line_horCenter")
        self.verticalLayout_2.addWidget(self.line_horCenter)
        self.frame_bottom = QtWidgets.QFrame(self.main_frame)
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_children = QtWidgets.QLabel(self.frame_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_children.setFont(font)
        self.label_children.setStyleSheet("color: white;")
        self.label_children.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter
        )
        self.label_children.setObjectName("label_children")
        self.verticalLayout_9.addWidget(self.label_children)
        self.comboBox_choiceChildren = QtWidgets.QComboBox(self.frame_bottom)
        self.comboBox_choiceChildren.setMinimumSize(QtCore.QSize(410, 32))
        self.comboBox_choiceChildren.setMaximumSize(QtCore.QSize(410, 32))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_choiceChildren.setFont(font)
        self.comboBox_choiceChildren.setStyleSheet(
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
        self.comboBox_choiceChildren.setObjectName("comboBox_choiceChildren")
        self.verticalLayout_9.addWidget(self.comboBox_choiceChildren)
        self.pushButton_addChildren = QtWidgets.QPushButton(self.frame_bottom)
        self.pushButton_addChildren.setMinimumSize(QtCore.QSize(30, 45))
        self.pushButton_addChildren.setMaximumSize(QtCore.QSize(30, 45))
        self.pushButton_addChildren.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.pushButton_addChildren.setStyleSheet(
            "QPushButton {\n"
            "    background-image: url(:/newPrefix/Icons/Add.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-image: url(:/newPrefix/Icons/Add_color.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-image: url(:/newPrefix/Icons/Add_color_pressed.ico);\n"
            "    background-position: center center;\n"
            "    background-repeat: no-repeat;\n"
            "    background-attachment: fixed;\n"
            "    background-size: cover;\n"
            "    border: none;\n"
            "}"
        )
        self.pushButton_addChildren.setText("")
        self.pushButton_addChildren.setObjectName("pushButton_addChildren")
        self.verticalLayout_9.addWidget(
            self.pushButton_addChildren, 0, QtCore.Qt.AlignHCenter
        )
        self.tableWidget_choiceChildren = QtWidgets.QTableWidget(
            self.frame_bottom
        )
        self.tableWidget_choiceChildren.setMaximumSize(QtCore.QSize(410, 73))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableWidget_choiceChildren.setFont(font)
        self.tableWidget_choiceChildren.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "gridline-color: rgb(255, 255, 255);"
        )
        self.tableWidget_choiceChildren.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn
        )
        self.tableWidget_choiceChildren.setRowCount(0)
        self.tableWidget_choiceChildren.setColumnCount(1)
        self.tableWidget_choiceChildren.setObjectName(
            "tableWidget_choiceChildren"
        )
        self.tableWidget_choiceChildren.horizontalHeader().setVisible(False)
        self.tableWidget_choiceChildren.horizontalHeader().setDefaultSectionSize(
            375
        )
        self.verticalLayout_9.addWidget(self.tableWidget_choiceChildren)
        self.verticalLayout_2.addWidget(
            self.frame_bottom, 0, QtCore.Qt.AlignHCenter
        )
        self.line_horBottom = QtWidgets.QFrame(self.main_frame)
        self.line_horBottom.setMinimumSize(QtCore.QSize(270, 4))
        self.line_horBottom.setMaximumSize(QtCore.QSize(270, 4))
        self.line_horBottom.setStyleSheet(
            "Line{\n" "    color: rgb(21, 22, 26);\n" "}"
        )
        self.line_horBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horBottom.setObjectName("line_horBottom")
        self.verticalLayout_2.addWidget(
            self.line_horBottom, 0, QtCore.Qt.AlignHCenter
        )
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

        self.retranslateUi(FamilyTies)
        QtCore.QMetaObject.connectSlotsByName(FamilyTies)

    def retranslateUi(self, FamilyTies):
        _translate = QtCore.QCoreApplication.translate
        FamilyTies.setWindowTitle(_translate("FamilyTies", "Сімейні зв'язки"))
        self.label_clan.setText(_translate("FamilyTies", "Рід: "))
        self.label_father.setText(_translate("FamilyTies", "Батько:"))
        self.label_mother.setText(_translate("FamilyTies", "Мати:"))
        self.label_BS.setText(_translate("FamilyTies", "Брати/Сестри:"))
        self.label_petson.setText(
            _translate(
                "FamilyTies",
                '<html><head/><body><p>Встановити сімейні зв\'язки для <span style=" color:#fb4938;">*</span>:</p></body></html>',
            )
        )
        self.label_partner.setText(_translate("FamilyTies", "Партнер:"))
        self.label_children.setText(_translate("FamilyTies", "Діти:"))
        self.pushButton_done.setText(_translate("FamilyTies", "Готово"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FamilyTies = QtWidgets.QDialog()
    ui = Ui_FamilyTies()
    ui.setupUi(FamilyTies)
    FamilyTies.show()
    sys.exit(app.exec_())
