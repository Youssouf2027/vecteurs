from __future__ import annotations
from types import TracebackType
from typing import Literal


class Transaction:
    def __init__(self, nom: str) -> None:
        self.nom = nom
        self.changements: list[str] = []

    def __enter__(self) -> "Transaction":
        print(f"Début de la transaction : {self.nom}")
        return self

    def ajouter(self, changement: str) -> None:
        self.changements.append(changement)
        print(f"  Changement ajouté : {changement}")

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> Literal[False]:
        if exc_type is None:
            print(f"Commit de la transaction : {self.nom} ({len(self.changements)} changement(s))")
        else:
            print(f"Rollback de la transaction : {self.nom} — erreur : {exc_value}")
        return False


if __name__ == "__main__":
    with Transaction("achat") as t:
        t.ajouter("débiter compte A de 50€")
        t.ajouter("créditer compte B de 50€")

    print()

    try:
        with Transaction("virement raté") as t:
            t.ajouter("débiter compte A de 100€")
            raise ValueError("solde insuffisant")
    except ValueError as e:
        print(f"Exception récupérée après le with : {e}")