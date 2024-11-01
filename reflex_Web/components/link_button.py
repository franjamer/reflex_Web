import reflex as rx

import reflex_Web.styles.styles as styles
# from reflex_Web.styles.styles import BASE_STYLE, BUTTON_TITLE_STYLE, BUTTON_BODY_STYLE, Size, MAX_WIDTH, DEFAULT_WIDTH, DEFAULT_HEIGHT, MAX_HEIGHT, BIG_HEIGHT
import reflex_Web.styles.colors as colors
from reflex_Web.styles.colors import TextColor, Color
# from reflex_Web.styles.styles import link_style as link_style
# from reflex_Web.styles.styles import buttom_title_style as buttom_title_style,buttom_body_style as buttom_body_style, buttom_style as buttom_style
# from reflex_Web.styles.styles import vstack_style,hstack_style
# from reflex_Web.styles.styles import buttom_style
def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="youtube",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    
                ),
                rx.vstack(
                    # con la propiedad both en el componente rx.text, ajustamos el texto en altura, para que quede dentro de los limites del botón.
                    rx.text(
                        title,                     
                        style= styles.buttom_title_style,
                    ),
                    rx.text(
                        body,
                        style=styles.buttom_body_style
                    ),
                # aplicación del estilo del vstack
                style=styles.vstack_style
                ),
                # aplicación del estilo del hstack                
            style= styles.hstack_style
            ),
        # style=styles.buttom_style
        ),
    # style=styles.link_style,
    # parametros propios del componente link, que no se meten en estilos
    href=url,
    is_external=True,
    )
