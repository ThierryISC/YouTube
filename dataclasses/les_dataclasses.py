

from dataclasses import dataclass

@dataclass(frozen=True)
class Utilisateur:
    nom: str
    email: str

u = Utilisateur(nom="Alice", email="alice@test.com")

print(u)

def modifie_utlisateur(user):
    user.nom = "COUCOU"

modifie_utlisateur(u)
print(u)
