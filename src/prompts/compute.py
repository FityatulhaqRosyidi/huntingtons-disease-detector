from algorithms.kmp import KMP
from algorithms.bm import BM
from constants.dna_patterns import SYMPTOM_PATTERN, INTERMEDIATE_PATTERN
from time import time

def compute_ID(algorithm : int, text: str):
    start_time = time()
    if algorithm == 1:
        kmp = KMP(text)

        idx = kmp.search(SYMPTOM_PATTERN)
        if idx != -1:
            # print(f"DNA mengandung pola penyakit Huntington pada indeks {idx}.")
            return (time() - start_time, "symptom")

        idx = kmp.search(INTERMEDIATE_PATTERN)
        if idx != -1:
            # print(f"DNA mengandung pola berpotensi mewariskan gen penyakit Huntington pada indeks {idx}.")
            return (time() - start_time, "intermediate")

        # print("Tidak ditemukan pola penyakit Huntington pada DNA.")
        return (time() - start_time, "normal")

    elif algorithm == 2:
        bm = BM(text)

        idx = bm.search(SYMPTOM_PATTERN)
        if idx != -1:
            # print(f"DNA mengandung pola penyakit Huntington pada indeks {idx}.")
            return (time() - start_time, "symptom")

        idx = bm.search(INTERMEDIATE_PATTERN)
        if idx != -1:
            # print(f"DNA mengandung pola berpotensi mewariskan gen penyakit Huntington pada indeks {idx}.")
            return (time() - start_time, "intermediate")

        # print("Tidak ditemukan pola penyakit Huntington pada DNA.")
        return (time() - start_time, "normal")



