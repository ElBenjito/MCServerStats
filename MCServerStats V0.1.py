import requests
import tkinter as tk
from tkinter import messagebox

def get_joueurs(ip):
    url = "https://api.mcsrvstat.us/2/{}".format(ip)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "players" in data and "online" in data["players"]:
            nombre_joueurs = data["players"]["online"]
            messagebox.showinfo("Joueurs en ligne", "Il y a actuellement {} joueur(s) sur {}".format(nombre_joueurs, ip))
        else:
            messagebox.showerror("Erreur", "Les informations sur le nombre de joueurs ne sont pas disponibles.")
    else:
        messagebox.showerror("Erreur", "Une erreur est survenue lors de la récupération des données : {}".format(response.status_code))

def on_button_click():
    ip = entry.get()
    get_joueurs(ip)

root = tk.Tk()
root.title("MCServerStats by ElBenjito_ V0.1")
root.geometry("400x100")

label = tk.Label(root, text="Adresse IP du serveur :")
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Obtenir le nombre de joueurs", command=on_button_click)
button.pack()

root.mainloop()

#Dev by ElBenjito#3930
#Thx to mcservstats for API <3
