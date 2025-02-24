import os
from tools.wp_brute import WordPressBruteForcer
from tools.finder import ShellFinder
from tools.removeduplicat import process_files_in_config_folder  # Impor fungsi dari removeduplicat.py
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

load_dotenv()
console = Console()

def show_menu():
    # Style definitions
    title_style = Style(color="bright_red", bold=True)
    menu_style = Style(color="bright_white", bold=True)
    
    # ASCII Art
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
    menu_text = Text.assemble(
        Text("\n[1] ", style="cyan") + Text("WordPress Bruteforce", style=menu_style),
        Text("\n[2] ", style="cyan") + Text("Shell Finder", style=menu_style),
        Text("\n[3] ", style="cyan") + Text("Remove Duplicates from Files", style=menu_style),  # Menu baru
        Text("\n[99] ", style="cyan") + Text("Show Configuration", style=menu_style),
        Text("\n[00] ", style="cyan") + Text("Exit Program\n", style=menu_style),
        justify="center"
    )
    # Panels
    dexion_panel = Panel(
        dexion_art,
        title="Plankton Dev",
        subtitle="Web Security Suite v2.0",
        style="bright_green",
        padding=(1, 3)
    )
    menu_panel = Panel(
        Text.assemble(
            Text("DEXION TOOLKIT", style=title_style),
            Text("\nAdvanced Web Penetration Testing Framework\n", style="bright_cyan"),
            menu_text
        ),
        title="[bright_blue]MAIN MENU[/]",
        subtitle="[bright_black]secured by plankton.dev[/]",
        padding=(1, 5),
        width=80
    )
    console.print(dexion_panel)
    console.print(menu_panel)

def main():
    # Initialize tools
    os.makedirs('config', exist_ok=True)
    os.makedirs('result', exist_ok=True)
    
    brute = WordPressBruteForcer()
    finder = ShellFinder()
    
    while True:
        show_menu()
        choice = console.input("\n[bold yellow]>> [/]").strip()
        
        if choice == '1':
            brute.load_resources()
            brute.start_attack()
        elif choice == '2':
            finder.load_resources()
            finder.start_scan()
            console.input("\n[bold][Press Enter to continue...][/]")
        elif choice == '3':  # Opsi baru untuk menghapus duplikat
            config_folder = "config"
            if not os.path.exists(config_folder) or not os.listdir(config_folder):
                console.print("[bold red]Folder 'config' kosong atau tidak ditemukan.[/]")
                console.input("\n[bold][Press Enter to continue...][/]")
                continue
    
            console.print("[bold green]Memproses file di folder 'config' untuk menghapus duplikat...[/]")
            process_files_in_config_folder(config_folder)
            console.print("[bold green]Proses selesai![/]")
            console.input("\n[bold][Press Enter to continue...][/]")
        elif choice == '99':
            console.print("\n[bold underline]CURRENT CONFIGURATION[/]")
            console.print("[bold cyan]WP Bruteforce:[/]")
            console.print(f"  URL File: {os.path.join('config', os.path.basename(brute.config['url_file']))}")
            console.print(f"  Wordlist: {os.path.join('config', os.path.basename(brute.config['wordlist_file']))}")
            console.print(f"  Threads: {brute.config['threads']}")
            
            console.print("\n[bold cyan]Shell Finder:[/]")
            console.print(f"  Domain List: {os.getenv('URL_FILE')}")
            console.print(f"  Payload List: {os.getenv('PWD_FILE')}")
            console.print(f"  Path List: {os.getenv('PATH_FILE')}")
            console.print(f"  Output File: {os.path.join('result', 'shell.txt')}")
            
            console.input("\n[bold][Press Enter to continue...][/]")
        elif choice == '00':
            console.print("[bold red]Exiting...[/]")
            break
        else:
            console.print("[bold red]Invalid option![/]")
            console.input("\n[bold][Press Enter to continue...][/]")

if __name__ == "__main__":
    main()