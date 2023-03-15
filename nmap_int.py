import tkinter as tk
import subprocess

# Fonction qui exécute la commande nmap et affiche le résultat dans le widget Text
def run_nmap(command):
    result = subprocess.run(command.split(), capture_output=True, text=True)
    output_text.delete(1.0, tk.END)  # Efface le contenu précédent du widget Text
    output_text.insert(tk.END, result.stdout)  # Insère le résultat dans le widget Text

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface Nmap")

# Création des boutons
button1 = tk.Button(root, text="Scan du réseau", command=lambda: run_nmap("nmap -sn 192.168.0.0/24"))
button2 = tk.Button(root, text="Scan de ports", command=lambda: run_nmap("nmap -p 1-1024 192.168.0.253"))

# Placement des boutons dans la fenêtre
button1.pack()
button2.pack()

# Création du widget Text pour afficher le résultat
output_text = tk.Text(root, height=10, width=80)
output_text.pack()

# Lancement de la boucle principale de la fenêtre
root.mainloop()
