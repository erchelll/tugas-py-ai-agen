def kalkulator(expr: str):
    try:
        return eval(expr)
    except Exception as e:
        return f"Error kalkulator: {e}"

KAMUS = {
    "python": "Bahasa pemrograman populer untuk otomasi, data, dan AI.",
    "agent": "Program yang bisa merencanakan dan memakai tool untuk menyelesaikan tujuan.",
    "llm": "Model bahasa besar yang menghasilkan teks berdasarkan konteks."
}

def kamus_lookup(kata: str) -> str:
    kata = kata.lower().strip()
    return KAMUS.get(kata, "Kata tidak ditemukan di kamus.")

def baca_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return f"Error baca file: {e}"

def konversi_suhu(nilai: float, mode: str):
    if mode == "c2f":
        return (nilai * 9/5) + 32
    elif mode == "f2c":
        return (nilai - 32) * 5/9
    else:
        return "Mode tidak dikenal"
