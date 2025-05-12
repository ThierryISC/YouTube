import time
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.progress import track
from rich.markdown import Markdown

console = Console()

contenu = """
# Rich est une super bibliothèque pour mettre en forme la console !
- Attribut comme *italique* ou *gras*
"""
console.print(Markdown(contenu))

console.print("\n")
tree = Tree("📂 Arbre")
src = tree.add("📂 Répertoire")
src.add("📄 fichier")
console.print(tree)
console.print("\n")
table = Table(title="Tableau")
table.add_column("Nombre", style="green", justify="center")
table.add_column("Carré", justify="center")
table.add_row("2", "4")
table.add_row("3", "9")
console.print(table)
console.print("[bold]Barre de progression[/bold]")
for etape in track(range(10), description="Traitement..."):
    time.sleep(0.2)