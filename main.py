import sys
from re import search
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as mesbox

from openpyxl import load_workbook
from PyQt5 import QtCore, QtGui, QtWidgets

from windows import (
    Ui_AddEdit,
    Ui_AddRemoveClan,
    Ui_FamilyTies,
    Ui_MainWindow,
    Ui_MyCard,
    Ui_Review,
)

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


varMy_cardWindow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
varAdd_editWindow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
varFamily_tiesWindow = [1, 2, 3, 4, 5, 6]


def my_card_def():
    # Create form and init ui
    MyCard = QtWidgets.QDialog()
    ui = Ui_MyCard()
    ui.setupUi(MyCard)
    MyCard.show()

    try:
        # Connect an Excel file
        wb = load_workbook("Family_lists.xlsx")
        ws = wb[wb.sheetnames[0]]

        # Check for the existence of information in the first line
        if ws["F1"].value != None:
            # Output data from the first line
            if ws["E1"].value == " Чоловіча":
                ui.comboBox_sex.setItemText(0, " Чоловіча")
            else:
                ui.comboBox_sex.setItemText(0, " Жіноча")
                ui.comboBox_sex.setItemText(1, " Чоловіча")

            ui.lineEdit_lname.setText(ws["F1"].value)
            ui.lineEdit_fname.setText(ws["G1"].value)
            ui.lineEdit_patronymic.setText(ws["H1"].value)
            ui.lineEdit_placeOfBirth.setText(ws["I1"].value)
            ui.lineEdit_placeOfDeath.setText(ws["J1"].value)
            ui.lineEdit_yearOfBirth.setText(ws["K1"].value)
            ui.lineEdit_yearOfDeath.setText(ws["L1"].value)
            ui.lineEdit_clanName.setText(ws.title)
            ui.plainTextEdit_addinfo.setPlainText(ws["M1"].value)

            # Output the thumbnail to the image_Button if the cell is not empty
            if ws["A1"].value != None:
                MAX_WIDTH, MAX_HEIGHT = resizeImage(ws.title, ws["A1"].value)
                icon = QtGui.QIcon()
                icon1 = QtGui.QIcon()
                icon1.addPixmap(
                    QtGui.QPixmap(ws["A1"].value),
                    QtGui.QIcon.Normal,
                    QtGui.QIcon.Off,
                )
                ui.image_Button.setIcon(icon1)
                ui.image_Button.setIconSize(
                    QtCore.QSize(MAX_WIDTH, MAX_HEIGHT)
                )
                icon.addPixmap(
                    QtGui.QPixmap(ws["A1"].value),
                    QtGui.QIcon.Normal,
                    QtGui.QIcon.Off,
                )
                MyCard.setWindowIcon(icon)

        # Image selection function
        def openImage():
            Tk().withdraw()
            file_name = fd.askopenfilename(
                filetypes=(
                    ("JPEG image", "*.jpeg;*.jpg"),
                    ("PNG image", "*.png"),
                )
            )

            if file_name != "":
                ws["A1"] = file_name
                MAX_WIDTH, MAX_HEIGHT = resizeImage(ws.title, ws["A1"].value)
                icon1 = QtGui.QIcon()
                icon1.addPixmap(
                    QtGui.QPixmap(ws["A1"].value),
                    QtGui.QIcon.Normal,
                    QtGui.QIcon.Off,
                )
                ui.image_Button.setIcon(icon1)
                ui.image_Button.setIconSize(
                    QtCore.QSize(MAX_WIDTH, MAX_HEIGHT)
                )

        # The function collects values ​​from line_Edit,
        # checks the conditions and writes the values ​​to file
        def returnToMainWindow():
            varMy_cardWindow[0] = ui.comboBox_sex.currentText()
            varMy_cardWindow[1] = ui.lineEdit_lname.text()
            varMy_cardWindow[2] = ui.lineEdit_fname.text()
            varMy_cardWindow[3] = ui.lineEdit_patronymic.text()
            varMy_cardWindow[4] = ui.lineEdit_placeOfBirth.text()
            varMy_cardWindow[5] = ui.lineEdit_placeOfDeath.text()
            varMy_cardWindow[6] = ui.lineEdit_yearOfBirth.text()
            varMy_cardWindow[7] = ui.lineEdit_yearOfDeath.text()
            varMy_cardWindow[8] = ui.plainTextEdit_addinfo.toPlainText()
            clanName = ui.lineEdit_clanName.text()

            if (
                varMy_cardWindow[1] == ""
                or varMy_cardWindow[2] == ""
                or varMy_cardWindow[6] == ""
                or clanName == ""
            ):
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!",
                    "Інформація не введена в одне з обов'язкових полів!",
                )
            elif search(r"[\\/?*]", clanName):
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!",
                    'В поле "Прізвище роду" введено недозволений символ!',
                )
            elif varMy_cardWindow[6].isdigit() == False:
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!", 'В поле "Рік ..." введено не цифри!'
                )
            elif (
                varMy_cardWindow[1][0] == " "
                or varMy_cardWindow[2][0] == " "
                or varMy_cardWindow[6][0] == " "
            ):
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!",
                    "Запис в одному з обов'язкових полів некоректний!",
                )
            else:
                if varMy_cardWindow[8] == "":
                    varMy_cardWindow[8] = " "

                i = 0
                for row in ws.iter_rows(
                    min_row=1, max_row=1, min_col=5, max_col=13
                ):
                    for cell in row:
                        cell.value = varMy_cardWindow[i]
                        i += 1
                ws.title = clanName

                ws["D1"] = (
                    varMy_cardWindow[1][0]
                    + varMy_cardWindow[2][0]
                    + varMy_cardWindow[6]
                )

                wb.save("Family_lists.xlsx")
                set_info_to_PB1()
                MyCard.close()
                MainWindow.show()

        ui.image_Button.clicked.connect(openImage)
        ui.pushButton_done.clicked.connect(returnToMainWindow)

    finally:
        wb.close()


def addRemove_clan_def():
    # Create form and init ui
    AddRemoveClan = QtWidgets.QDialog()
    ui = Ui_AddRemoveClan()
    ui.setupUi(AddRemoveClan)
    AddRemoveClan.show()

    wb = load_workbook("Family_lists.xlsx")
    # Loop to generate file sheet names
    for i in range(len(wb.sheetnames)):
        ui.comboBox_choiceRemoveClan.insertItem(i + 1, wb.sheetnames[i])

    wb.close()

    def returnToMainWindow():
        add_clan = ui.lineEdit_addClan.text()
        choice_rm_clan = ui.comboBox_choiceRemoveClan.currentText()

        wb = load_workbook("Family_lists.xlsx")

        if add_clan == "" and choice_rm_clan == "":
            wb.close()
            AddRemoveClan.close()
            MainWindow.show()
        elif search(r"[\\/?*]", add_clan):
            Tk().withdraw()
            mesbox.showerror(
                "Увага!", 'В поле "Додати рід" введено недозволений символ!'
            )
        elif choice_rm_clan != "" and len(wb.sheetnames) == 1:
            Tk().withdraw()
            mesbox.showerror(
                "Увага!",
                "Якщо рід в списку тільки один, \nто його не можна видаляти!",
            )
        else:
            # If the above conditions are not met, a new letter is created
            if add_clan != "":
                wb.create_sheet(add_clan)

            # or (and) the selected letter is deleted
            if choice_rm_clan != "":
                wb.remove(wb[choice_rm_clan])

                Tk().withdraw()
                mesbox.showinfo("", f"Рід {choice_rm_clan} видалено!")

            wb.save("Family_lists.xlsx")
            wb.close()

            AddRemoveClan.close()
            MainWindow.show()

    ui.pushButton_done.clicked.connect(returnToMainWindow)


def add_edit_def():
    # Create form and init ui
    AddEdit = QtWidgets.QDialog()
    ui = Ui_AddEdit()
    ui.setupUi(AddEdit)
    AddEdit.show()

    try:
        wb = load_workbook("Family_lists.xlsx")
        # Dynamic clan list generation
        for i in range(len(wb.sheetnames)):
            ui.comboBox_choiceClan.insertItem(i, wb.sheetnames[i])

        # Inserting data into window cells
        def insertingData():
            row_index = ui.comboBox_addEdit.currentIndex()
            if row_index == 0:
                ui.lineEdit_lname.clear()
                ui.lineEdit_fname.clear()
                ui.lineEdit_patronymic.clear()
                ui.lineEdit_placeOfBirth.clear()
                ui.lineEdit_placeOfDeath.clear()
                ui.lineEdit_yearOfBirth.clear()
                ui.lineEdit_yearOfDeath.clear()
                ui.plainTextEdit_addinfo.clear()

                icon1 = QtGui.QIcon()
                icon1.addPixmap(
                    QtGui.QPixmap(
                        "C:\\Users\\Hitar\\source\\Family_tree\\Icons/Add_image.png"
                    ),
                    QtGui.QIcon.Normal,
                    QtGui.QIcon.Off,
                )
                ui.image_Button.setIcon(icon1)
                ui.image_Button.setIconSize(QtCore.QSize(175, 175))
                ui.image_Button.setObjectName("image_Button")
            else:
                clan_index = ui.comboBox_choiceClan.currentIndex()
                sheet = wb[wb.sheetnames[clan_index]]
                if sheet[row_index][4].value == " Чоловіча":
                    ui.comboBox_sex.setItemText(0, " Чоловіча")
                else:
                    ui.comboBox_sex.setItemText(0, " Жіноча")
                    ui.comboBox_sex.setItemText(1, " Чоловіча")

                ui.lineEdit_lname.setText(sheet[row_index][5].value)
                ui.lineEdit_fname.setText(sheet[row_index][6].value)
                ui.lineEdit_patronymic.setText(sheet[row_index][7].value)
                ui.lineEdit_placeOfBirth.setText(sheet[row_index][8].value)
                ui.lineEdit_placeOfDeath.setText(sheet[row_index][9].value)
                ui.lineEdit_yearOfBirth.setText(sheet[row_index][10].value)
                ui.lineEdit_yearOfDeath.setText(sheet[row_index][11].value)
                ui.plainTextEdit_addinfo.setPlainText(
                    sheet[row_index][12].value
                )

                # Output the thumbnail to the image_Button if the cell is not empty
                if sheet[row_index][0].value != None:
                    MAX_WIDTH, MAX_HEIGHT = resizeImage(
                        sheet.title, sheet[row_index][0].value
                    )
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(
                        QtGui.QPixmap(sheet[row_index][0].value),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off,
                    )
                    ui.image_Button.setIcon(icon1)
                    ui.image_Button.setIconSize(
                        QtCore.QSize(MAX_WIDTH, MAX_HEIGHT)
                    )
                else:
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(
                        QtGui.QPixmap(
                            "C:\\Users\\Hitar\\source\\Family_tree\\Icons/Add_image.png"
                        ),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off,
                    )
                    ui.image_Button.setIcon(icon1)
                    ui.image_Button.setIconSize(QtCore.QSize(175, 175))
                    ui.image_Button.setObjectName("image_Button")

        # Dynamic generation of the list of persons of the selected clan
        def genInAddEditCombo():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]
            count = ui.comboBox_addEdit.count()

            if count > 1:
                ui.comboBox_addEdit.setCurrentIndex(0)
                for x in range(1, count):
                    ui.comboBox_addEdit.removeItem(1)
                count = 1
            if count == 1:
                if ws["F1"].value != None:
                    for y in range(1, ws.max_row + 1):
                        ui.comboBox_addEdit.insertItem(
                            y,
                            f"{ws[y][5].value} {ws[y][6].value}, {ws[y][10].value}",
                        )

            ui.comboBox_addEdit.currentIndexChanged.connect(insertingData)

        genInAddEditCombo()
        ui.comboBox_choiceClan.currentIndexChanged.connect(genInAddEditCombo)

        # Image selection function
        def openImage():
            Tk().withdraw()
            file_name = fd.askopenfilename(
                filetypes=(
                    ("JPEG image", "*.jpeg;*.jpg"),
                    ("PNG image", "*.png"),
                )
            )

            if file_name != "":
                clan_index = ui.comboBox_choiceClan.currentIndex()
                ws = wb[wb.sheetnames[clan_index]]
                row_index = ui.comboBox_addEdit.currentIndex()

                if row_index == 0:
                    if ws[ws.max_row][5].value == None:
                        line_number = ws.max_row
                    else:
                        line_number = ws.max_row + 1
                else:
                    line_number = row_index
                ws[line_number][0].value = file_name
                MAX_WIDTH, MAX_HEIGHT = resizeImage(
                    ws.title, ws[line_number][0].value
                )
                icon1 = QtGui.QIcon()
                icon1.addPixmap(
                    QtGui.QPixmap(ws[line_number][0].value),
                    QtGui.QIcon.Normal,
                    QtGui.QIcon.Off,
                )
                ui.image_Button.setIcon(icon1)
                ui.image_Button.setIconSize(
                    QtCore.QSize(MAX_WIDTH, MAX_HEIGHT)
                )

        def returnToMainWindow():
            # Read values ​​from all lineEdit cells
            varAdd_editWindow[0] = ui.comboBox_sex.currentText()
            varAdd_editWindow[1] = ui.lineEdit_lname.text()
            varAdd_editWindow[2] = ui.lineEdit_fname.text()
            varAdd_editWindow[3] = ui.lineEdit_patronymic.text()
            varAdd_editWindow[4] = ui.lineEdit_placeOfBirth.text()
            varAdd_editWindow[5] = ui.lineEdit_placeOfDeath.text()
            varAdd_editWindow[6] = ui.lineEdit_yearOfBirth.text()
            varAdd_editWindow[7] = ui.lineEdit_yearOfDeath.text()
            varAdd_editWindow[8] = ui.plainTextEdit_addinfo.toPlainText()

            clan_index = ui.comboBox_choiceClan.currentIndex()
            ws = wb[wb.sheetnames[clan_index]]
            row_index = ui.comboBox_addEdit.currentIndex()

            if (
                varAdd_editWindow[1] == ""
                or varAdd_editWindow[2] == ""
                or varAdd_editWindow[6] == ""
            ):
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!",
                    "Інформація не введена в одне з обов'язкових полів!",
                )
            elif varAdd_editWindow[6].isdigit() == False:
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!", 'В поле "Рік ..." введено не цифри!'
                )
            elif (
                varAdd_editWindow[1][0] == " "
                or varAdd_editWindow[2][0] == " "
                or varAdd_editWindow[6][0] == " "
            ):
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!",
                    "Запис в одному з обов'язкових полів некоректний!",
                )
            else:
                if varAdd_editWindow[8] == "":
                    varAdd_editWindow[8] = " "

                # If 'Add' is selected
                if row_index == 0:
                    if ws[ws.max_row][5].value == None:
                        line_number = ws.max_row
                    else:
                        line_number = ws.max_row + 1

                    # Write values ​​in the desired row and columns
                    i = 0
                    for row in ws.iter_rows(
                        min_row=line_number,
                        max_row=line_number,
                        min_col=5,
                        max_col=13,
                    ):
                        for cell in row:
                            cell.value = varAdd_editWindow[i]
                            i += 1

                    ws[ws.max_row][3].value = (
                        varAdd_editWindow[1][0]
                        + varAdd_editWindow[2][0]
                        + varAdd_editWindow[6]
                    )

                else:
                    i = 0
                    for row in ws.iter_rows(
                        min_row=row_index,
                        max_row=row_index,
                        min_col=5,
                        max_col=13,
                    ):
                        for cell in row:
                            cell.value = varAdd_editWindow[i]
                            i += 1

                    ws[row_index][3].value = (
                        varAdd_editWindow[1][0]
                        + varAdd_editWindow[2][0]
                        + varAdd_editWindow[6]
                    )

                wb.save("Family_lists.xlsx")
                set_info_to_PB1()
                AddEdit.close()
                MainWindow.show()

        ui.pushButton_done.clicked.connect(returnToMainWindow)
        ui.image_Button.clicked.connect(openImage)

    finally:
        wb.close()


def family_ties_def():
    FamilyTies = QtWidgets.QDialog()
    ui = Ui_FamilyTies()
    ui.setupUi(FamilyTies)
    FamilyTies.show()

    try:
        wb = load_workbook("Family_lists.xlsx")
        # Dynamic clan list generation
        for i in range(len(wb.sheetnames)):
            ui.comboBox_choiceClan.insertItem(i, wb.sheetnames[i])

        def tiesCheck():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]

            person_rowInd = ui.comboBox_choicePerson.currentIndex()

            if person_rowInd > 0:
                ui.comboBox_choiceFather.clear()
                ui.comboBox_choiceMother.clear()
                ui.tableWidget_BS.clear()
                ui.tableWidget_BS.setRowCount(0)
                ui.tableWidget_choiceChildren.clear()
                ui.tableWidget_choiceChildren.setRowCount(0)
                ui.comboBox_choicePartner.clear()

                # If a person has parents - find them
                if ws[person_rowInd][2].value != None:
                    parent_index = ws[person_rowInd][2].value
                    BS_row = 1

                    for n in range(1, ws.max_row + 1):
                        marriage_iter = ws[n][1].value

                        if (
                            parent_index == marriage_iter
                        ):  # If they are found ...
                            if (
                                ws[n][4].value == " Чоловіча"
                            ):  # and the first is the father,
                                ui.comboBox_choiceFather.insertItem(
                                    0,  # set it to the zero position of Box.
                                    f"{ws[n][5].value} {ws[n][6].value}, {ws[n][10].value}",
                                )

                                for f in range(
                                    1, ws.max_row + 1
                                ):  # After, generate all the others,
                                    if f != n:  # except him.
                                        ui.comboBox_choiceFather.insertItem(
                                            f,
                                            f"{ws[f][5].value} {ws[f][6].value}, {ws[f][10].value}",
                                        )
                                    else:
                                        ui.comboBox_choiceFather.insertItem(
                                            f, ""
                                        )

                            if ws[n][4].value == " Жіноча":
                                ui.comboBox_choiceMother.insertItem(
                                    0,
                                    f"{ws[n][5].value} {ws[n][6].value}, {ws[n][10].value}",
                                )

                                for m in range(1, ws.max_row + 1):
                                    if m != n:
                                        ui.comboBox_choiceMother.insertItem(
                                            m,
                                            f"{ws[m][5].value} {ws[m][6].value}, {ws[m][10].value}",
                                        )
                                    else:
                                        ui.comboBox_choiceMother.insertItem(
                                            m, ""
                                        )

                        # Generation of siblings in the table
                        BS_index = ws[n][2].value
                        if parent_index == BS_index and n != person_rowInd:
                            ui.tableWidget_BS.setRowCount(BS_row)
                            item = QtWidgets.QTableWidgetItem()
                            ui.tableWidget_BS.setItem(BS_row - 1, 0, item)
                            if n < 10:
                                item.setText(
                                    f"0{n}, {ws[n][5].value} {ws[n][6].value}, {ws[n][10].value}"
                                )
                            else:
                                item.setText(
                                    f"{n}, {ws[n][5].value} {ws[n][6].value}, {ws[n][10].value}"
                                )
                            BS_row += 1

                else:
                    ui.comboBox_choiceFather.insertItem(0, "")
                    for f in range(1, ws.max_row + 1):
                        ui.comboBox_choiceFather.insertItem(
                            f,
                            f"{ws[f][5].value} {ws[f][6].value}, {ws[f][10].value}",
                        )

                    ui.comboBox_choiceMother.insertItem(0, "")
                    for m in range(1, ws.max_row + 1):
                        ui.comboBox_choiceMother.insertItem(
                            m,
                            f"{ws[m][5].value} {ws[m][6].value}, {ws[m][10].value}",
                        )

                # If the marriage cell in person is not empty
                if ws[person_rowInd][1].value != None:
                    marriage_index = ws[person_rowInd][1].value
                    children_row = 1

                    for c in range(1, ws.max_row + 1):
                        children_index = ws[c][2].value

                        if marriage_index == children_index:
                            ui.tableWidget_choiceChildren.setRowCount(
                                children_row
                            )  # generate a list of children
                            item = (
                                QtWidgets.QTableWidgetItem()
                            )  # in the table,
                            ui.tableWidget_choiceChildren.setItem(
                                children_row - 1, 0, item
                            )
                            if c < 10:
                                item.setText(
                                    f"0{c}, {ws[c][5].value} {ws[c][6].value}, {ws[c][10].value}"
                                )
                            else:
                                item.setText(
                                    f"{c}, {ws[c][5].value} {ws[c][6].value}, {ws[c][10].value}"
                                )
                            children_row += 1

                        marriage_iter2 = ws[c][1].value
                        if (
                            marriage_index == marriage_iter2
                            and c != person_rowInd
                        ):
                            ui.comboBox_choicePartner.insertItem(
                                0,  # and show a partner.
                                f"{ws[c][5].value} {ws[c][6].value}, {ws[c][10].value}",
                            )

                            for p in range(1, ws.max_row + 1):
                                if p != c:
                                    ui.comboBox_choicePartner.insertItem(
                                        p,
                                        f"{ws[p][5].value} {ws[p][6].value}, {ws[p][10].value}",
                                    )
                                else:
                                    ui.comboBox_choicePartner.insertItem(p, "")
                    if ui.comboBox_choicePartner.currentIndex() == -1:
                        ui.comboBox_choicePartner.insertItem(0, "")
                        for p in range(1, ws.max_row + 1):
                            ui.comboBox_choicePartner.insertItem(
                                p,
                                f"{ws[p][5].value} {ws[p][6].value}, {ws[p][10].value}",
                            )

                else:
                    ui.comboBox_choicePartner.insertItem(0, "")
                    for p in range(1, ws.max_row + 1):
                        ui.comboBox_choicePartner.insertItem(
                            p,
                            f"{ws[p][5].value} {ws[p][6].value}, {ws[p][10].value}",
                        )

        # Dynamic generation of the list of persons of the selected clan in all ComboBoxes
        def genInSomeCombo():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]
            count = ui.comboBox_choicePerson.count()

            if count > 1:
                ui.comboBox_choicePerson.setCurrentIndex(0)
                for x in range(1, count):
                    ui.comboBox_choicePerson.removeItem(1)

                ui.comboBox_choiceFather.clear()
                ui.comboBox_choiceMother.clear()
                ui.comboBox_choiceBS.clear()
                ui.tableWidget_BS.clear()
                ui.tableWidget_BS.setRowCount(0)
                ui.comboBox_choicePartner.clear()
                ui.comboBox_choiceChildren.clear()
                ui.tableWidget_choiceChildren.setRowCount(0)
                ui.tableWidget_choiceChildren.clear()
                count = 1

            if count == 1 and ws["F1"].value != None:
                for y in range(1, ws.max_row + 1):
                    ui.comboBox_choicePerson.insertItem(
                        y,
                        f"{ws[y][5].value} {ws[y][6].value}, {ws[y][10].value}",
                    )

                    ui.comboBox_choiceBS.insertItem(
                        y - 1,
                        f"{ws[y][5].value} {ws[y][6].value}, {ws[y][10].value}",
                    )

                    ui.comboBox_choiceChildren.insertItem(
                        y - 1,
                        f"{ws[y][5].value} {ws[y][6].value}, {ws[y][10].value}",
                    )

            ui.comboBox_choicePerson.currentIndexChanged.connect(tiesCheck)

        genInSomeCombo()
        ui.comboBox_choiceClan.currentIndexChanged.connect(genInSomeCombo)

        # Add siblings function
        def addBS():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]

            BS_index = (
                ui.comboBox_choiceBS.currentIndex() + 1
            )  # Get the row index in the file,
            rowCount = ui.tableWidget_BS.rowCount()  # and the number of rows
            # in the table.
            ui.tableWidget_BS.setRowCount(rowCount + 1)
            item = QtWidgets.QTableWidgetItem()
            ui.tableWidget_BS.setItem(rowCount, 0, item)
            if BS_index < 10:  # The person index must consist
                item.setText(
                    f"0{BS_index}, {ws[BS_index][5].value} {ws[BS_index][6].value}, {ws[BS_index][10].value}"
                )
            else:
                item.setText(
                    f"{BS_index}, {ws[BS_index][5].value} {ws[BS_index][6].value}, {ws[BS_index][10].value}"
                )

        def addChildren():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]

            Children_index = ui.comboBox_choiceChildren.currentIndex() + 1
            rowCount = ui.tableWidget_choiceChildren.rowCount()

            ui.tableWidget_choiceChildren.setRowCount(rowCount + 1)
            item = QtWidgets.QTableWidgetItem()
            ui.tableWidget_choiceChildren.setItem(rowCount, 0, item)
            if Children_index < 10:
                item.setText(
                    f"0{Children_index}, {ws[Children_index][5].value} {ws[Children_index][6].value}, {ws[Children_index][10].value}"
                )
            else:
                item.setText(
                    f"{Children_index}, {ws[Children_index][5].value} {ws[Children_index][6].value}, {ws[Children_index][10].value}"
                )

        def returnToMainWindow():
            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]

            varFam_t_tab_BS = []
            varFam_t_tab_Chd = []

            choicePerson_ind = ui.comboBox_choicePerson.currentIndex()
            choicePerson_text = ui.comboBox_choicePerson.currentText()
            choicePartner_ind = ui.comboBox_choicePartner.currentIndex()
            choicePartner_text = ui.comboBox_choicePartner.currentText()
            choiceFather_ind = ui.comboBox_choiceFather.currentIndex()
            choiceFather_text = ui.comboBox_choiceFather.currentText()
            choiceMother_ind = ui.comboBox_choiceMother.currentIndex()
            choiceMother_text = ui.comboBox_choiceMother.currentText()
            rowCount_BS = ui.tableWidget_BS.rowCount()
            rowCount_Children = ui.tableWidget_choiceChildren.rowCount()

            if rowCount_BS > 0:
                for t in range(rowCount_BS):
                    if ui.tableWidget_BS.item(t, 0).text() != "":
                        varFam_t_tab_BS.append(
                            ui.tableWidget_BS.item(t, 0).text()
                        )

            if rowCount_Children > 0:
                for t in range(rowCount_Children):
                    if ui.tableWidget_choiceChildren.item(t, 0).text() != "":
                        varFam_t_tab_Chd.append(
                            ui.tableWidget_choiceChildren.item(t, 0).text()
                        )

            # Check conditions
            if rowCount_BS > 0 and rowCount_Children > 0:
                for b in range(len(varFam_t_tab_BS)):
                    for c in range(len(varFam_t_tab_Chd)):
                        if varFam_t_tab_BS[b] == varFam_t_tab_Chd[c]:
                            Tk().withdraw()
                            mesbox.showerror(
                                "Увага!",
                                'В таблиці "Брати/Сестри" і "Діти" \
                                \nзнайдено однакові елементи!',
                            )
                            return

            if choicePerson_ind == 0:
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!",
                    "Не вибрано, для кого встановити \nсімейні рв'язки!",
                )
            elif (choiceFather_text != "" and choiceMother_text == "") or (
                choiceFather_text == "" and choiceMother_text != ""
            ):
                Tk().withdraw()
                mesbox.showerror("Увага!", "Не додано одного з батьків!")
            elif (
                choiceFather_text == choiceMother_text
                and choiceFather_ind != 0
            ):
                Tk().withdraw()
                mesbox.showerror("Увага!", "Вибрано однакових батьків!")
            elif (
                choiceFather_ind != 0
                and ws[choiceFather_ind][10].value
                > ws[choicePerson_ind][10].value
            ):
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!", 'В поле "Батько" встановлено некоректну особу!'
                )
            elif (
                choiceMother_ind != 0
                and ws[choiceMother_ind][10].value
                > ws[choicePerson_ind][10].value
            ):
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!", 'В поле "Мати" встановлено некоректну особу!'
                )
            elif (
                choiceFather_ind != 0
                and choiceMother_ind != 0
                and ws[choiceFather_ind][1].value
                != ws[choiceMother_ind][1].value
            ):
                Tk().withdraw()
                mesbox.showwarning("Увага!", "Батько або Мати вже в шлюбі!")
            elif choicePartner_text == choicePerson_text:
                Tk().withdraw()
                mesbox.showerror(
                    "Увага!",
                    'Поля "Встановити сімейні зв\'зки для" \
                                    \n і "Партнер" не можуть бути однакові!',
                )
            elif (
                varFam_t_tab_BS != []
                and choiceFather_text == ""
                or choiceMother_text == ""
            ):
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!",
                    "Не можна додавати братів чи сестер, \nпоки не вибрано батьків!",
                )
            elif (
                varFam_t_tab_Chd != []
                and choicePartner_ind == 0
                and choicePartner_text == ""
            ):
                Tk().withdraw()
                mesbox.showwarning(
                    "Увага!",
                    "Не можна додавати дітей, \nпоки не вибрано партнера!",
                )

            else:

                def setChildren(marriage):
                    # If the children's table is not empty,
                    if varFam_t_tab_Chd != []:
                        for c in range(
                            len(varFam_t_tab_Chd)
                        ):  # go through the list with children,
                            chd_row_ind = int(
                                varFam_t_tab_Chd[c][0:2]
                            )  # and everyone read the index
                            # of the string in the file.
                            # If the child's year of birth is less than the person's - show error
                            if int(ws[chd_row_ind][10].value) < int(
                                ws[choicePerson_ind][10].value
                            ):
                                Tk().withdraw()
                                mesbox.showerror(
                                    "Увага!",
                                    f"{ws[chd_row_ind][5].value} {ws[chd_row_ind][6].value} \
                                                \nне може бути Вашою дитиною!",
                                )
                            elif (
                                ws[chd_row_ind][2].value != None
                                and ws[chd_row_ind][2].value != marriage
                            ):
                                Tk().withdraw()
                                mesbox.showerror(
                                    "Увага!",
                                    f"{ws[chd_row_ind][5].value} {ws[chd_row_ind][6].value} \
                                                \nвже є чиєюсь дитиною!",
                                )
                            else:
                                ws[chd_row_ind][2].value = marriage

                # If the partner has not changed
                if choicePartner_ind == 0 and choicePartner_text != "":
                    marriage = ws[choicePerson_ind][1].value
                    setChildren(marriage)

                elif choicePartner_ind != 0 or choicePartner_text != "":
                    # If the person is married,
                    if ws[choicePerson_ind][1].value != None:
                        person_ind = ws[choicePerson_ind][3].value
                        partner_ind = ws[choicePartner_ind][3].value
                        marriage = (
                            person_ind + partner_ind
                        )  # add new person and partner indexes,

                        old_marriage = ws[choicePerson_ind][1].value
                        for p in range(1, ws.max_row + 1):
                            marriage_ind = ws[p][1].value
                            parents_ind = ws[p][2].value

                            if old_marriage == marriage_ind:
                                ws[p][1].value = None  # delete old marriage,
                            if (
                                old_marriage == parents_ind
                            ):  # overwrite the new index
                                ws[p][
                                    2
                                ].value = marriage  # for existing children,

                        ws[choicePerson_ind][
                            1
                        ].value = marriage  # and set a new index in the
                        ws[choicePartner_ind][
                            1
                        ].value = marriage  # marriage cells.
                        setChildren(marriage)

                    else:
                        person_ind = ws[choicePerson_ind][3].value
                        partner_ind = ws[choicePartner_ind][3].value
                        marriage = person_ind + partner_ind
                        ws[choicePerson_ind][1].value = marriage
                        ws[choicePartner_ind][1].value = marriage
                        setChildren(marriage)

                def setBS(marriage, father_row_ind):
                    # If the BS table is not empty,
                    if varFam_t_tab_BS != []:
                        for s in range(
                            len(varFam_t_tab_BS)
                        ):  # go through the list with siblings,
                            BS_row_ind = int(
                                varFam_t_tab_BS[s][0:2]
                            )  # and everyone read the index
                            # of the string in the file.
                            # If the siblings year of birth is less than the person's - show error.
                            if int(ws[BS_row_ind][10].value) < int(
                                ws[father_row_ind][10].value
                            ):
                                Tk().withdraw()
                                mesbox.showerror(
                                    "Увага!",
                                    f"{ws[BS_row_ind][5].value} {ws[BS_row_ind][6].value} \
                                \nне може бути Вашим братом чи сестрою!",
                                )
                            elif (
                                ws[BS_row_ind][2].value != None
                                and ws[BS_row_ind][2].value != marriage
                            ):
                                Tk().withdraw()
                                mesbox.showerror(
                                    "Увага!",
                                    f"{ws[BS_row_ind][5].value} {ws[BS_row_ind][6].value} \
                                \nвже є чиїмось братом чи сестрою!",
                                )
                            elif (
                                BS_row_ind == choicePerson_ind
                                or BS_row_ind == choicePartner_ind
                                or BS_row_ind == choiceFather_ind
                                or BS_row_ind == choiceMother_ind
                                or BS_row_ind
                                == ui.comboBox_choiceFather.findText("")
                                or BS_row_ind
                                == ui.comboBox_choiceMother.findText("")
                                or BS_row_ind
                                == ui.comboBox_choicePartner.findText("")
                            ):
                                Tk().withdraw()
                                mesbox.showerror(
                                    "Увага!",
                                    'Особа в списку "Брати/Сестри" співпадає \
                                з якимось із членів сім\'ї!',
                                )
                            else:
                                ws[BS_row_ind][2].value = marriage

                # If a father and mother are selected
                if (choiceFather_ind != 0 and choiceFather_text != "") and (
                    choiceMother_ind != 0 and choiceMother_text != ""
                ):
                    father_ind = ws[choiceFather_ind][3].value
                    mother_ind = ws[choiceMother_ind][3].value
                    marriage = father_ind + mother_ind
                    ws[choiceFather_ind][1].value = marriage
                    ws[choiceMother_ind][1].value = marriage
                    if (
                        ws[choicePerson_ind][2].value != None
                        and ws[choicePerson_ind][2].value != marriage
                    ):
                        Tk().withdraw()
                        mesbox.showerror(
                            "Увага!",
                            f"{ws[choicePerson_ind][5].value} {ws[choicePerson_ind][6].value} \
                                        \nвже є чиїмось братом чи сестрою!",
                        )
                    else:
                        ws[choicePerson_ind][2].value = marriage

                    setBS(marriage, choiceFather_ind)

                # If the father and mother are generated and have not changed
                elif (choiceFather_ind == 0 and choiceFather_text != "") and (
                    choiceMother_ind == 0 and choiceMother_text != ""
                ):
                    father_row_ind = ui.comboBox_choiceFather.findText("")
                    marriage = ws[father_row_ind][1].value
                    setBS(marriage, father_row_ind)

                # If either the father or the mother has changed
                elif (choiceFather_ind == 0 and choiceMother_ind != 0) or (
                    choiceMother_ind == 0 and choiceFather_ind != 0
                ):
                    if choiceFather_ind == 0 and choiceMother_ind != 0:
                        father_ind = ws[ui.comboBox_choiceFather.findText("")][
                            3
                        ].value
                        mother_ind = ws[choiceMother_ind][3].value
                        old_marriage = ws[
                            ui.comboBox_choiceFather.findText("")
                        ][1].value
                    else:
                        father_ind = ws[choiceFather_ind][3].value
                        mother_ind = ws[ui.comboBox_choiceMother.findText("")][
                            3
                        ].value
                        old_marriage = ws[
                            ui.comboBox_choiceMother.findText("")
                        ][1].value

                    marriage = (
                        father_ind + mother_ind
                    )  # add new person and partner indexes,

                    for p in range(1, ws.max_row + 1):
                        marriage_ind = ws[p][1].value
                        parents_ind = ws[p][2].value

                        if old_marriage == marriage_ind:
                            ws[p][1].value = None  # delete old marriage,
                        if (
                            old_marriage == parents_ind
                        ):  # overwrite the new index
                            ws[p][2].value = marriage  # for existing children,

                    # and set a new index in the marriage cells.
                    if choiceFather_ind == 0 and choiceMother_ind != 0:
                        ws[ui.comboBox_choiceFather.findText("")][
                            1
                        ].value = marriage
                        ws[choiceMother_ind][1].value = marriage
                        father_row_ind = ui.comboBox_choiceFather.findText("")
                    else:
                        ws[choiceFather_ind][1].value = marriage
                        ws[ui.comboBox_choiceMother.findText("")][
                            1
                        ].value = marriage
                        father_row_ind = choiceFather_ind

                    setBS(marriage, father_row_ind)

                wb.save("Family_lists.xlsx")
                FamilyTies.close()
                MainWindow.show()

            varFam_t_tab_BS.clear()
            varFam_t_tab_Chd.clear()

        ui.pushButton_done.clicked.connect(returnToMainWindow)
        ui.pushButton_addBS.clicked.connect(addBS)
        ui.pushButton_addChildren.clicked.connect(addChildren)

    finally:
        wb.close()


def review_def():
    Review = QtWidgets.QDialog()
    ui = Ui_Review()
    ui.setupUi(Review)
    Review.show()

    try:
        wb = load_workbook("Family_lists.xlsx")
        # Dynamic clan list generation
        for i in range(len(wb.sheetnames)):
            ui.comboBox_choiceClan.insertItem(i, wb.sheetnames[i])

        def genInTable():
            # Delete content before outputting information
            ui.tableWidget.clearContents()

            clanName = ui.comboBox_choiceClan.currentText()
            ws = wb[clanName]
            max_file_row = ws.max_row

            # Set as many rows in the table as in the file
            ui.tableWidget.setRowCount(max_file_row)

            row_ind = col_ind = 0
            for row_cells in ws.iter_rows(
                min_col=5, max_col=13
            ):  # Read one row from the file,
                for cell in row_cells:  # and write in one cell of
                    item = (
                        QtWidgets.QTableWidgetItem()
                    )  # the table one value from
                    ui.tableWidget.setItem(
                        row_ind, col_ind, item
                    )  # the read tuple (row).
                    item.setText(cell.value)
                    col_ind += 1

                row_ind += 1
                col_ind = 0

        genInTable()
        ui.comboBox_choiceClan.currentIndexChanged.connect(genInTable)

        def returnToMainWindow():
            Review.close()
            MainWindow.show()

        ui.pushButton_done.clicked.connect(returnToMainWindow)

    finally:
        wb.close()


def resizeImage(clan_Name, cell):
    from PIL import Image

    wb = load_workbook("Family_lists.xlsx")
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


# Set the lables in the My_card buttom
def set_info_to_PB1():
    wb = load_workbook("Family_lists.xlsx")
    ws = wb[wb.sheetnames[0]]

    clan_name = ws.title
    first_name = ws["G1"].value
    last_name = ws["F1"].value
    ui.my_data = f"Рід: {clan_name}" f"\n{first_name} {last_name}"
    ui.pushButton_1.setText(ui.my_data)

    if ws["A1"].value != None:
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(ws["A1"].value), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        ui.pushButton_1.setIcon(icon1)

    wb.close()


# Condition of pressing buttons
ui.pushButton_1.clicked.connect(my_card_def)
ui.pushButton_2.clicked.connect(addRemove_clan_def)
ui.pushButton_3.clicked.connect(add_edit_def)
ui.pushButton_4.clicked.connect(family_ties_def)
ui.pushButton_5.clicked.connect(review_def)

# Check for the entry into the program
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


app.exec()
