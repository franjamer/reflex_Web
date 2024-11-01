import reflex as rx
import reflex_Web.styles.styles as styles
import reflex_Web.styles.colors as color
from reflex_Web.styles.colors import Color as Color
from reflex_Web.styles.colors import TextColor as TextColor

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="twitter", color=TextColor.HEADER.value
        ),
        href=url,
        is_external=True

    )