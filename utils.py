import random

def random_values(total, n):
    values = []
    for _ in range(n - 1):
        value = random.uniform(0, total)
        values.append(value)
        total -= value
    values.append(total)
    random.shuffle(values)
    return values