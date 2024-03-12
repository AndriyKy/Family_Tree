import sys
from os.path import join as join_path
from re import search
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as msbox
from typing import Any

from openpyxl import Workbook, load_workbook
from PIL import Image
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

main_window = QtWidgets.QMainWindow()
ui_main_window = Ui_MainWindow()
ui_main_window.setupUi(main_window)
main_window.show()

WORKBOOK_NAME = "Family_lists.xlsx"


class WindowConstructor(QtWidgets.QDialog):
    def __init__(
        self,
        window: type[
            Ui_AddEdit
            | Ui_AddRemoveClan
            | Ui_FamilyTies
            | Ui_MainWindow
            | Ui_MyCard
            | Ui_Review
        ],
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ui_window = window()
        self.ui_window.setupUi(self)

    def openEvent(self) -> None:
        self.workbook = load_workbook(WORKBOOK_NAME)
        self.show()

    def closeEvent(self, *args: Any) -> None:
        self.workbook.save(WORKBOOK_NAME)
        self.workbook.close()
        super().closeEvent(*args)

    @staticmethod
    def resize_image(file_path) -> tuple[int, int]:
        image = Image.open(file_path)
        width, height = image.size
        max_width = max_height = 175

        if width > height:
            max_height = (max_width * height) // width
        elif width < height:
            max_width = (max_height * width) // height

        return max_width, max_height

    def fetch_image_path(self) -> str | None:
        return (
            fd.askopenfilename(
                filetypes=(
                    ("JPEG image", ["*.jpeg", "*.jpg", "*.JPG"]),
                    ("PNG image", "*.png"),
                )
            )
            or None  # `askopenfilename` returns `()` if nothing is selected.
        )

    @staticmethod
    def is_input_valid(family_member: dict[str, str]) -> bool:
        if (
            not family_member["last_name"]
            or not family_member["first_name"]
            or not family_member["year_of_birth"]
            or not family_member["family_name"]
        ):
            msbox.showwarning(
                "Увага!",
                "Інформація не введена в одне з обов'язкових полів!",
            )
        elif any(
            search(r"[:\/\*\?[\]<>|]", item) for item in family_member.values()
        ):
            msbox.showerror(
                "Увага!",
                "Заборонено вводити такі символи: / \ * ? [ ] < > : |",
            )
        elif not family_member["year_of_birth"].isdigit() or (
            family_member["year_of_death"]
            and not family_member["year_of_death"].isdigit()
        ):
            msbox.showwarning("Увага!", 'В поле "Рік ..." введено не цифри!')
        else:
            return True
        return False

    def set_icon(self, image_path: str) -> None:
        width, height = resize_image(image_path)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.ui_window.image_Button.setIcon(icon)
        self.ui_window.image_Button.setIconSize(QtCore.QSize(width, height))


class MyCard(WindowConstructor):
    def __init__(self) -> None:
        super().__init__(Ui_MyCard)

    def openEvent(self) -> None:
        super().openEvent()
        self.worksheet = self.workbook.active
        self.fill_window()

    def fill_window(self) -> None:
        # Check for the existence of information in the first line.
        if self.worksheet["F1"].value:
            if image_path := self.worksheet["A1"].value:
                self.set_icon(image_path)
            if self.worksheet["E1"].value == "Чоловіча":
                self.ui_window.comboBox_sex.setItemText(0, "Чоловіча")
            else:
                self.ui_window.comboBox_sex.setItemText(0, "Жіноча")
                self.ui_window.comboBox_sex.setItemText(1, "Чоловіча")

            self.ui_window.lineEdit_lname.setText(self.worksheet["F1"].value)
            self.ui_window.lineEdit_fname.setText(self.worksheet["G1"].value)
            self.ui_window.lineEdit_patronymic.setText(
                self.worksheet["H1"].value
            )
            self.ui_window.lineEdit_placeOfBirth.setText(
                self.worksheet["I1"].value
            )
            self.ui_window.lineEdit_placeOfDeath.setText(
                self.worksheet["J1"].value
            )
            self.ui_window.lineEdit_yearOfBirth.setText(
                self.worksheet["K1"].value
            )
            self.ui_window.lineEdit_yearOfDeath.setText(
                self.worksheet["L1"].value
            )
            self.ui_window.lineEdit_clanName.setText(self.worksheet.title)
            self.ui_window.plainTextEdit_addinfo.setPlainText(
                self.worksheet["M1"].value
            )

    def set_avatar(self) -> None:
        image_path = self.fetch_image_path()
        if image_path:
            self.worksheet["A1"] = image_path
            self.set_icon(image_path)

    def set_my_card_button_label(self) -> None:
        ui_main_window.pushButton_1.setText(
            f'Рід: {self.worksheet.title}\n'
            f'{self.worksheet["G1"].value} {self.worksheet["F1"].value}'
        )

        if image_path := self.worksheet["A1"].value:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(
                QtGui.QPixmap(image_path),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )

            ui_main_window.pushButton_1.setIcon(icon1)

    def save(self) -> None:
        family_member = {
            "sex": self.ui_window.comboBox_sex.currentText().strip(),
            "last_name": self.ui_window.lineEdit_lname.text().strip(),
            "first_name": self.ui_window.lineEdit_fname.text().strip(),
            "patronymic": self.ui_window.lineEdit_patronymic.text().strip(),
            "place_of_birth": self.ui_window.lineEdit_placeOfBirth.text().strip(),
            "place_of_death": self.ui_window.lineEdit_placeOfDeath.text().strip(),
            "year_of_birth": self.ui_window.lineEdit_yearOfBirth.text().strip(),
            "year_of_death": self.ui_window.lineEdit_yearOfDeath.text().strip(),
            "add_info": self.ui_window.plainTextEdit_addinfo.toPlainText().strip()
            or " ",
            "family_name": self.ui_window.lineEdit_clanName.text().strip(),
        }

        if self.is_input_valid(family_member):
            self.worksheet.title = family_member["family_name"]
            del family_member["family_name"]
            for column, value in enumerate(family_member.values()):
                self.worksheet.cell(row=1, column=column + 5, value=value)

            # TODO: use hash instead. Don't change the initial value!!!
            self.worksheet.cell(  # ID of a member.
                row=1,
                column=4,
                value=family_member["last_name"][0]
                + family_member["first_name"][0]
                + family_member["year_of_birth"],
            )

            self.set_my_card_button_label()
            self.close()


class AddRemoveClan(WindowConstructor):
    def __init__(self) -> None:
        super().__init__(Ui_AddRemoveClan)

    def openEvent(self) -> None:
        super().openEvent()
        self.fill_clan_names()

    def fill_clan_names(self) -> None:
        self.ui_window.lineEdit_addClan.clear()
        self.ui_window.comboBox_choiceRemoveClan.clear()
        self.ui_window.comboBox_choiceRemoveClan.insertItem(0, "")
        self.ui_window.comboBox_choiceRemoveClan.insertItems(
            1, self.workbook.sheetnames
        )

    def save(self) -> None:
        clan_name = self.ui_window.lineEdit_addClan.text()
        clan_to_remove = self.ui_window.comboBox_choiceRemoveClan.currentText()

        if clan_name:
            if search(r"[:\/\*\?[\]<>|]", clan_name):
                msbox.showerror(
                    "Увага!",
                    "Заборонено вводити такі символи: / \ * ? [ ] < > : |",
                )
                return
            else:
                self.workbook.create_sheet(clan_name)
        if clan_to_remove:
            if len(self.workbook.sheetnames) == 1:
                msbox.showerror("Увага!", "Неможливо видалити єдиний рід!")
                return
            else:
                del self.workbook[clan_to_remove]
                msbox.showinfo(message=f'Рід "{clan_to_remove}" видалено!')
        self.close()


class AddEdit(WindowConstructor):
    def __init__(self) -> None:
        super().__init__(Ui_AddEdit)

    def openEvent(self) -> None:
        super().openEvent()
        self.ui_window.comboBox_choiceClan.currentIndexChanged.connect(
            self.fill_clans_and_members
        )
        self.ui_window.comboBox_choiceClan.addItems(self.workbook.sheetnames)
        self.fill_clans_and_members()

    def closeEvent(self, *args: Any) -> None:
        self.ui_window.comboBox_choiceClan.disconnect()
        self.ui_window.comboBox_choiceClan.clear()
        return super().closeEvent(*args)

    def fill_window(self) -> None:
        row_index = self.ui_window.comboBox_addEdit.currentIndex()
        if row_index == 0:
            self.ui_window.lineEdit_lname.clear()
            self.ui_window.lineEdit_fname.clear()
            self.ui_window.lineEdit_patronymic.clear()
            self.ui_window.lineEdit_placeOfBirth.clear()
            self.ui_window.lineEdit_placeOfDeath.clear()
            self.ui_window.lineEdit_yearOfBirth.clear()
            self.ui_window.lineEdit_yearOfDeath.clear()
            self.ui_window.plainTextEdit_addinfo.clear()
            self.set_icon(join_path("Icons", "Add_image.png"))
        else:
            clan_index = self.ui_window.comboBox_choiceClan.currentIndex()
            sheet = self.workbook[self.workbook.sheetnames[clan_index]]
            row = sheet[row_index]
            if row[4].value == "Чоловіча":
                self.ui_window.comboBox_sex.setItemText(0, "Чоловіча")
            else:
                self.ui_window.comboBox_sex.setItemText(0, "Жіноча")
                self.ui_window.comboBox_sex.setItemText(1, "Чоловіча")

            self.ui_window.lineEdit_lname.setText(row[5].value)
            self.ui_window.lineEdit_fname.setText(row[6].value)
            self.ui_window.lineEdit_patronymic.setText(row[7].value)
            self.ui_window.lineEdit_placeOfBirth.setText(row[8].value)
            self.ui_window.lineEdit_placeOfDeath.setText(row[9].value)
            self.ui_window.lineEdit_yearOfBirth.setText(row[10].value)
            self.ui_window.lineEdit_yearOfDeath.setText(row[11].value)
            self.ui_window.plainTextEdit_addinfo.setPlainText(row[12].value)

            # Output the thumbnail to the image_Button if the cell is not empty
            self.set_icon(row[0].value or join_path("Icons", "Add_image.png"))

    def fill_clans_and_members(self) -> None:
        clan_name = self.ui_window.comboBox_choiceClan.currentText()
        worksheet = self.workbook[clan_name]
        count = self.ui_window.comboBox_addEdit.count()

        if count > 1:
            self.ui_window.comboBox_addEdit.setCurrentIndex(0)
            for _ in range(1, count):
                self.ui_window.comboBox_addEdit.removeItem(1)
            count = 1
        if count == 1:
            if worksheet["F1"].value:
                for row_number in range(1, worksheet.max_row + 1):
                    self.ui_window.comboBox_addEdit.insertItem(
                        row_number,
                        f"{worksheet[row_number][5].value} "
                        f"{worksheet[row_number][6].value}, "
                        f"{worksheet[row_number][10].value}",
                    )

    def set_avatar(self) -> None:
        image_path = self.fetch_image_path()
        if image_path:
            clan_index = self.ui_window.comboBox_choiceClan.currentIndex()
            worksheet = self.workbook[self.workbook.sheetnames[clan_index]]
            row_index = self.ui_window.comboBox_addEdit.currentIndex()

            if row_index == 0:  # If "Add" is selected.
                if not worksheet[worksheet.max_row][5].value:
                    row_index = worksheet.max_row
                else:
                    row_index = worksheet.max_row + 1
            worksheet.cell(row=row_index, column=1, value=image_path)
            self.set_icon(image_path)

    def save(self) -> None:
        family_member = {
            "sex": self.ui_window.comboBox_sex.currentText().strip(),
            "last_name": self.ui_window.lineEdit_lname.text().strip(),
            "first_name": self.ui_window.lineEdit_fname.text().strip(),
            "patronymic": self.ui_window.lineEdit_patronymic.text().strip(),
            "place_of_birth": self.ui_window.lineEdit_placeOfBirth.text().strip(),
            "place_of_death": self.ui_window.lineEdit_placeOfDeath.text().strip(),
            "year_of_birth": self.ui_window.lineEdit_yearOfBirth.text().strip(),
            "year_of_death": self.ui_window.lineEdit_yearOfDeath.text().strip(),
            "add_info": self.ui_window.plainTextEdit_addinfo.toPlainText().strip()
            or " ",
            "family_name": " ",
        }
        clan_index = self.ui_window.comboBox_choiceClan.currentIndex()
        worksheet = self.workbook[self.workbook.sheetnames[clan_index]]
        row_index = self.ui_window.comboBox_addEdit.currentIndex()

        if self.is_input_valid(family_member):
            if row_index == 0:  # If "Add" is selected.
                if not worksheet[worksheet.max_row][5].value:
                    row_index = worksheet.max_row
                else:
                    row_index = worksheet.max_row + 1

            del family_member["family_name"]
            for column, value in enumerate(family_member.values()):
                worksheet.cell(row=row_index, column=column + 5, value=value)

            worksheet.cell(  # ID of a member.
                row=row_index,
                column=4,
                value=f"{family_member['last_name'][0]}"
                + f"{family_member['first_name'][0]}"
                + f"{family_member['year_of_birth']}",
            )
            self.close()


def family_ties_def():
    FamilyTies = QtWidgets.QDialog()
    ui = Ui_FamilyTies()
    ui.setupUi(FamilyTies)
    FamilyTies.show()

    try:
        wb = load_workbook(WORKBOOK_NAME)
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
                                ws[n][4].value == "Чоловіча"
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

                            if ws[n][4].value == "Жіноча":
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
                            msbox.showerror(
                                "Увага!",
                                'В таблиці "Брати/Сестри" і "Діти" \
                                \nзнайдено однакові елементи!',
                            )
                            return

            if choicePerson_ind == 0:
                Tk().withdraw()
                msbox.showwarning(
                    "Увага!",
                    "Не вибрано, для кого встановити \nсімейні рв'язки!",
                )
            elif (choiceFather_text != "" and choiceMother_text == "") or (
                choiceFather_text == "" and choiceMother_text != ""
            ):
                Tk().withdraw()
                msbox.showerror("Увага!", "Не додано одного з батьків!")
            elif (
                choiceFather_text == choiceMother_text
                and choiceFather_ind != 0
            ):
                Tk().withdraw()
                msbox.showerror("Увага!", "Вибрано однакових батьків!")
            elif (
                choiceFather_ind != 0
                and ws[choiceFather_ind][10].value
                > ws[choicePerson_ind][10].value
            ):
                Tk().withdraw()
                msbox.showerror(
                    "Увага!", 'В поле "Батько" встановлено некоректну особу!'
                )
            elif (
                choiceMother_ind != 0
                and ws[choiceMother_ind][10].value
                > ws[choicePerson_ind][10].value
            ):
                Tk().withdraw()
                msbox.showerror(
                    "Увага!", 'В поле "Мати" встановлено некоректну особу!'
                )
            elif (
                choiceFather_ind != 0
                and choiceMother_ind != 0
                and ws[choiceFather_ind][1].value
                != ws[choiceMother_ind][1].value
            ):
                Tk().withdraw()
                msbox.showwarning("Увага!", "Батько або Мати вже в шлюбі!")
            elif choicePartner_text == choicePerson_text:
                Tk().withdraw()
                msbox.showerror(
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
                msbox.showwarning(
                    "Увага!",
                    "Не можна додавати братів чи сестер, \nпоки не вибрано батьків!",
                )
            elif (
                varFam_t_tab_Chd != []
                and choicePartner_ind == 0
                and choicePartner_text == ""
            ):
                Tk().withdraw()
                msbox.showwarning(
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
                                msbox.showerror(
                                    "Увага!",
                                    f"{ws[chd_row_ind][5].value} {ws[chd_row_ind][6].value} \
                                                \nне може бути Вашою дитиною!",
                                )
                            elif (
                                ws[chd_row_ind][2].value != None
                                and ws[chd_row_ind][2].value != marriage
                            ):
                                Tk().withdraw()
                                msbox.showerror(
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
                                msbox.showerror(
                                    "Увага!",
                                    f"{ws[BS_row_ind][5].value} {ws[BS_row_ind][6].value} \
                                \nне може бути Вашим братом чи сестрою!",
                                )
                            elif (
                                ws[BS_row_ind][2].value != None
                                and ws[BS_row_ind][2].value != marriage
                            ):
                                Tk().withdraw()
                                msbox.showerror(
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
                                msbox.showerror(
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
                        msbox.showerror(
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

                wb.save(WORKBOOK_NAME)
                FamilyTies.close()
                main_window.show()

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
        wb = load_workbook(WORKBOOK_NAME)
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
            main_window.show()

        ui.pushButton_done.clicked.connect(returnToMainWindow)

    finally:
        wb.close()


def resize_image(file_path) -> tuple[int, int]:
    image = Image.open(file_path)
    width, height = image.size
    max_width = max_height = 175

    if width > height:
        max_height = (max_width * height) // width
    elif width < height:
        max_width = (max_height * width) // height

    return max_width, max_height


def set_my_card_button_label() -> None:
    wb = load_workbook(WORKBOOK_NAME)
    ws = wb[wb.sheetnames[0]]

    ui_main_window.pushButton_1.setText(
        f'Рід: {ws.title}" f"\n{ws["G1"].value} {ws["F1"].value}'
    )

    if ws["A1"].value:
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(ws["A1"].value), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )

        ui_main_window.pushButton_1.setIcon(icon1)

    wb.close()


my_card = MyCard()
add_remove_clan = AddRemoveClan()
add_edit = AddEdit()

# Condition of pressing buttons.
my_card.ui_window.image_Button.clicked.connect(my_card.set_avatar)
my_card.ui_window.pushButton_done.clicked.connect(my_card.save)
add_remove_clan.ui_window.pushButton_done.clicked.connect(add_remove_clan.save)

add_edit.ui_window.comboBox_addEdit.currentIndexChanged.connect(
    add_edit.fill_window
)
add_edit.ui_window.image_Button.clicked.connect(add_edit.set_avatar)
add_edit.ui_window.pushButton_done.clicked.connect(add_edit.save)

ui_main_window.pushButton_1.clicked.connect(my_card.openEvent)
ui_main_window.pushButton_2.clicked.connect(add_remove_clan.openEvent)
ui_main_window.pushButton_3.clicked.connect(add_edit.openEvent)
ui_main_window.pushButton_4.clicked.connect(family_ties_def)
ui_main_window.pushButton_5.clicked.connect(review_def)

try:
    wb = load_workbook(WORKBOOK_NAME)
    set_my_card_button_label()
except FileNotFoundError:
    wb = Workbook()
    ws = wb.active
    ws.insert_rows(0)
    wb.save(WORKBOOK_NAME)
    my_card.openEvent()
finally:
    wb.close()

app.exec()
