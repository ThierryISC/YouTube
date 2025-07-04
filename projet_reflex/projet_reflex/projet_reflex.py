import reflex as rx


class State(rx.State):
    nom: str = ""
    compteur: int = 0

    @rx.var
    def bonjour(self) -> str:
        return f"Bonjour {self.nom} !"

    def on_click(self):
        self.compteur += 1

    @rx.var
    def message_compteur(self) -> str:
        return f"Tu as cliqué {self.compteur} fois."


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Informatique Sans Complexe !"),
            rx.button("Clique-moi !", on_click=State.on_click),
            rx.text(State.message_compteur),
            rx.input(placeholder="Ton prénom", on_change=State.set_nom),
            rx.text(State.bonjour)
        ))


app = rx.App()
app.add_page(index)
