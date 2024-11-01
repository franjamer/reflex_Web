import reflex as rx
from enum import Enum
import reflex_Web.styles.colors as colors
from .colors import Color as Color
from .colors import TextColor as TextColor

# Constants
MAX_WIDTH = "550px"
DEFAULT_WIDTH = "350px"
MAX_HEIGHT = "60px"
DEFAULT_HEIGHT = "40px"
BIG_HEIGHT = "50px"

BUTTON_BODY_STYLE = '2'
BUTTON_TITLE_STYLE = '3'
TITLE_STYLE = '7'


# Size


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"


# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "margin": Size.ZERO.value,
    "padding": Size.ZERO.value,
    "font_family": "Comfortaa-Medium",
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "bg": colors.Color.CONTENT.value


    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "opacity": 0.5,
            "color": colors.TextColor.BODY.value
        },
    }





}

# *** DEFINICION DE ESTILOS POR COMPONENTES. ***
# Para aplicar el stilo del componente  hay que incluirlo en la propiedad style del componente
buttom_style = dict(
    width="100%",
    height=BIG_HEIGHT,
    display="block",
    color=TextColor.HEADER.value,
    border_radius=Size.DEFAULT.value,
    background_color=Color.CONTENT.value,  # Color del botón completo
    _hover={
        "opacity": 0.5,
            "background_color": "violet",
            "color": TextColor.BODY.value
    },
)


title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    padding_left=Size.SMALL.value,

)

buttom_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    size=BUTTON_TITLE_STYLE,
    # margin_y= Size.ZERO.value,
    # padding_y= Size.ZERO.value,
    trim="both",
)

buttom_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    size=BUTTON_BODY_STYLE,
    trim="both",
)
link_style = dict(
    width="100%",
    border_radius=Size.DEFAULT.value,
)
vstack_style = dict(
    trim="none",
    # spacing = "0",
    align_items="start",
    margin=Size.ZERO.value,
)
hstack_style = dict(
    align="center",
    justify="center",
)
navbar_title_style = dict (
    font_family= "Comfortaa-Medium",
    font_size = Size.LARGE.value
)