import reflex as rx
from reflex_Web.styles.styles import Size as Size
from reflex_Web.styles.colors import Color as Color

from reflex_Web.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        _as="span",
        color=TextColor.BODY.value
    )
