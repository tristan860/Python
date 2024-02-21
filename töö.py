import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import os

class Teenus:
    def __init__(self, kirjeldus, hind):
        self.kirjeldus = kirjeldus
        self.hind = hind

class Arve:
    def __init__(self):
        self.teenused = []

    def lisateenus(self, teenus):
        self.teenused.append(teenus)

    def eemaldateenus(self, indeks):
        del self.teenused[indeks]

    def arve_summa(self):
        return sum(teenus.hind for teenus in self.teenused)

    def to_dict(self):
        return {'Teenuse kirjeldused': [teenus.kirjeldus for teenus in self.teenused],
                'Teenuste hinnad': [teenus.hind for teenus in self.teenused],
                'Kogusumma': self.arve_summa()}

class ArveteRakendus:
    def __init__(self, root):
        self.root = root
        self.root.title("Arvete Haldamine")

        self.teenused = self.laadi_andmed_andmefailist("teenused.csv")
        self.arved = self.laadi_arved_csv_failidest()

        tk.Label(root, text="Teenused:").pack()
        self.teenuste_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.teenuste_listbox.pack()

        self.kuva_teenused()

        lisamise_nupp = tk.Button(root, text="Lisa Teenus", command=self.lisa_teenus)
        lisamise_nupp.pack()

        muutmise_nupp = tk.Button(root, text="Muuda Teenust", command=self.muuda_teenust)
        muutmise_nupp.pack()

        kustutamise_nupp = tk.Button(root, text="Kustuta Teenus", command=self.kustuta_teenus)
        kustutamise_nupp.pack()

        koostamise_nupp = tk.Button(root, text="Koosta Arve", command=self.koosta_arve)
        koostamise_nupp.pack()

        vaatamise_nupp = tk.Button(root, text="Vaata Arveid", command=self.vaata_arveid)
        vaatamise_nupp.pack()

        self.arve_tekst = tk.Text(root, height=10, width=50)
        self.arve_tekst.pack()

    def kuva_teenused(self):
        self.teenuste_listbox.delete(0, tk.END)
        for teenus in self.teenused:
            self.teenuste_listbox.insert(tk.END, f"{teenus.kirjeldus} - {teenus.hind}€")

    def lisa_teenus(self):
        kirjeldus = simpledialog.askstring("Lisa Teenus", "Sisesta teenuse kirjeldus:")
        if kirjeldus:
            hind = simpledialog.askfloat("Lisa Teenus", "Sisesta teenuse hind:")
            if hind is not None:
                uus_teenus = Teenus(kirjeldus, hind)
                self.teenused.append(uus_teenus)
                self.kuva_teenused()
                self.salvesta_andmed_andmefaili(self.teenused, "teenused.csv")

    def muuda_teenust(self):
        valitud_indeks = self.teenuste_listbox.curselection()
        if not valitud_indeks:
            messagebox.showwarning("Hoiatus", "Palun vali teenus, mida muuta.")
            return

        valitud_indeks = valitud_indeks[0]
        muudetav_teenus = self.teenused[valitud_indeks]

        uus_kirjeldus = simpledialog.askstring("Muuda Teenust", "Sisesta uus kirjeldus:", initialvalue=muudetav_teenus.kirjeldus)
        if uus_kirjeldus:
            uus_hind = simpledialog.askfloat("Muuda Teenust", "Sisesta uus hind:", initialvalue=muudetav_teenus.hind)
            if uus_hind is not None:
                muudetav_teenus.kirjeldus = uus_kirjeldus
                muudetav_teenus.hind = uus_hind
                self.kuva_teenused()
                self.salvesta_andmed_andmefaili(self.teenused, "teenused.csv")

    def kustuta_teenus(self):
        valitud_indeksid = self.teenuste_listbox.curselection()
        if not valitud_indeksid:
            messagebox.showwarning("Hoiatus", "Palun vali vähemalt üks teenus kustutamiseks.")
            return

        valitud_indeksid = sorted(valitud_indeksid, reverse=True)
        for indeks in valitud_indeksid:
            del self.teenused[indeks]
        self.kuva_teenused()
        self.salvesta_andmed_andmefaili(self.teenused, "teenused.csv")

    def koosta_arve(self):
        valitud_indeksid = self.teenuste_listbox.curselection()
        if not valitud_indeksid:
            messagebox.showwarning("Hoiatus", "Palun vali vähemalt üks teenus arve koostamiseks.")
            return

        valitud_teenused = [self.teenused[index] for index in valitud_indeksid]
        uus_arve = Arve()
        for teenus in valitud_teenused:
            uus_arve.lisateenus(teenus)

        arve_tekst = f"Arve sisu:\n"
        for teenus in uus_arve.teenused:
            arve_tekst += f"{teenus.kirjeldus} - {teenus.hind}€\n"

        arve_tekst += f"\nKogusumma: {uus_arve.arve_summa()}€"
        self.arve_tekst.delete(1.0, tk.END)
        self.arve_tekst.insert(tk.END, arve_tekst)

        # Küsi kas kasutaja soovib salvestada uue arve või muuta olemasolevat
        kas_uus_arve = messagebox.askyesno("Arve Salvestamine", "Kas soovid salvestada uue arve?")
        if kas_uus_arve:
            # Salvesta uus arve CSV-faili
            self.salvesta_arve_csv_faili(uus_arve, f"arve_{len(self.arved)+1}.csv")
            self.arved.append(uus_arve)
            messagebox.showinfo("Arve Koostatud", f"Arve summa: {uus_arve.arve_summa()}€")
        else:
            # Küsi, kas muuta olemasolevat arvet
            muuda_olemasolevat = messagebox.askyesno("Arve Muutmine", "Kas soovid muuta olemasolevat arvet?")
            if muuda_olemasolevat:
                self.muuda_arve(uus_arve)

    def vaata_arveid(self):
        if not self.arved:
            messagebox.showinfo("Arved", "Arveid ei ole veel koostatud.")
            return

        arved_nimekiri = ""
        for i, arve in enumerate(self.arved, start=1):
            arved_nimekiri += f"Arve {i}, Kogusumma: {arve.arve_summa()}€\n"

        valitud_arve = simpledialog.askinteger("Vali Arve", f"Vali arve (1-{len(self.arved)}):\n{arved_nimekiri}", minvalue=1, maxvalue=len(self.arved))
        if valitud_arve:
            valitud_arve_index = valitud_arve - 1
            muudetav_arve = self.arved[valitud_arve_index]

            arve_tekst = f"Arve sisu:\n"
            for teenus in muudetav_arve.teenused:
                arve_tekst += f"{teenus.kirjeldus} - {teenus.hind}€\n"

            arve_tekst += f"\nKogusumma: {muudetav_arve.arve_summa()}€"
            self.arve_tekst.delete(1.0, tk.END)
            self.arve_tekst.insert(tk.END, arve_tekst)

            muudatused = messagebox.askyesno("Muuda Arvet", "Kas soovid muuta selle arve sisu?")
            if muudatused:
                self.muuda_arve(muudetav_arve)
            else:
                # Kui kasutaja ei soovi muudatusi, küsime, kas kustutada arve
                kustutada = messagebox.askyesno("Kustuta Arve", "Kas soovid kustutada selle arve?")
                if kustutada:
                    self.arved.remove(muudetav_arve)
                    # Kustuta arve CSV-fail
                    self.kustuta_arve_csv_fail(muudetav_arve)

    def muuda_arve(self, arve):
        muudatused_nimekiri = [teenus.kirjeldus for teenus in arve.teenused]

        while True:
            muudatus = simpledialog.askstring("Muuda Arve", f"Muuda teenuseid (sisesta teenuse kirjeldus või 'lõpeta' lõpetamiseks):\n{muudatused_nimekiri}")
            if muudatus.lower() == 'lõpeta':
                break

            leitud_teenus = None
            for teenus in self.teenused:
                if teenus.kirjeldus.lower() == muudatus.lower():
                    leitud_teenus = teenus
                    break

            if leitud_teenus:
                lisada = messagebox.askyesno("Muuda Arve", f"Kas soovid lisada teenuse '{leitud_teenus.kirjeldus}' arvele?")
                if lisada:
                    arve.lisateenus(leitud_teenus)
                    muudatused_nimekiri.append(leitud_teenus.kirjeldus)
                else:
                    eemaldada = messagebox.askyesno("Muuda Arve", f"Kas soovid eemaldada teenuse '{leitud_teenus.kirjeldus}' arvelt?")
                    if eemaldada:
                        try:
                            indeks = muudatused_nimekiri.index(leitud_teenus.kirjeldus)
                            arve.eemaldateenus(indeks)
                            muudatused_nimekiri.remove(leitud_teenus.kirjeldus)
                        except ValueError:
                            pass

        arve_tekst = f"Arve sisu:\n"
        for teenus in arve.teenused:
            arve_tekst += f"{teenus.kirjeldus} - {teenus.hind}€\n"

        arve_tekst += f"\nKogusumma: {arve.arve_summa()}€"
        self.arve_tekst.delete(1.0, tk.END)
        self.arve_tekst.insert(tk.END, arve_tekst)

        # Salvesta muudetud arve CSV-faili
        arve_indeks = self.arved.index(arve)
        self.salvesta_arve_csv_faili(arve, f"arve_{arve_indeks + 1}.csv")

    def salvesta_arve_csv_faili(self, arve, failinimi):
        arve_dict = arve.to_dict()
        with open(failinimi, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Teenuse kirjeldused"] + arve_dict['Teenuse kirjeldused'])
            writer.writerow(["Teenuste hinnad"] + arve_dict['Teenuste hinnad'])
            writer.writerow(["Kogusumma", arve_dict['Kogusumma']])

    def kustuta_arve_csv_fail(self, arve):
        try:
            arve_indeks = self.arved.index(arve)
            failinimi = f"arve_{arve_indeks + 1}.csv"
            os.remove(failinimi)
        except (FileNotFoundError, ValueError):
            pass

    def salvesta_andmed_andmefaili(self, andmed, andmefaili_nimi):
        with open(andmefaili_nimi, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for rida in andmed:
                writer.writerow([rida.kirjeldus, rida.hind])

    def laadi_andmed_andmefailist(self, andmefaili_nimi):
        andmed = []
        try:
            with open(andmefaili_nimi, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                for rida in reader:
                    andmed.append(Teenus(rida[0], float(rida[1])))
        except FileNotFoundError:
            pass
        return andmed

    def laadi_arved_csv_failidest(self):
        arved = []
        for failinimi in os.listdir():
            if failinimi.startswith("arve_") and failinimi.endswith(".csv"):
                arve = self.laadi_arve_csv_failist(failinimi)
                arved.append(arve)
        return arved

    def laadi_arve_csv_failist(self, failinimi):
        with open(failinimi, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            kirjeldused = next(reader)[1:]
            hinnad = next(reader)[1:]
            kogusumma = float(next(reader)[1])

            arve = Arve()
            for kirjeldus, hind_str in zip(kirjeldused, hinnad):
                hind = float(hind_str)
                teenus = Teenus(kirjeldus, hind)
                arve.lisateenus(teenus)

            return arve

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ArveteRakendus(root)
    app.run()
