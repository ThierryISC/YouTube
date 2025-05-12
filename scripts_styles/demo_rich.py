import time
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.progress import track
from rich.markdown import Markdown
import rich.traceback

console = Console()

rich.traceback.install()

def plante():
    return 1/0

contenu = """
# Titre 1
## Titre 2

Voici une *liste* :
- Python
- Java
- C++

**Mot en gras**

[Ceci est un lien](https://www.informatiquesanscomplexe.com)
"""

console.print(Markdown(contenu))


console.print("[bold]Traitement des fichiers[/bold]")
for etape in track(range(100), description="Chargement..."):
    time.sleep(0.01)



tree = Tree('📂 Mes fichiers')
src = tree.add("📂 src")
src.add("📄 fichier1.py")
src.add("📄 fichier2.py")

docs = tree.add("📂 docs")
docs.add("📄 readme.txt")

console.print(tree)

table = Table(title="Voiture de sport")

table.add_column("Modèle", style="cyan")
table.add_column("Puissance", justify="center")

table.add_row("Ferrari", "1000 Ch")
table.add_row("Porshe", "650 Ch")
table.add_row("Mc Laren", "745 Ch")

console.print(table)

console.print("[bold]Texte en gras[/bold]")
console.print("[italic]Texte en italique[/italic]")
console.print("[red]Texte en rouge[/red]")
console.print("[green italic]Texte en italique vert[/green italic]")


plante()
