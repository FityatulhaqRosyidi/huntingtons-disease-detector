from constants import colors

def coloring_string_at_index_to_index(text: str, start: int, end: int) -> str:
    return f"{text[:start]}{colors.YELLOW}{text[start:end]}{colors.RESET}{text[end:]}"