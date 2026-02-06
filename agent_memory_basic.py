from tools import kalkulator, kamus_lookup, baca_file
import json

memory_chat = []

def simpan_chat(role, content):
    memory_chat.append({"role": role, "content": content})

def tampilkan_ringkas_chat(n=5):
    return memory_chat[-n:]

def save_memory(path="memory_chat.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory_chat, f, indent=2)

def load_memory(path="memory_chat.json"):
    global memory_chat
    try:
        with open(path, "r", encoding="utf-8") as f:
            memory_chat = json.load(f)
    except FileNotFoundError:
        memory_chat = []

load_memory()

def agent_jawab(user_input: str) -> str:
    teks = user_input.lower().strip()

    if "hitung" in teks:
        expr = teks.replace("hitung", "").strip()
        return f"Hasil perhitungan: {kalkulator(expr)}"

    if teks.startswith("arti "):
        kata = teks.replace("arti", "").strip()
        return f"Arti '{kata}': {kamus_lookup(kata)}"

    if teks.startswith("baca file "):
        path = teks.replace("baca file", "").strip()
        return f"Isi file '{path}':\n{baca_file(path)}"

    if teks == "ringkas chat":
        return str(tampilkan_ringkas_chat())

    return "Saya belum punya tool untuk itu."

while True:
    q = input("Kamu: ")
    if q.lower() in ["exit", "quit"]:
        save_memory()
        break
    simpan_chat("user", q)
    ans = agent_jawab(q)
    simpan_chat("agent", ans)
    print("Agent:", ans)
