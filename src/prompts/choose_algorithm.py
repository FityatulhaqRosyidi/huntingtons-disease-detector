from constants import colors

def choose_algorithm_ID() -> int:
    while True:
        print("pilih metode analisis:")
        print("1. Algoritma KMP")
        print("2. Algoritma Boyer-Moore")
        print("3. Kembali")

        choice = input(">> ")
        if choice == "1":
            print("Anda telah memilih Algoritma KMP.")
            return 1
        elif choice == "2":
            print("Anda telah memilih Algoritma Boyer-Moore.")
            return 2
        elif choice == "3":
            print("Kembali ke menu utama.")
            return 3
        else:
            print(colors.RED + "Pilihan tidak valid." + colors.RESET)