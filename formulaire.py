#importation du datetime

from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import *
#import module gérant les fichiers

from os import path


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.init_file_csv()
        self.fn_creer_widgets()
        self.load_bdd()

    def msg_error(self, erreur):
        messagebox.showinfo("Erreur", erreur)

    def msg_saved(self):
        messagebox.showinfo("Info", "Les données ont été correctement enregistrer")

    def init_file_csv(self):
        self.init_formulaire_csv = "Formulaire.csv"
        if not path.exists(self.init_formulaire_csv):
            try:
                self.formulaire_csv = open("Formulaire.csv", "w", encoding="utf-8")
            except FileNotFoundError:
                self.msg_error("Fichier introuvable")
            except IOError:
                self.msg_error("Erreur d\'ouverture")
            header = "Nom,Prénom,Date de naissance"

            self.formulaire_csv.write(header)
            self.formulaire_csv.write("\n")
            self.formulaire_csv.close()

    def file_csv(self,list_value):
        print(list_value)
        line = ""
        sep = ","
        for x in list_value:
            line = line + x + sep
        line = line[:-1]

        print(line)
        try:
            self.formulaire_csv = open("Formulaire.csv", "a", encoding="utf-8")
        except FileNotFoundError:
            self.msg_error("Fichier introuvable")
        except IOError:
            self.msg_error("Erreur d\'ouverture")

        self.formulaire_csv.write(line)
        self.formulaire_csv.write("\n")
        self.formulaire_csv.close()

    def fn_read_file_csv(self):
        try :
            self.formulaire_csv = open("Formulaire.csv","r", encoding="utf-8")
        except FileNotFoundError:
            self.fn_msg_error("Fichier introuvable")
        except IOError :
            self.msg_error("Erreur d'ouverture")
            self.record_formulaire01 = self.formulaire_csv.readlines()




    def fn_creer_widgets(self):
        #variables
        self.nom_var = tk.StringVar()
        self.prenom_var = tk.StringVar()
        self.date_de_naissance_var = tk.StringVar()



        #def de widgets
        self.nom_label = tk.Label(self, text="Entrez votre nom")
        self.prenom_label = tk.Label(self, text="Entrez votre prénom")
        self.date_de_naissance_label = tk.Label(self, text = "Entrez votre date de naissance (jj-mm-aaaa)")

        #def des entry
        self.nom_entry = tk.Entry(self, textvariable=self.nom_var)
        self.prenom_entry = tk.Entry(self, textvariable=self.prenom_var)
        self.date_de_naissance_entry = tk.Entry(self, textvariable=self.date_de_naissance_var)

        #def des boutons
        self.enregistrer_b = tk.Button(self, text="Enregistrer", command=self.fn_enregistrer)
        self.lire_base_b = tk.Button(self, text="Charger la base de donnée", command=self.fn_read_file_csv)
        self.quitter_b = tk.Button(self, text="Quitter", command=self.quit)


        #implémentation des widgets
        self.nom_label.grid(column = 0, row = 0,pady = 2)
        self.nom_entry.grid(column =1, row = 0, pady = 2)
        self.prenom_label.grid(column = 0, row = 1, pady = 2)
        self.prenom_entry.grid(column =1, row = 1, pady = 2)
        self.date_de_naissance_label.grid(column =0, row = 2, pady = 2)
        self.date_de_naissance_entry.grid(column =1, row = 2, pady =2)
        self.enregistrer_b.grid(columnspan = 4, column = 1, row = 3, pady = 2)
        self.lire_base_b.grid(columnspan = 4, column = 1, row = 3, pady = 2)
        self.quitter_b.grid(columnspan = 1, column = 0, row = 3, pady = 2)

    def fn_enregistrer(self):

        self.nom= self.nom_var.get()
        self.prenom = self.prenom_var.get()
        self.date_de_naissance = self.date_de_naissance_var.get()
        self.erreur_nom = False
        self.erreur_prenom = False
        self.erreur_date_de_naissance = False
        self.erreur_nom_txt = ""
        self.erreur_prenom_txt = ""
        self.erreur_date_de_naissance_txt = ""
        self.list_value = []
        if not self.nom.isalpha():
            self.erreur_nom = True
            self.erreur_nom_txt = "Caractère(s) invalide(s) dans le nom\n"
        if not self.prenom.isalpha():
            self.erreur_prenom = True
            self.erreur_prenom_txt ="Caractère(s) invalide(s) dans le prenom\n"
        try:
            datetime.strptime(self.date_de_naissance,"%d-%m-%Y")
        except ValueError:
            self.erreur_date_de_naissance = True
            self.erreur_date_de_naissance_txt = "Date invalide"
        if self.erreur_nom or self.erreur_prenom or self.erreur_date_de_naissance:
            self.erreur_global = self.erreur_nom_txt + self.erreur_prenom_txt + self.erreur_date_de_naissance_txt
            self.msg_error(self.erreur_global)
        if not (self.erreur_nom or self.erreur_prenom or self.erreur_date_de_naissance):
            self.list_value.append(self.nom)
            self.list_value.append(self.prenom)
            self.list_value.append(self.date_de_naissance)
            self.file_csv(self.list_value)


            self.msg_saved()
            self.nom_var.set("")
            self.prenom_var.set("")
            self.date_de_naissance_var.set("")


if __name__ == "__main__":
    app = Application()
    app.title("formulaire")
    app.geometry("380x120")
    app.mainloop()
