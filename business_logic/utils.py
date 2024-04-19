import shutil
from os import remove
from os.path import join as join_path
from os.path import sep
from tkinter import filedialog as fd
from uuid import uuid4


def _copy_image_to_local_folder(
    image_path: str, local_folder: str = "avatars"
) -> str:
    """Copies an image from one folder to another and returns the image name."""
    image_name = image_path.split(sep)[-1]
    unique_image_name = f"{str(uuid4())}.{image_name.split('.')[-1]}"
    destination_path = join_path(local_folder, unique_image_name)
    shutil.copyfile(image_path, destination_path)
    return unique_image_name


def select_image() -> str | None:
    """Selects an image from the user's computer, copies it to a local folder,
    and returns its name.
    """
    image_path = fd.askopenfilename(
        filetypes=(
            ("JPEG image", ["*.jpeg", "*.jpg", "*.JPG"]),
            ("PNG image", "*.png"),
        )
    )
    if not image_path:
        return None
    return _copy_image_to_local_folder(image_path)


def remove_image_if_exists(image_name: str) -> None:
    if image_name:
        image_path = join_path("avatars", image_name)
        remove(image_path)


def fit_image_size(
    image_size: tuple[int, int], max_on_long_side: int = 175
) -> tuple[int, int]:
    width, height = image_size
    max_width = max_height = max_on_long_side

    if width > height:
        max_height = (max_width * height) // width
    elif width < height:
        max_width = (max_height * width) // height

    return max_width, max_height
