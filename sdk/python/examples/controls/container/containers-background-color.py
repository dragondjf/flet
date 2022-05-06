from typing import Text

import flet
from flet import Container, ElevatedButton, OutlinedButton, Page, Text, colors


def main(page: Page):
    page.title = "Containers with different background color"

    c1 = Container(
        content=Text("#CC0000"),
        bgcolor="#CC0000",
        padding=5,
    )

    c2 = Container(
        content=Text("colors.Yellow", opacity=0.5),
        bgcolor=colors.YELLOW,
        padding=5,
    )

    c3 = Container(
        content=OutlinedButton("Outlined Button in Container"),
        bgcolor=colors.YELLOW,
        padding=5,
    )
    page.add(c1, c2, c3)


flet.app(target=main)
