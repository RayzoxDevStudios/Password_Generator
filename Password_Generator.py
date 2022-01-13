from random import randint, choice
import string
from tkinter import *

# Créer une première fenêtre
window = Tk()

# Création de la fonction permettant de générer le mot de passe
def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# Personalisation de la fenêtre
window.title("Générateur de Mot de Passe")
window.geometry("720x480")  # Taille par défaut de la fenêtre quand elle s'ouvre
window.minsize(480, 360)  # Taille minimum de la fenêtre
window.maxsize(1080, 720)  # Taille maximum de la fenêtre
window.iconbitmap("logo.ico")  # Logo de la fenêtre en haut à gauche
window.config(background='#4065A4')  # Couleur du fond

# Création de la frame principale
master_frame = Frame(window, bg='#4065A4')

# Création de l'image
width = 300
height = 300
image = PhotoImage(file="mot-de-passe.png").zoom(18).subsample(32)
canvas = Canvas(master_frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W) # On peut utiliser aussi .pack

# Créer une sous-boîte
right_frame = Frame(master_frame, bg='#4065A4')

# Créer un titre
label_title = Label(right_frame, text="Mot De Passe", font=("Courrier", 20), bg='#4065A4',
                    fg='white')  # On peut aussi mettre window a la place de frame
label_title.pack()

# Créer un champ/entrée/input
password_entry = Entry(right_frame, font=("Courrier", 20), bg='#4065A4',
                    fg='white')
password_entry.pack()

# Créer un bouton
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg='#4065A4',
                    fg='white', command=generate_password)  # On peut aussi mettre window a la place de frame
generate_password_button.pack(fill=X)

# On place la sous-boîte a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W) # On peut utiliser aussi .pack

# Afficher la frame
master_frame.pack(expand=YES)

# Afficher cette fenêtre
window.mainloop()