import reflex as rx
from reflex_Web.components.link_button import link_button
from reflex_Web.styles import styles
from reflex_Web.styles.styles import Size, MAX_WIDTH
from reflex_Web.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "https://twitch.tv/mouredev"
        ),
        link_button(
            "YouTube",
            "Siempre disponibles",
            "https://youtube.com/@mouredev"
        ),
        link_button(
            "YouTube(canal secundario)",
            "Mi canal de directos",
            "https://youtube.com/@mouredevtv"
        ),
        link_button(
            "Discord",
            "El lugar de encuentro de la comunidad",
            "https://discord.gg/mouredev"
        ),
        # background_color="indigo",
        width=MAX_WIDTH,
        padding_y=Size.SMALL.value,
        # Este align centra el contenido de la vista de links(start,center,end)
        align="between",
        spacing=Size.MEDIUM.value,
        justify="center",
        # text_decoration="underline"
    )
