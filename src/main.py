from algorithms.bm import BM
from algorithms.kmp import KMP
from prompts.choose_file_input import choose_file_input_ID
from prompts.choose_languanges import choose_languages
from prompts.choose_algorithm import choose_algorithm_ID
from prompts.compute import compute_ID




def main():
    language = choose_languages()
    if language == "ID":
        print("Selamat datang di detektor penyakit Huntington!")
        print("Program ini akan membantu Anda mendeteksi penyakit Huntington.")
        dna_sequence = choose_file_input_ID()
        algorithm_choice = choose_algorithm_ID()

        exec_time = compute_ID(algorithm_choice, dna_sequence)

        print(f"Waktu eksekusi: {exec_time} detik")

    elif language == "EX":
        return
    

if __name__ == "__main__":
    main()