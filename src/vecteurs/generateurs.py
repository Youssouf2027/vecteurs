from __future__ import annotations
from typing import Iterator, TypeVar, Callable, Any, Iterable

T = TypeVar("T")
K = TypeVar("K")


def charger(chemin: str) -> Iterator[str]:
    with open(chemin) as f:
        for ligne in f:
            yield ligne


def mon_chain(*iterables: Iterable[T]) -> Iterator[T]:
    for iterable in iterables:
        for item in iterable:
            yield item


def mon_islice(iterable: Iterable[T], start: int, stop: int) -> Iterator[T]:
    for i, item in enumerate(iterable):
        if i >= start and i < stop:
            yield item
        elif i >= stop:
            break


def mon_groupby(iterable: Iterable[T], key: Callable[[T], K]) -> Iterator[tuple[K, list[T]]]:
    iterator = iter(iterable)
    try:
        current_item = next(iterator)
    except StopIteration:
        return
    current_key = key(current_item)
    group: list[T] = [current_item]

    for item in iterator:
        item_key = key(item)
        if item_key == current_key:
            group.append(item)
        else:
            yield (current_key, group)
            current_key = item_key
            group = [item]

    yield (current_key, group)


if __name__ == "__main__":
    result = list(mon_chain([1, 2, 3], ['a', 'b'], [True, False]))
    print(result)

    result2 = list(mon_islice(range(10), 3, 7))
    print(result2)

    data = [1, 1, 2, 2, 2, 3, 3, 1]
    result3 = list(mon_groupby(data, lambda x: x))
    print(result3)
