import os
from tools.wp_brute import WordPressBruteForcer
from tools.finder import ShellFinder
from tools.removeduplicat import process_files_in_config_folder  # Impor fungsi untuk menghapus duplikat
from tools.finder_v2 import scan_website  # Impor fungsi untuk Shell Finder V2
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
        Text("\n[3] ", style="cyan") + Text("Shell Finder V2", style=menu_style),  # Menu baru
        Text("\n[77] ", style="cyan") + Text("Remove Duplicates from Files", style=menu_style),  # Pindah ke 77
        Text("\n[88] ", style="cyan") + Text("Install Dependencies", style=menu_style),  # Menu baru
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

def run_shell_finder_v2():
    """
    Menjalankan Shell Finder V2.
    """
    console.print("[bold green]Memulai Shell Finder V2...[/]")
    try:
        # Minta pengguna memasukkan file target
        target_file = console.input("[bold yellow]Masukkan nama file target (contoh: targets.txt): [/]").strip()
        if not os.path.exists(target_file):
            console.print(f"[bold red]File '{target_file}' tidak ditemukan.[/]")
            return

        # Jalankan Shell Finder V2
        with open(target_file, 'r') as file:
            targets = [line.strip() for line in file.readlines()]

        from multiprocessing.dummy import Pool
        pool = Pool(150)  # Gunakan 150 thread
        pool.map(scan_website, targets)
        pool.close()
        pool.join()

        console.print("[bold green]Shell Finder V2 selesai![/]")
    except Exception as e:
        console.print(f"[bold red]Terjadi kesalahan: {e}[/]")

def install_dependencies():
    """
    Menginstal semua dependensi Python yang diperlukan.
    """
    console.print("[bold green]Menginstal dependensi...[/]")
    dependencies = [
        "requests",
        "colorama",
        "rich",
        "psutil",
        "urllib3",
        "python-dotenv"
    ]
    try:
        for package in dependencies:
            console.print(f"[bold cyan]Menginstal {package}...[/]")
            os.system(f"pip install {package}")
        console.print("[bold green]Semua dependensi berhasil diinstal![/]")
    except Exception as e:
        console.print(f"[bold red]Gagal menginstal dependensi: {e}[/]")

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
        elif choice == '3':  # Opsi baru untuk Shell Finder V2
            run_shell_finder_v2()
            console.input("\n[bold][Press Enter to continue...][/]")
        elif choice == '77':  # Opsi untuk Remove Duplicates from Files
            config_folder = "config"
            if not os.path.exists(config_folder) or not os.listdir(config_folder):
                console.print("[bold red]Folder 'config' kosong atau tidak ditemukan.[/]")
                console.input("\n[bold][Press Enter to continue...][/]")
                continue
            
            console.print("[bold green]Memproses file di folder 'config' untuk menghapus duplikat...[/]")
            process_files_in_config_folder(config_folder)
            console.print("[bold green]Proses selesai![/]")
            console.input("\n[bold][Press Enter to continue...][/]")
        elif choice == '88':  # Opsi untuk Install Dependencies
            install_dependencies()
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