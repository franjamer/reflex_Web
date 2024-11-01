import reflex as rx
import reflex_Web.styles.colors as colors
from reflex_Web.components.navbar import navbar as navbar
from reflex_Web.components.footer import footer as footer
from reflex_Web.components.link_icon import link_icon
from reflex_Web.views.header.header import header
from reflex_Web.views.links.links import links
from reflex_Web.styles import styles
from reflex_Web.styles.styles import BASE_STYLE, MAX_WIDTH,BUTTON_TITLE_STYLE
from reflex_Web.styles.styles import Size as Size
from reflex_Web.styles.colors import TextColor as TextColor
from reflex_Web.styles.colors import Color as Color

import rxconfig as config


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                link_icon("https://x.com/mouredev"),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            ),
        ),
        rx.center(
            footer()
        ),
        # background_color= Color.CONTENT.value,
        # color= Color.SECONDARY.value
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
