import tkinter as tk
import time
import random
import threading

# Mängu muutujad
taimer = 20
töötab = True
tase = 1
õige_vastused = 0
õige = 0

# Taimeri funktsioon
def loendur():
    global taimer
    global töötab

    while taimer > 0 and töötab:
        taimer_silt.config(text="Aega: " + str(taimer) + "s  ||  Tase: " + str(tase))
        time.sleep(1)
        taimer -= 1

    # Kui aeg saab nulli, siis mäng lõpeb
    if taimer <= 0:
        töötab = False
        taimer_silt.config(text="Pomm plahvatas! Mäng läbi.")
        tagasiside_silt.config(text="Õigeid vastuseid kokku: " + str(õige_vastused))
        vasta_nupp.config(state="disabled")

        for nupp in numbri_nupud:
            nupp.config(state="disabled")


# Uue tehte tegemine
def loo_tehe():
    global a
    global b
    global õige
    global sümbol

    # Mida kõrgem tase, seda suuremad arvud
    maksimaalne = 10 * (2 ** (tase - 1))

    a = random.randint(1, maksimaalne)
    b = random.randint(1, maksimaalne)
    sümbol = random.choice(["+", "-", "*"])

    if sümbol == "+":
        õige = a + b
    elif sümbol == "-":
        õige = a - b
    else:
        õige = a * b

    küsimus_silt.config(text=str(a) + " " + sümbol + " " + str(b) + " = ?")


# Vastuse kontrollimine, kui vajutatakse VASTA nuppu
def kontrolli_vastust():
    global taimer
    global õige_vastused
    global tase

    # Proovi muuta ekraanil olev tekst arvuks
    try:
        vastus = int(ekraan_muutuja.get())
    except ValueError:
        tagasiside_silt.config(text="❗See ei olnud number! Aega ei lisatud.")
        return

    # Tühjenda ekraan
    ekraan_muutuja.set("")

    if vastus == õige:
        taimer += 5
        õige_vastused += 1
        tagasiside_silt.config(text="✔️ Õige vastus! +5 sekundit.")

        # Iga 5 õige vastuse järel tõuseb tase
        if õige_vastused % 5 == 0:
            tase += 1
            tagasiside_silt.config(text="Uus tase: " + str(tase) + "!")

    else:
        taimer = max(0, taimer - 2)
        tagasiside_silt.config(text="❌ Vale! Õige vastus oli " + str(õige) + ". -2 sekundit")

    # Tee uus teje pärast vastuse kontrollimist
    loo_tehe()


# Nupu vajutus lisab numbri ekraanile
def vajuta(väärtus):
    vana_tekst = ekraan_muutuja.get()
    ekraan_muutuja.set(vana_tekst + str(väärtus))


# Kustutab viimase numbri
def kustuta():
    vana_tekst = ekraan_muutuja.get()
    uus_tekst = vana_tekst[:-1]
    ekraan_muutuja.set(uus_tekst)


############
# Tkinter UI
############

# Aken
aken = tk.Tk()
aken.title("ARVUTAMISE MÄNG")
aken.geometry("300x500")
aken.resizable(False, False)

# Taimer tekst akna ülaosas
taimer_silt = tk.Label(aken, text="Aega: 20s  ||  Tase: 1", font=("Arial", 16), fg="red")
taimer_silt.pack()

# Küsimus
küsimus_silt = tk.Label(aken, text="", font=("Arial", 22))
küsimus_silt.pack()

# Ekraan, kus näeb sisestatud numbrit
ekraan_muutuja = tk.StringVar()
ekraan = tk.Label(aken, textvariable=ekraan_muutuja, font=("Arial", 28), width=10, bg="white")
ekraan.pack()

# Tagasiside tekst (õige või vale)
tagasiside_silt = tk.Label(aken, text="", font=("Arial", 12))
tagasiside_silt.pack()

# Raam, kus on kõik numbri nupud
nupu_raam = tk.Frame(aken)
nupu_raam.pack()

# Nimekiri kõikidest numbri nuppudest // vaja, et lülitada mängu lõpus vajutamise välja
numbri_nupud = []

# Numbrite paigutus kalkulaatori kujul
numbrid = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

for rida in range(len(numbrid)):
    for veerg in range(len(numbrid[rida])):
        number = numbrid[rida][veerg]

        nupp = tk.Button(
            nupu_raam,
            text=str(number),
            width=6,
            height=2,
            font=("Arial", 16),
            command=lambda n=number: vajuta(n)
        )

        nupp.grid(row=rida, column=veerg)
        numbri_nupud.append(nupp)

# Nupp 0
nupp0 = tk.Button(nupu_raam, text="0", width=6, height=2, font=("Arial", 16), command=lambda: vajuta(0))
nupp0.grid(row=3, column=1)
numbri_nupud.append(nupp0)

# Kustuta nupp
kustuta_nupp = tk.Button(nupu_raam, text="⌫", width=6, height=2, font=("Arial", 16), command=kustuta)
kustuta_nupp.grid(row=3, column=2)
numbri_nupud.append(kustuta_nupp)

# Vasta nupp
vasta_nupp = tk.Button(
    aken,
    text="VASTA",
    width=20,
    height=2,
    font=("Arial", 14),
    bg="green",
    fg="white",
    command=kontrolli_vastust
)
vasta_nupp.pack()

# Käivita mäng 
loo_tehe()

lõim = threading.Thread(target=loendur)
lõim.start()

aken.mainloop()
töötab = False