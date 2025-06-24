from filestream.input import get_txt_file_from_path

def choose_file_input_ID() -> str:
    while True:
        print("Silakan masukkan filepath data genetik Anda untuk analisis.")
        path = input(">> ")
        if not path.endswith(".txt"):
            print("File harus berformat .txt")
            continue

        dna_sequence = get_txt_file_from_path(path)
        if not dna_sequence:
            print("Gagal membaca file.")
            continue

        return dna_sequence


        


