import reflex as rx
import datetime
from reflex_Web.styles.styles import Size as Size
import reflex_Web.styles.colors as color
from reflex_Web.styles.colors import Color as Color
from reflex_Web.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"@ 2023-{datetime.date.today().year} FJMRDEV by Francisco Javier Menayo Ramos V0.",
                href="https://mouredev.com",
                is_external=True,
                font_size=Size.MEDIUM.value,
                ),
        rx.text("BUILDING SOFTWARE WITH @LIKE FROM GALICIA TO THE WORLD.",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value,
                ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )
