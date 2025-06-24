import os

from prompts.compute import compute_ID
from filestream.input import get_txt_file_from_path

def list_files_in_folder(folder_path):
    """
    Mendapatkan semua nama file dalam folder tertentu.

    Args:
        folder_path (str): Path ke folder.

    Returns:
        list: Array berisi nama file.
    """
    try:
        # Hanya mengambil nama file (bukan folder)
        files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        return files
    except FileNotFoundError:
        print(f"Folder '{folder_path}' tidak ditemukan.")
        return []
    except PermissionError:
        print(f"Tidak memiliki izin untuk mengakses folder '{folder_path}'.")
        return []

# Contoh penggunaan
folder_path = "D:\Repository\huntingtons-disease-detector\data"

print("|  length |  KMP Time |  BM Time  |")
for i in range(7):
    print(f"| {(2**i) * 1_000_000} |", end=' ')
    file_name = f"DNA_sequence_{(2**i) * 10_000_000}_Normal.txt"
    dna_sequence = get_txt_file_from_path(os.path.join(folder_path, file_name))

    for j in range(2):
        time, res = compute_ID(j+1, dna_sequence)
        print(f" {time:.4f} s {res} |", end=' ')
    print("")