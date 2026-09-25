from __future__ import annotations
import time
import functools
from typing import TypeVar, Callable, Any
from collections.abc import Callable as CallableABC

F = TypeVar("F", bound=Callable[..., Any])


def chrono(fonction_originale: F) -> F:
    @functools.wraps(fonction_originale)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        resultat = fonction_originale(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{fonction_originale.__name__} a pris {fin - start:.6f} secondes")
        return resultat
    return wrapper  # type: ignore[return-value]


def debug(fonction_originale: F) -> F:
    @functools.wraps(fonction_originale)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Appel de {fonction_originale.__name__} avec {args} {kwargs}")
        resultat = fonction_originale(*args, **kwargs)
        print(f"{fonction_originale.__name__} a retourné {resultat}")
        return resultat
    return wrapper  # type: ignore[return-value]


def retry(n: int, delay: float) -> Callable[[F], F]:
    def decorateur(fonction_originale: F) -> F:
        @functools.wraps(fonction_originale)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            derniere_erreur: BaseException | None = None
            for _ in range(n):
                try:
                    return fonction_originale(*args, **kwargs)
                except Exception as e:
                    derniere_erreur = e
                    time.sleep(delay)
            assert derniere_erreur is not None
            raise derniere_erreur
        return wrapper  # type: ignore[return-value]
    return decorateur


if __name__ == "__main__":
    @chrono
    def somme(n: int) -> int:
        return sum(range(n))

    print(somme(1_000_000))

    @debug
    def addition(a: int, b: int) -> int:
        return a + b

    addition(20, 70)

    @retry(3, 0)
    def fonction_qui_echoue() -> None:
        raise ValueError("Ça ne marche jamais")

    try:
        fonction_qui_echoue()
    except ValueError as e:
        print(f"Erreur attrapée : {e}")