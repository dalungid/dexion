import os

def remove_duplicates(input_file):
    """
    Menghapus baris duplikat dari file teks tanpa mengubah file asli.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    unique_lines = []
    seen = set()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and stripped_line not in seen:
            unique_lines.append(line)
            seen.add(stripped_line)

    return unique_lines


def process_single_file(config_folder, filename):
    """
    Memproses satu file .txt dalam folder config.
    Menghapus duplikat, menyimpan hasil ke file baru dengan prefix 'c-'.
    """
    input_file_path = os.path.join(config_folder, filename)
    output_file_path = os.path.join(config_folder, f"c-{filename}")

    if not os.path.exists(input_file_path):
        print(f"[bold red]File '{filename}' tidak ditemukan di folder 'config'.[/]")
        return

    # Hapus duplikat dari file
    unique_lines = remove_duplicates(input_file_path)

    # Simpan hasil ke file baru
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(unique_lines)

    print(f"[bold green]File '{filename}' telah diproses. Hasil disimpan sebagai 'c-{filename}'.[/]")


def process_files_in_config_folder(config_folder):
    """
    Memproses file yang diminta oleh pengguna di folder config.
    """
    if not os.path.exists(config_folder):
        print(f"[bold red]Folder 'config' tidak ditemukan.[/]")
        return

    # Minta pengguna memasukkan nama file
    filename = input("Masukkan nama file yang ingin diproses (contoh: id.txt): ").strip()
    if not filename.endswith(".txt"):
        print("[bold red]Nama file harus memiliki ekstensi .txt.[/]")
        return

    process_single_file(config_folder, filename)