from tools import baca_file

def plan(user_input: str):
    teks = user_input.lower().strip()
    langkah = []

    if teks.startswith("buat ringkasan file "):
        path = teks.replace("buat ringkasan file", "").strip()
        langkah.append(("baca_file", path))
        langkah.append(("ringkas_teks", None))
        return langkah

    if teks.startswith("analisis nilai file "):
        path = teks.replace("analisis nilai file", "").strip()
        langkah.append(("baca_file", path))
        langkah.append(("hitung_rata2", None))
        return langkah

    return [("jawab_langsung", teks)]

def act(step, context):
    nama, arg = step

    if nama == "baca_file":
        return baca_file(arg)

    if nama == "ringkas_teks":
        teks = context.get("last_output", "")
        kalimat = teks.split(".")
        return ".".join(kalimat[:2]).strip() + "."

    if nama == "hitung_rata2":
        teks = context.get("last_output", "")
        angka = []
        for line in teks.splitlines():
            try:
                angka.append(float(line.strip()))
            except:
                pass
        return sum(angka) / len(angka) if angka else "Tidak ada angka."

    return "Saya belum paham tugas itu."

def run_agent(user_input):
    langkah = plan(user_input)
    context = {}

    for step in langkah:
        out = act(step, context)
        context["last_output"] = out
    return context.get("last_output", "")

while True:
    q = input("Kamu: ")
    if q.lower() in ["exit", "quit"]:
        break
    print("Agent:", run_agent(q))
