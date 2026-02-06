from tools import kalkulator, kamus_lookup, baca_file

def log_interaksi(user_input, agent_output):
    with open("log_agent.txt", "a", encoding="utf-8") as f:
        f.write(f"USER: {user_input}\nAGENT: {agent_output}\n---\n")

def agent_jawab(user_input: str) -> str:
    teks = user_input.lower()

    if "hitung" in teks:
        expr = teks.replace("hitung", "").strip()
        return f"Hasil perhitungan: {kalkulator(expr)}"

    if teks.startswith("arti "):
        kata = teks.replace("arti", "").strip()
        return f"Arti '{kata}': {kamus_lookup(kata)}"

    if teks.startswith("baca file "):
        path = teks.replace("baca file", "").strip()
        return f"Isi file '{path}':\n{baca_file(path)}"

    return "Saya belum punya tool untuk itu."

while True:
    q = input("Kamu: ")
    if q.lower() in ["exit", "quit"]:
        break
    ans = agent_jawab(q)
    log_interaksi(q, ans)
    print("Agent:", ans)
