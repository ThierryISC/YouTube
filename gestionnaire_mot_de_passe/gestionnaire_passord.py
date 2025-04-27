import os
from cryptography.fernet import Fernet
import sqlite3
import string
import secrets
import pyperclip

KEY_FILE = "passwords.key"
DB_FILE = "passwords.db"


def generer_cle():
    if not os.path.exists(KEY_FILE):
        cle = Fernet.generate_key()
        with open(KEY_FILE, "wb") as fichier:
            fichier.write(cle)


def charger_cle():
    with open(KEY_FILE, "rb") as fichier:
        return fichier.read()


def initialise_base():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS passwords (
                     id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     site TEXT NOT NULL, 
                     login TEXT NOT NULL, 
                     password TEXT NOT NULL)
                """)
    conn.commit()
    conn.close()


def generer_mot_de_passe(longueur=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(longueur))

def ajouter_password(site, login, password, fernet):
    encrypted = fernet.encrypt(password.encode()).decode()
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO passwords (site, login, password) VALUES (?, ?, ?)", (site, login, encrypted))
    conn.commit()
    pyperclip.copy(password)
    print(f"Mot de passe pour le site {site} copié dans le presse-papier")


def liste_passwords():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT site, login FROM passwords")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("Pas de données !")
    else:
        print("Liste des mots de passe :")
        for site, login in rows:
            print(f"Site : {site} | Login : {login} | Mot de passe : ***********")


def recherche_password(requete, fernet):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT site, login, password FROM passwords WHERE site LIKE ?", (f"%{requete}%",))
    row = cur.fetchone()
    conn.close()

    if not row:
        print('Aucun résultat')
    else:
        site, login, password = row
        mot_de_passe = fernet.decrypt(password.encode()).decode()
        pyperclip.copy(mot_de_passe)
        print(f"Mot de passe pour le site {site} copié dans le presse-papier")

generer_cle()
fernet = Fernet(charger_cle())
initialise_base()

while True:
    print("Option : (g)énérer / (l)ister / (r)echercher / (q)uitter")
    choix = input("Entrez votre choix : ")

    if choix == "g":
        site = input("Entrez le site : ")
        login = input("Entrez le login : ")
        password = generer_mot_de_passe()
        ajouter_password(site, login, password, fernet)
    elif choix == "l":
        liste_passwords()
    elif choix == "r":
        requete = input("Mot-clé : ")
        recherche_password(requete, fernet)
    elif choix == "q":
        print('Au revoir !')
        break
    else:
        print("Option invalide !")
