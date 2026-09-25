from __future__ import annotations
from typing import Any, Iterator


class FrozenDict:
    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = dict(data)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        raise TypeError("FrozenDict est immuable")

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __hash__(self) -> int:
        return hash(frozenset(self._data.items()))
