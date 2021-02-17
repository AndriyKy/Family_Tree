from PyQt5 import QtCore, QtGui, QtWidgets
from Main_window import Ui_MainWindow
from openpyxl import load_workbook
from tkinter import messagebox as mesbox
from tkinter import filedialog as fd
from tkinter import Tk
from tkinter import *

import Resource_rc
import sys 

## ==> CREATE MAIN APP
app = QtWidgets.QApplication(sys.argv)

## ==> CREATE FORT AND INIT UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


## ==> LOGIC

## Variables 
varMy_cardWindows = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

def my_card_def():
    from My_card import Ui_MyCard
    MyCard = QtWidgets.QDialog()
    ui = Ui_MyCard()
    ui.setupUi(MyCard)
    MyCard.show()

    wb = load_workbook('Family_lists.xlsx')
    ws = wb.active

    if ws['F1'].value != None:
        if ws['E1'].value == " Чоловіча":
            ui.comboBox_sex.setItemText(0, " Чоловіча")
        else:
            ui.comboBox_sex.setItemText(0, " Жіноча")
            ui.comboBox_sex.setItemText(1, " Чоловіча")
        
        ui.lineEdit_lname.setText(ws['F1'].value)
        ui.lineEdit_fname.setText(ws['G1'].value)
        ui.lineEdit_patronymic.setText(ws['H1'].value)
        ui.lineEdit_placeOfBirth.setText(ws['I1'].value)
        ui.lineEdit_placeOfDeath.setText(ws['J1'].value)
        ui.lineEdit_yearOfBirth.setText(ws['K1'].value)
        ui.lineEdit_yearOfDeath.setText(ws['L1'].value)
        ui.lineEdit_clanName.setText(ws.title)
        ui.plainTextEdit_addinfo.setPlainText(ws['M1'].value)

        if ws['A1'].value != None:
            MAX_WIDTH, MAX_HEIGHT = resizeImage(ws.title, ws['A1'].value)
            icon = QtGui.QIcon()
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(ws['A1'].value), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.image_Button.setIcon(icon1)
            ui.image_Button.setIconSize(QtCore.QSize(MAX_WIDTH, MAX_HEIGHT))
            icon.addPixmap(QtGui.QPixmap(ws['A1'].value), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MyCard.setWindowIcon(icon)
    wb.close()

    def openImage():
        Tk().withdraw()
        file_name = fd.askopenfilename(
            filetypes=(("JPEG image", "*.jpeg;*.jpg"),
                            ("PNG image", "*.png")))
        
        if file_name != "":    
            wb = load_workbook('Family_lists.xlsx')
            ws = wb.active

            ws['A1'] = file_name
            MAX_WIDTH, MAX_HEIGHT = resizeImage(ws.title, ws['A1'].value)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(ws['A1'].value), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.image_Button.setIcon(icon1)
            ui.image_Button.setIconSize(QtCore.QSize(MAX_WIDTH, MAX_HEIGHT))

            wb.save('Family_lists.xlsx')
            wb.close()

    ui.image_Button.clicked.connect(openImage)

    def returnToMainWindow():
        varMy_cardWindows[0] = ui.comboBox_sex.currentText()
        varMy_cardWindows[1] = ui.lineEdit_lname.text()
        varMy_cardWindows[2] = ui.lineEdit_fname.text()
        varMy_cardWindows[3] = ui.lineEdit_patronymic.text()
        varMy_cardWindows[4] = ui.lineEdit_placeOfBirth.text()
        varMy_cardWindows[5] = ui.lineEdit_placeOfDeath.text()
        varMy_cardWindows[6] = ui.lineEdit_yearOfBirth.text()
        varMy_cardWindows[7] = ui.lineEdit_yearOfDeath.text()
        varMy_cardWindows[8] = ui.plainTextEdit_addinfo.toPlainText()
        clanName = ui.lineEdit_clanName.text()

        if varMy_cardWindows[1] == "" or varMy_cardWindows[2] == "" or varMy_cardWindows[6] == "" or clanName == "":
            Tk().withdraw()
            mesbox.showwarning("Увага!", "Інформація не введена в одне з обов'язкових полів!")
        elif varMy_cardWindows[6].isdigit() == False:
            Tk().withdraw()
            mesbox.showwarning("Увага!", "В поле \"Рік ...\" введено не цифри!")
        elif varMy_cardWindows[1][0] == " " or varMy_cardWindows[2][0] == " " or varMy_cardWindows[6][0] == " ":
            Tk().withdraw()
            mesbox.showerror("Увага!", "Запис в одному з обов'язкових полів некоректний!")
        else:
            wb = load_workbook('Family_lists.xlsx')
            ws = wb.active
            i = 0
            for row in ws.iter_rows(min_row=1, max_row=1, min_col = 5, max_col=13):
                for cell in row:
                    cell.value = varMy_cardWindows[i]
                    i += 1
            ws.title = clanName

            ws['D1'] = varMy_cardWindows[1][0] + varMy_cardWindows[2][0] + varMy_cardWindows[6]
            wb.save('Family_lists.xlsx')
            wb.close()

            set_info_to_PB1()
            MyCard.close()
            MainWindow.show()

    ui.pushButton_done.clicked.connect(returnToMainWindow)

def resizeImage(clan_Name, cell):
    from PIL import Image
    wb = load_workbook('Family_lists.xlsx')
    ws = wb[clan_Name]

    image = Image.open(cell)
    im_size = image.size

    if im_size[0] > im_size[1]:
        MAX_WIDTH = 175
        MAX_HEIGHT = (MAX_WIDTH * im_size[1]) // im_size[0] 
    elif im_size[0] < im_size[1]:
        MAX_HEIGHT = 175
        MAX_WIDTH = (MAX_HEIGHT * im_size[0]) // im_size[1]
    else:
        MAX_WIDTH = MAX_HEIGHT = 175
    
    wb.close()
    return (MAX_WIDTH, MAX_HEIGHT)
     

def set_info_to_PB1():
    ## Set the lables in the My_card buttom
    wb = load_workbook('Family_lists.xlsx')
    ws = wb.active
           
    clan_name = ws.title
    first_name = ws['G1'].value
    last_name = ws['F1'].value
    ui.my_data = f"Рід: {clan_name}" f"\n{first_name} {last_name}"
    ui.pushButton_1.setText(ui.my_data)

    if ws['A1'].value != None:
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(ws['A1'].value), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.pushButton_1.setIcon(icon1)

    wb.close()


def add_edit_def():
    from Add_edit import Ui_AddEdit
    AddEdit = QtWidgets.QDialog()
    ui = Ui_AddEdit()
    ui.setupUi(AddEdit)
    AddEdit.show()

    def returnToMainWindow():
        AddEdit.close()
        MainWindow.show()
    ui.pushButton_done.clicked.connect(returnToMainWindow)

def family_ties_def():
    from Family_ties import Ui_FamilyTies
    FamilyTies = QtWidgets.QDialog()
    ui = Ui_FamilyTies()
    ui.setupUi(FamilyTies)
    FamilyTies.show()

    def returnToMainWindow():
        FamilyTies.close()
        MainWindow.show()
    ui.pushButton_done.clicked.connect(returnToMainWindow)

def addSelect_clan_def():
    from AddSelect_clan import Ui_AddSelectClan
    AddSelectClan = QtWidgets.QDialog()
    ui = Ui_AddSelectClan()
    ui.setupUi(AddSelectClan)
    AddSelectClan.show()

    def returnToMainWindow():
        clan_name = ui.lineEdit_addClan.text()
     
        AddSelectClan.close()
        MainWindow.show()
    ui.pushButton_done.clicked.connect(returnToMainWindow)

def review_def():
    from Review import Ui_Review
    Review = QtWidgets.QDialog()
    ui = Ui_Review()
    ui.setupUi(Review)
    Review.show()
    
    def returnToMainWindow():
            Review.close()
            MainWindow.show()
    ui.pushButton_done.clicked.connect(returnToMainWindow)

## Condition of pressing buttons
ui.pushButton_1.clicked.connect(my_card_def)
ui.pushButton_2.clicked.connect(add_edit_def)
ui.pushButton_3.clicked.connect(family_ties_def)
ui.pushButton_4.clicked.connect(addSelect_clan_def)
ui.pushButton_5.clicked.connect(review_def)


## Check for the entry into the program
try:
    counter = open("counter.txt", "r")
    text_counter = counter.read()
    if text_counter == "0":
        my_card_def()
    else:
        set_info_to_PB1()

    counter.close()
    counter = open("counter.txt", "w")
    counter.write("1")
finally:
    counter.close()


## ==> RUN MAIN LOOP
sys.exit(app.exec_())
