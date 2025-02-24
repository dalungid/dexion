from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

console = Console()

def show_menu():
    # Style definitions
    title_style = Style(color="bright_red", bold=True)
    subtitle_style = Style(color="cyan", italic=True)
    menu_style = Style(color="bright_white", bold=True)
    border_style = Style(color="bright_yellow")

    # ASCII Art with gradient
    dexion_art = Text.assemble(
        Text("\n██████╗ ███████╗██╗  ██╗██╗ ██████╗ ███╗   ██╗\n", style="red"),
        Text("██╔══██╗██╔════╝╚██╗██╔╝██║██╔═══██╗████╗  ██║\n", style="dark_orange"),
        Text("██║  ██║█████╗   ╚███╔╝ ██║██║   ██║██╔██╗ ██║\n", style="gold1"),
        Text("██║  ██║██╔══╝   ██╔██╗ ██║██║   ██║██║╚██╗██║\n", style="dark_red"),
        Text("██████╔╝███████╗██╔╝ ██╗██║╚██████╔╝██║ ╚████║\n", style="orange_red1"),
        Text("╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n", style="yellow"),
        justify="center"
    )

    # Menu items
    menu_items = Text.assemble(
        Text("\n1. ", style="cyan") + Text("WP Brute Force", style=menu_style),
        Text("\n2. ", style="cyan") + Text("Show Config", style=menu_style),
        Text("\n3. ", style="cyan") + Text("Exit\n", style=menu_style),
        justify="center"
    )

    # Plankton Dev Panel (Dexion Art with Title)
    dexion_panel = Panel(
        dexion_art,
        title="Plankton Dev",
        subtitle="Version 1.3",
        style="bright_green",
        border_style="bright_blue",
        padding=(1, 3)
    )

    # Main menu panel
    menu_panel = Panel(
        Text.assemble(
            Text("DEXION Tools", style=title_style),
            Text("\nPrivate Pentest Tools", style=subtitle_style),
            menu_items,
        ),
        title="[bright_cyan]MENU[/]",
        subtitle="[bright_black]secured by Plankton Dev[/]",
        style="bright_blue",
        padding=(1, 5),
        width=80
    )

    # Print both panels to the console
    console.print(dexion_panel)
    console.print(menu_panel)

if __name__ == "__main__":
    show_menu()
