import reflex as rx
import datetime
import reflex_Web.styles.styles as styles
from reflex_Web.components.link_icon import link_icon
from reflex_Web.components.info_text import info_text
from reflex_Web.styles.styles import Size as Size
from reflex_Web.styles.colors import TextColor as TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # name="Francisco Javier", size= "xl" <- Estos parametros no funcionan.
            rx.avatar(fallback="FJMR", size="xl",
                      radius="full"),
            rx.vstack(
                rx.heading(
                    "Francisco Javier Menayo Ramos",
                    size="4",
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@fjmrdev",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                ),

                align_items="start",
            ), spacing=Size.DEFAULT.value
        ),
        rx.flex(
            rx.spacer(),
            info_text(f"{experience()}", " años de experiencia"),
            rx.spacer(),
            info_text("+10", " aplicaciones creadas"),
            rx.spacer(),
            info_text("+1", " seguidores"),
            rx.spacer(),
            width=styles.MAX_WIDTH,

        ),
        rx.text(
            f""" Soy Técnico Superior en Instalaciones Electrotécnicas y Técnico Especialista en Máquinas Eléctricas.
                    Tengo amplia experiencia en el sector farmaceutico, por mi trayectoria laboral.
                    Entre mis principales Hobbies está el desarrollo de páginas Web, y la maquetación de PCB'S 
                    """,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start",
    )


def experience() -> int:
    return datetime.date.today().year - 2022
