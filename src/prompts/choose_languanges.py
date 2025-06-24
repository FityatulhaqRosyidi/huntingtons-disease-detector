from constants import colors

def choose_languages() -> str:
    while True:
        print("Choose your language (1/2):")
        print("1. English ")
        print("2. Bahasa Indonesia")
        print("3. Exit")
        language = int(input(">> "))
        if language == 1:
            print("You have chosen English.")
            return "EN"
        elif language == 2:
            print("Anda telah memilih Bahasa Indonesia.")
            return "ID"
        elif language == 3:
            print("Exiting...")
            return "EX"
        else:
            print(colors.RED + "Invalid choice, please try again!" + colors.RESET)
