from __future__ import annotations
import pytest
import time
from vecteurs.decorateurs import chrono, debug, retry
from vecteurs.Transaction import Transaction


# ── chrono ────────────────────────────────────────────────────────────────────

def test_chrono_retourne_resultat() -> None:
    @chrono
    def addition(a: int, b: int) -> int:
        return a + b
    assert addition(2, 3) == 5

def test_chrono_preserve_nom() -> None:
    @chrono
    def ma_fonction() -> int:
        return 42
    assert ma_fonction.__name__ == "ma_fonction"

def test_chrono_affiche_message(capsys: pytest.CaptureFixture[str]) -> None:
    @chrono
    def rapide() -> None:
        pass
    rapide()
    out = capsys.readouterr().out
    assert "rapide" in out
    assert "secondes" in out


# ── debug ─────────────────────────────────────────────────────────────────────

def test_debug_retourne_resultat() -> None:
    @debug
    def multiplication(a: int, b: int) -> int:
        return a * b
    assert multiplication(3, 4) == 12

def test_debug_preserve_nom() -> None:
    @debug
    def ma_fonction() -> int:
        return 0
    assert ma_fonction.__name__ == "ma_fonction"

def test_debug_affiche_appel(capsys: pytest.CaptureFixture[str]) -> None:
    @debug
    def addition(a: int, b: int) -> int:
        return a + b
    addition(1, 2)
    out = capsys.readouterr().out
    assert "addition" in out
    assert "3" in out


# ── retry ─────────────────────────────────────────────────────────────────────

def test_retry_succes_premier_essai() -> None:
    appels = [0]
    @retry(3, 0)
    def fonction() -> str:
        appels[0] += 1
        return "ok"
    assert fonction() == "ok"
    assert appels[0] == 1

def test_retry_reessaie_puis_succes() -> None:
    appels = [0]
    @retry(3, 0)
    def fonction() -> str:
        appels[0] += 1
        if appels[0] < 3:
            raise ValueError("pas encore")
        return "ok"
    assert fonction() == "ok"
    assert appels[0] == 3

def test_retry_epuise_toutes_tentatives() -> None:
    @retry(3, 0)
    def toujours_echoue() -> None:
        raise RuntimeError("toujours raté")
    with pytest.raises(RuntimeError):
        toujours_echoue()

def test_retry_preserve_nom() -> None:
    @retry(3, 0)
    def ma_fonction() -> None:
        pass
    assert ma_fonction.__name__ == "ma_fonction"

def test_retry_releve_derniere_exception() -> None:
    compteur = [0]
    @retry(3, 0)
    def fonction() -> None:
        compteur[0] += 1
        raise ValueError(f"erreur {compteur[0]}")
    with pytest.raises(ValueError, match="erreur 3"):
        fonction()


# ── Transaction ───────────────────────────────────────────────────────────────

def test_transaction_commit() -> None:
    with Transaction("test") as t:
        t.ajouter("op1")
        t.ajouter("op2")
    assert len(t.changements) == 2

def test_transaction_rollback_ne_faut_pas_avaler() -> None:
    with pytest.raises(ValueError):
        with Transaction("test") as t:
            t.ajouter("op1")
            raise ValueError("erreur volontaire")

def test_transaction_retourne_false() -> None:
    t = Transaction("test")
    result = t.__exit__(None, None, None)
    assert result is False

def test_transaction_changements_vides_au_debut() -> None:
    with Transaction("test") as t:
        assert t.changements == []
