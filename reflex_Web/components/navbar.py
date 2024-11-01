import reflex as rx
from reflex_Web.styles.styles import Size as Size
import reflex_Web.styles.colors as color
from reflex_Web.styles.colors import Color as Color
from reflex_Web.styles.colors import TextColor as TextColor
import reflex_Web.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "fjmr", 
                color=Color.PRIMARY.value, 
                _as="span"),
            rx.text(
                "dev", 
                color=Color.SECONDARY.value, 
                _as="span"),
            # direction="row",
            # font_family="Comfortaa"
            style= styles.styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
