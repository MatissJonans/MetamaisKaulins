import tkinter as tk
from PIL import Image, ImageTk
import random

def SagatavoAttelu(p):
    # attēlu saraksts
    att = [
        "atteli/dice1.png",
        "atteli/dice2.png",
        "atteli/dice3.png",
        "atteli/dice4.png",
        "atteli/dice5.png",
        "atteli/dice6.png"
    ]

    # nejauši izvēlas attēlu
    attels = Image.open(att[p-1])

    # iegūst attēla izmērus
    p, h = attels.size
    platums = int(p * 0.5)
    augstums = int(h * 0.5)

    # samazina attēla izmēru
    attels = attels.resize((platums, augstums))

    # konvertē attēlu uz Tkinter formātu
    foto = ImageTk.PhotoImage(attels)

    return foto

#definē mainīgos lai tos vēlāk varētu izmantot
metiens = 1
P = 0
P2 = 0

#Mest funkcija un animācija
def MetKaulinu():
    metieni = 0
    def Animacija():
        nonlocal metieni
        global metiens, P, P2
        metieni += 1
        p1 = random.randint(1, 6) #Met 3 kauliņus.
        p2 = random.randint(1, 6)
        p3 = random.randint(1, 6)
        if metieni <= 10:
            jkaulins = SagatavoAttelu(p1)
            akaulins.config(image = jkaulins)
            akaulins.image = jkaulins
            kkaulins = SagatavoAttelu(p2)
            bkaulins.config(image = kkaulins)
            bkaulins.image = kkaulins
            lkaulins = SagatavoAttelu(p3)
            ckaulins.config(image = lkaulins)
            ckaulins.image = lkaulins 
            window.after(100, Animacija)
            if metieni == 10:
                if metiens == 1:#Ja ir 1. metiens parāda 1. spēlētāja punktu summu.
                    P = p1 + p2 + p3
                    punkti.config(text=f"1. spēlētāja punkti: {P}")
                    metiens += 1
                else:#ja ir 2. metiens parāda 2. spēlētāja punktu summu un nomaian "Mest" pogu ar "Rezultāti" pogu.
                    P2 = p1 + p2 + p3
                    punkti.config(text=f"2. spēlētāja punkti: {P2}") 
                    mest.pack_forget()
    Animacija()


#Rezultātu pogas funkcija
def RezultatiPog():
    punkti.pack_forget()
    kaulins_frame.pack_forget()
    rezultatiPog.pack_forget()
    rezultati.pack(fill="both", expand=True)
    punkti1.config(text=f"1. Spēlētājs ieguva {P} punktus") #Parāda abu spēlētāju punktus.
    punkti2.config(text=f"2. Spēlētājs ieguva {P2} punktus")
    if P > P2: #Nosaka uzvarētāju.
        rezultati.config(text="1. Spēlētājs uzvar!")
    elif P < P2:
        rezultati.config(text="2. Spēlētājs uzvar!")
    else:
        rezultati.config(text="Neizšķirts!")


#Izveido logu
window = tk.Tk()
window.title("Metamo kauliņu spēle")
window.geometry("600x300")

p = random.randint(1, 6)


#Spēles skats
kaulins_frame = tk.Frame(window)
kaulins_frame.pack(expand=True)

punkti = tk.Label(kaulins_frame, text=f"Spēlētājs ar lielāko punktu summu uzvar.")
punkti.pack(side=tk.TOP, padx=10, pady=10)

#Metamo kauliņu foto ielāde.
foto1 = SagatavoAttelu(p)
akaulins = tk.Label(kaulins_frame, image=foto1)
akaulins.pack(side="left", pady=10)

foto2 = SagatavoAttelu(p)
bkaulins = tk.Label(kaulins_frame, image=foto2)
bkaulins.pack(side="left", pady=10)

foto3 = SagatavoAttelu(p)
ckaulins = tk.Label(kaulins_frame, image=foto2)
ckaulins.pack(side="left", pady=10)

#"Mest" poga.
mest = tk.Button(window, text = "Mest", command = MetKaulinu)
mest.pack(pady=30)

#"Rezultāti" poga.
rezultatiPog = tk.Button(window, text = "Rezultāti", command = RezultatiPog)
rezultatiPog.pack(pady=30)


#Rezultātu skats
rezultati_frame = tk.Frame(window)
rezultati_frame.pack(expand=True)

punkti1 = tk.Label(rezultati_frame, text =f"")
punkti1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

punkti2 = tk.Label(rezultati_frame, text =f"")
punkti2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

rezultati = tk.Label(rezultati_frame, text = "", font =("Arial", 12, "bold"))
rezultati.pack(expand=True, pady = 20, )

window.mainloop()