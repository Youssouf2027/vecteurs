def charger(chemin):
    with open(chemin) as f:
        for ligne in f:
            yield ligne



# écris une fonction mon_chain qui prend plusieurs itérables et les produit bout à bout avec yield

def mon_chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

def mon_islice(iterable, start, stop):
    for i, item in enumerate(iterable):
        if i >= start and i < stop:
            yield item
        elif i >= stop:
            break

def mon_groupby(iterable, key):
    iterator = iter(iterable)
    try:
        current_item = next(iterator)
    except StopIteration:
        return
    current_key = key(current_item)
    group = [current_item]
    
    for item in iterator:
        item_key = key(item)
        if item_key == current_key:
            group.append(item)
        else:
            yield (current_key, group)
            current_key = item_key
            group = [item]
    
    yield (current_key, group)