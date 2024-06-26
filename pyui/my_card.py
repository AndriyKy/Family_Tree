# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hitar\source\Family_tree\My_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os.path import join as join_path

from PyQt5 import QtCore, QtGui, QtWidgets


class UIMyCard(object):
    def setupUi(self, MyCard):
        MyCard.setObjectName("MyCard")
        MyCard.resize(685, 570)
        MyCard.setMinimumSize(QtCore.QSize(685, 570))
        MyCard.setMaximumSize(QtCore.QSize(685, 570))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(join_path("icons", "Avatar.ico")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MyCard.setWindowIcon(icon)
        MyCard.setStyleSheet("background-color: rgb(32, 33, 37);")
        MyCard.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyCard)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(MyCard)
        self.main_frame.setMinimumSize(QtCore.QSize(400, 400))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(self.main_frame)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_Button = QtWidgets.QPushButton(self.frame_top)
        self.image_Button.setMinimumSize(QtCore.QSize(175, 175))
        self.image_Button.setMaximumSize(QtCore.QSize(175, 175))
        self.image_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.image_Button.setStyleSheet(
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(join_path("avatars", "Add_image.png")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.image_Button.setIcon(icon1)
        self.image_Button.setIconSize(QtCore.QSize(175, 175))
        self.image_Button.setObjectName("image_Button")
        self.horizontalLayout.addWidget(self.image_Button)
        self.center_frame_1 = QtWidgets.QFrame(self.frame_top)
        self.center_frame_1.setMinimumSize(QtCore.QSize(236, 0))
        self.center_frame_1.setMaximumSize(QtCore.QSize(224, 183))
        self.center_frame_1.setObjectName("center_frame_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.center_frame_1)
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_3.setContentsMargins(5, 0, -1, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_lname = QtWidgets.QLabel(self.center_frame_1)
        self.label_lname.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_lname.setFont(font)
        self.label_lname.setMouseTracking(True)
        self.label_lname.setStyleSheet("color: white;")
        self.label_lname.setScaledContents(False)
        self.label_lname.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_lname.setObjectName("label_lname")
        self.verticalLayout_3.addWidget(self.label_lname)
        self.lineEdit_lname = QtWidgets.QLineEdit(self.center_frame_1)
        self.lineEdit_lname.setMinimumSize(QtCore.QSize(222, 29))
        self.lineEdit_lname.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_lname.setFont(font)
        self.lineEdit_lname.setMouseTracking(False)
        self.lineEdit_lname.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_lname.setText("")
        self.lineEdit_lname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_lname.setClearButtonEnabled(True)
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.verticalLayout_3.addWidget(self.lineEdit_lname)
        self.label_note = QtWidgets.QLabel(self.center_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_note.setFont(font)
        self.label_note.setMouseTracking(True)
        self.label_note.setStyleSheet("color: white;")
        self.label_note.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing
        )
        self.label_note.setWordWrap(True)
        self.label_note.setObjectName("label_note")
        self.verticalLayout_3.addWidget(self.label_note)
        self.horizontalLayout.addWidget(self.center_frame_1)
        self.right_frame_1 = QtWidgets.QFrame(self.frame_top)
        self.right_frame_1.setMaximumSize(QtCore.QSize(16777215, 180))
        self.right_frame_1.setObjectName("right_frame_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.right_frame_1)
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_fname = QtWidgets.QLabel(self.right_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_fname.setFont(font)
        self.label_fname.setMouseTracking(True)
        self.label_fname.setStyleSheet("color: white;")
        self.label_fname.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_fname.setObjectName("label_fname")
        self.verticalLayout_4.addWidget(self.label_fname)
        self.lineEdit_fname = QtWidgets.QLineEdit(self.right_frame_1)
        self.lineEdit_fname.setMinimumSize(QtCore.QSize(222, 30))
        self.lineEdit_fname.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_fname.setFont(font)
        self.lineEdit_fname.setMouseTracking(False)
        self.lineEdit_fname.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_fname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_fname.setClearButtonEnabled(True)
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.verticalLayout_4.addWidget(self.lineEdit_fname)
        self.label_patronymic = QtWidgets.QLabel(self.right_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setStyleSheet("color: white;")
        self.label_patronymic.setTextFormat(QtCore.Qt.AutoText)
        self.label_patronymic.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_patronymic.setObjectName("label_patronymic")
        self.verticalLayout_4.addWidget(self.label_patronymic)
        self.lineEdit_patronymic = QtWidgets.QLineEdit(self.right_frame_1)
        self.lineEdit_patronymic.setMinimumSize(QtCore.QSize(222, 30))
        self.lineEdit_patronymic.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_patronymic.setFont(font)
        self.lineEdit_patronymic.setMouseTracking(False)
        self.lineEdit_patronymic.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_patronymic.setDragEnabled(False)
        self.lineEdit_patronymic.setReadOnly(False)
        self.lineEdit_patronymic.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_patronymic.setClearButtonEnabled(True)
        self.lineEdit_patronymic.setObjectName("lineEdit_patronymic")
        self.verticalLayout_4.addWidget(self.lineEdit_patronymic)
        self.label_sex = QtWidgets.QLabel(self.right_frame_1)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_sex.setFont(font)
        self.label_sex.setMouseTracking(True)
        self.label_sex.setStyleSheet("color: white;")
        self.label_sex.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_sex.setObjectName("label_sex")
        self.verticalLayout_4.addWidget(self.label_sex)
        self.comboBox_sex = QtWidgets.QComboBox(self.right_frame_1)
        self.comboBox_sex.setMinimumSize(QtCore.QSize(222, 30))
        self.comboBox_sex.setMaximumSize(QtCore.QSize(222, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.comboBox_sex.setFont(font)
        self.comboBox_sex.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);\n"
            "selection-background-color: white;\n"
            "selection-color:rgba(21, 22, 26, 255);"
        )
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_sex)
        self.horizontalLayout.addWidget(
            self.right_frame_1, 0, QtCore.Qt.AlignRight
        )
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_center_top = QtWidgets.QFrame(self.main_frame)
        self.frame_center_top.setMinimumSize(QtCore.QSize(0, 63))
        self.frame_center_top.setMaximumSize(QtCore.QSize(16777215, 63))
        self.frame_center_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center_top.setObjectName("frame_center_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_center_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_frame_2 = QtWidgets.QFrame(self.frame_center_top)
        self.left_frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.left_frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.left_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame_2.setObjectName("left_frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.left_frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_yearOfBirth = QtWidgets.QLabel(self.left_frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_yearOfBirth.setFont(font)
        self.label_yearOfBirth.setMouseTracking(True)
        self.label_yearOfBirth.setStyleSheet("color: white;")
        self.label_yearOfBirth.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_yearOfBirth.setObjectName("label_yearOfBirth")
        self.verticalLayout_8.addWidget(self.label_yearOfBirth)
        self.lineEdit_yearOfBirth = QtWidgets.QLineEdit(self.left_frame_2)
        self.lineEdit_yearOfBirth.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_yearOfBirth.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_yearOfBirth.setFont(font)
        self.lineEdit_yearOfBirth.setMouseTracking(False)
        self.lineEdit_yearOfBirth.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_yearOfBirth.setCursorMoveStyle(
            QtCore.Qt.LogicalMoveStyle
        )
        self.lineEdit_yearOfBirth.setClearButtonEnabled(True)
        self.lineEdit_yearOfBirth.setObjectName("lineEdit_yearOfBirth")
        self.verticalLayout_8.addWidget(self.lineEdit_yearOfBirth)
        self.horizontalLayout_3.addWidget(self.left_frame_2)
        self.center_frame_2 = QtWidgets.QFrame(self.frame_center_top)
        self.center_frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.center_frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.center_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame_2.setObjectName("center_frame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.center_frame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_yearOfDeath = QtWidgets.QLabel(self.center_frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_yearOfDeath.setFont(font)
        self.label_yearOfDeath.setStyleSheet("color: white;")
        self.label_yearOfDeath.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_yearOfDeath.setObjectName("label_yearOfDeath")
        self.verticalLayout_9.addWidget(self.label_yearOfDeath)
        self.lineEdit_yearOfDeath = QtWidgets.QLineEdit(self.center_frame_2)
        self.lineEdit_yearOfDeath.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_yearOfDeath.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_yearOfDeath.setFont(font)
        self.lineEdit_yearOfDeath.setMouseTracking(False)
        self.lineEdit_yearOfDeath.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_yearOfDeath.setCursorMoveStyle(
            QtCore.Qt.LogicalMoveStyle
        )
        self.lineEdit_yearOfDeath.setClearButtonEnabled(True)
        self.lineEdit_yearOfDeath.setObjectName("lineEdit_yearOfDeath")
        self.verticalLayout_9.addWidget(self.lineEdit_yearOfDeath)
        self.horizontalLayout_3.addWidget(self.center_frame_2)
        self.right_frame_2 = QtWidgets.QFrame(self.frame_center_top)
        self.right_frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.right_frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame_2.setObjectName("right_frame_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.right_frame_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_clanName = QtWidgets.QLabel(self.right_frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_clanName.setFont(font)
        self.label_clanName.setStyleSheet("color: white;")
        self.label_clanName.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_clanName.setObjectName("label_clanName")
        self.verticalLayout_12.addWidget(self.label_clanName)
        self.lineEdit_clanName = QtWidgets.QLineEdit(self.right_frame_2)
        self.lineEdit_clanName.setMinimumSize(QtCore.QSize(222, 30))
        self.lineEdit_clanName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_clanName.setFont(font)
        self.lineEdit_clanName.setMouseTracking(False)
        self.lineEdit_clanName.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_clanName.setClearButtonEnabled(True)
        self.lineEdit_clanName.setObjectName("lineEdit_clanName")
        self.verticalLayout_12.addWidget(self.lineEdit_clanName)
        self.horizontalLayout_3.addWidget(self.right_frame_2)
        self.verticalLayout_2.addWidget(self.frame_center_top)
        self.frame_center_bottom = QtWidgets.QFrame(self.main_frame)
        self.frame_center_bottom.setMinimumSize(QtCore.QSize(0, 63))
        self.frame_center_bottom.setMaximumSize(QtCore.QSize(16777215, 63))
        self.frame_center_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_center_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center_bottom.setObjectName("frame_center_bottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.frame_center_bottom
        )
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_frame_3 = QtWidgets.QFrame(self.frame_center_bottom)
        self.left_frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.left_frame_3.setObjectName("left_frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left_frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_placeOfBirth = QtWidgets.QLabel(self.left_frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_placeOfBirth.setFont(font)
        self.label_placeOfBirth.setStyleSheet("color: white;")
        self.label_placeOfBirth.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_placeOfBirth.setObjectName("label_placeOfBirth")
        self.verticalLayout_5.addWidget(self.label_placeOfBirth)
        self.lineEdit_placeOfBirth = QtWidgets.QLineEdit(self.left_frame_3)
        self.lineEdit_placeOfBirth.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_placeOfBirth.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_placeOfBirth.setFont(font)
        self.lineEdit_placeOfBirth.setMouseTracking(False)
        self.lineEdit_placeOfBirth.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_placeOfBirth.setClearButtonEnabled(True)
        self.lineEdit_placeOfBirth.setObjectName("lineEdit_placeOfBirth")
        self.verticalLayout_5.addWidget(self.lineEdit_placeOfBirth)
        self.horizontalLayout_2.addWidget(self.left_frame_3)
        self.right_frame_3 = QtWidgets.QFrame(self.frame_center_bottom)
        self.right_frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_frame_3.setObjectName("right_frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.right_frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_placeOfDeath = QtWidgets.QLabel(self.right_frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_placeOfDeath.setFont(font)
        self.label_placeOfDeath.setStyleSheet("color: white;")
        self.label_placeOfDeath.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_placeOfDeath.setObjectName("label_placeOfDeath")
        self.verticalLayout_6.addWidget(self.label_placeOfDeath)
        self.lineEdit_placeOfDeath = QtWidgets.QLineEdit(self.right_frame_3)
        self.lineEdit_placeOfDeath.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_placeOfDeath.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.lineEdit_placeOfDeath.setFont(font)
        self.lineEdit_placeOfDeath.setMouseTracking(False)
        self.lineEdit_placeOfDeath.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);"
        )
        self.lineEdit_placeOfDeath.setClearButtonEnabled(True)
        self.lineEdit_placeOfDeath.setObjectName("lineEdit_placeOfDeath")
        self.verticalLayout_6.addWidget(self.lineEdit_placeOfDeath)
        self.horizontalLayout_2.addWidget(self.right_frame_3)
        self.verticalLayout_2.addWidget(self.frame_center_bottom)
        self.frame_bottom = QtWidgets.QFrame(self.main_frame)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 143))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 143))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_addinfo = QtWidgets.QLabel(self.frame_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_addinfo.setFont(font)
        self.label_addinfo.setStyleSheet("color: white;")
        self.label_addinfo.setAlignment(
            QtCore.Qt.AlignBottom
            | QtCore.Qt.AlignLeading
            | QtCore.Qt.AlignLeft
        )
        self.label_addinfo.setObjectName("label_addinfo")
        self.verticalLayout_7.addWidget(self.label_addinfo)
        self.plainTextEdit_addinfo = QtWidgets.QPlainTextEdit(
            self.frame_bottom
        )
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.plainTextEdit_addinfo.setFont(font)
        self.plainTextEdit_addinfo.setStyleSheet(
            "background-color: rgba(21, 22, 26, 255);\n"
            "color: rgb(190, 190, 190);\n"
            "border-radius: 10px;\n"
            "border-bottom: 2px solid rgba(80, 80, 85, 255);\n"
            "border-right: 2px solid rgba(80, 80, 85, 255);\n"
            "border-top: 2px solid rgba(80, 80, 85, 255);\n"
            "border-left: 2px solid rgba(80, 80, 85, 255);\n"
            "\n"
            ""
        )
        self.plainTextEdit_addinfo.setObjectName("plainTextEdit_addinfo")
        self.verticalLayout_7.addWidget(self.plainTextEdit_addinfo)
        self.verticalLayout_2.addWidget(self.frame_bottom)
        self.line = QtWidgets.QFrame(self.main_frame)
        self.line.setMinimumSize(QtCore.QSize(270, 4))
        self.line.setMaximumSize(QtCore.QSize(270, 4))
        self.line.setStyleSheet("Line{\n" "    color: rgb(21, 22, 26);\n" "}")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(
            self.line, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
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
        self.verticalLayout.addWidget(
            self.main_frame, 0, QtCore.Qt.AlignVCenter
        )

        as_needed = QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        self.comboBox_sex.view().setVerticalScrollBarPolicy(as_needed)

        self.retranslateUi(MyCard)
        QtCore.QMetaObject.connectSlotsByName(MyCard)

    def retranslateUi(self, MyCard):
        _translate = QtCore.QCoreApplication.translate
        MyCard.setWindowTitle(_translate("MyCard", "Моя картка"))
        self.label_lname.setText(
            _translate(
                "MyCard",
                '<html><head/><body><p>    Прізвище <span style=" color:#fb4938;">*</span></p></body></html>',
            )
        )
        self.label_note.setText(
            _translate(
                "MyCard",
                '<html><head/><body><p>Жіноче прізвище записується у форматі дівоче-чоловіче прізвище через дефіс. </p><p><span style=" color:#fd4837;">*</span> Обов\'язкові поля</p></body></html>',
            )
        )
        self.label_fname.setText(
            _translate(
                "MyCard",
                '<html><head/><body><p> Ім\'я <span style=" color:#fb4938;">*</span></p></body></html>',
            )
        )
        self.label_patronymic.setText(_translate("MyCard", "Ім'я по батькові"))
        self.label_sex.setText(_translate("MyCard", "Стать"))
        self.comboBox_sex.setItemText(0, _translate("MyCard", "Чоловіча"))
        self.comboBox_sex.setItemText(1, _translate("MyCard", "Жіноча"))
        self.label_yearOfBirth.setText(
            _translate(
                "MyCard",
                '<html><head/><body><p> Рік народження <span style=" color:#fb4938;">*</span></p></body></html>',
            )
        )
        self.label_yearOfDeath.setText(_translate("MyCard", "Рік смерті"))
        self.label_clanName.setText(
            _translate(
                "MyCard",
                '<html><head/><body><p>Прізвище роду <span style=" color:#fb4938;">*</span></p></body></html>',
            )
        )
        self.lineEdit_clanName.setPlaceholderText(
            _translate("MyCard", "В род. відм. множини")
        )
        self.label_placeOfBirth.setText(
            _translate("MyCard", "Місце народження")
        )
        self.lineEdit_placeOfBirth.setPlaceholderText(
            _translate("MyCard", "Населений пункт")
        )
        self.label_placeOfDeath.setText(_translate("MyCard", "Місце смерті"))
        self.lineEdit_placeOfDeath.setPlaceholderText(
            _translate("MyCard", "Населений пункт")
        )
        self.label_addinfo.setText(
            _translate("MyCard", " Додаткова інформація")
        )
        self.pushButton_done.setText(_translate("MyCard", "Готово"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MyCard = QtWidgets.QDialog()
    ui = UIMyCard()
    ui.setupUi(MyCard)
    MyCard.show()
    sys.exit(app.exec_())
