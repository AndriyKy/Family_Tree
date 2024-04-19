from re import search
from tkinter import filedialog as fd
from tkinter import messagebox as msbox
from typing import Any

from openpyxl import load_workbook
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

from pyui import (
    UIAddEdit,
    UIAddRemoveClan,
    UIFamilyTies,
    UIMainWindow,
    UIMyCard,
    UIReview,
)

WORKBOOK_NAME = "Family_lists.xlsx"


class WindowConstructor(QtWidgets.QDialog):
    """
    Access spreadsheet column at index 0, record at index 1.

    Columns explained:
    * A/0/1 - Image path
    * B/1/2 - * Person's ID
    * C/2/3 - Partner's ID
    * D/3/4 - Father's ID
    * E/4/5 - Mather's ID
    * F/5/6 - * Sex
    * G/6/7 - * Last name
    * H/7/8 - * First name
    * I/8/9 - Patronymic
    * J/9/10 - * Year of birth
    * K/10/11 - Year of death
    * L/11/12 - Place of birth
    * M/12/13 - Place of death
    * N/13/14 - Additional info

    \* - required field
    """

    def __init__(
        self,
        window: type[
            UIAddEdit
            | UIAddRemoveClan
            | UIFamilyTies
            | UIMainWindow
            | UIMyCard
            | UIReview
        ],
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ui_window = window()
        self.ui_window.setupUi(self)
        QtWidgets.QShortcut(
            QtGui.QKeySequence("Escape"), self, activated=self.on_Escape
        )

    def openEvent(self) -> None:
        self.workbook = load_workbook(WORKBOOK_NAME)
        self.show()

    def closeEvent(self, *args: Any) -> None:
        self.workbook.save(WORKBOOK_NAME)
        self.workbook.close()
        super().closeEvent(*args)

    @QtCore.pyqtSlot()
    def on_Escape(self) -> None:
        self.close()

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
                "Помилка!",
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
        width, height = self.resize_image(image_path)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.ui_window.image_Button.setIcon(icon)
        self.ui_window.image_Button.setIconSize(QtCore.QSize(width, height))
