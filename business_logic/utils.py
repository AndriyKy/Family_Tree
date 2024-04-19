from tkinter import filedialog as fd


def fetch_image_path() -> str | None:
    return (
        fd.askopenfilename(
            filetypes=(
                ("JPEG image", ["*.jpeg", "*.jpg", "*.JPG"]),
                ("PNG image", "*.png"),
            )
        )
        or None  # `askopenfilename` returns `()` if nothing is selected.
    )


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
