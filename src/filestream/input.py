
def get_txt_file_from_path(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

