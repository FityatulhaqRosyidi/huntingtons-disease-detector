import random

# Fungsi untuk menghasilkan urutan DNA
def generate_dna_sequence_huntington(file_name, sequence_length, huntington_repeats):
    # Basis DNA
    bases = ['A', 'T', 'C', 'G']
    huntington_marker = "CAG" * huntington_repeats  # Penanda penyakit Huntington
    
    # Panjang urutan DNA tanpa penanda
    remaining_length = sequence_length - len(huntington_marker)
    
    # Membuat urutan DNA acak
    random_sequence = "".join(random.choices(bases, k=remaining_length))
    
    # Menyisipkan penanda Huntington pada posisi acak
    insert_position = random.randint(0, len(random_sequence))
    final_sequence = random_sequence[:insert_position] + huntington_marker + random_sequence[insert_position:]
    
    # Menyimpan urutan ke file teks
    folder_path = "D:\Repository\huntingtons-disease-detector\data"
    with open(folder_path + file_name, "w") as file:
        file.write(final_sequence)
    print(f"DNA sequence with {huntington_repeats} CAG repeats saved to {file_name}")

# Fungsi untuk menghasilkan urutan DNA
def generate_dna_sequence_normal(file_name, sequence_length):
    # Basis DNA
    bases = ['A', 'T', 'C', 'G']
    # Membuat urutan DNA acak
    random_sequence = "".join(random.choices(bases, k=sequence_length))
    # Menyimpan urutan ke file teks
    folder_path = "D:\Repository\huntingtons-disease-detector\data"
    with open(folder_path + file_name, "w") as file:
        file.write(random_sequence)
    print(f"DNA sequence normal saved to {file_name}")

# Parameter
total_length = 2_000_000  # Panjang total urutan DNA
cag_repeats = 36  # Jumlah pengulangan CAG

# Panggil fungsi
for i in range(7):
    output_file = f"\DNA_sequence_{(2**i) * 10_000_000}_Abnormal.txt"
    generate_dna_sequence_huntington(output_file, total_length, 37)
