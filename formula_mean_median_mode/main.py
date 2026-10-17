def mean(items, frequency=None, continuous=False):

    # Individual series
    if frequency is None:
        return sum(items) / len(items)

    # Continuous series
    if continuous:
        midpoints = [(low + high) / 2 for low, high in items]

        total = sum(
            midpoints[i] * frequency[i]
            for i in range(len(items))
        )

        total_frequency = sum(frequency)

        return total / total_frequency

    # Discrete series
    total = sum(
        items[i] * frequency[i]
        for i in range(len(items))
    )

    total_frequency = sum(frequency)

    return total / total_frequency

def median(items, frequency=None, continuous=False):

    # Individual series
    if frequency is None:
        items = sorted(items)
        n = len(items)

        if n % 2 == 0:
            return (items[n // 2 - 1] + items[n // 2]) / 2

        return items[n // 2]

    # Discrete series
    if not continuous:
        data = []

        for i in range(len(items)):
            data.extend([items[i]] * frequency[i])

        data.sort()

        n = len(data)

        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2

        return data[n // 2]

    # Continuous series
    total_frequency = sum(frequency)
    cumulative = 0

    for i in range(len(items)):
        previous_cf = cumulative
        cumulative += frequency[i]

        if cumulative >= total_frequency / 2:
            L = items[i][0]
            f = frequency[i]
            h = items[i][1] - items[i][0]

            return L + ((total_frequency / 2 - previous_cf) / f) * h

def mode(items, frequency=None, continuous=False):

    # Individual series
    if frequency is None:
        return max(set(items), key=items.count)

    # Discrete series
    if not continuous:
        index = frequency.index(max(frequency))
        return items[index]

    # Continuous series
    modal_index = frequency.index(max(frequency))

    L = items[modal_index][0]
    h = items[modal_index][1] - items[modal_index][0]

    f1 = frequency[modal_index]

    f0 = frequency[modal_index - 1] if modal_index > 0 else 0
    f2 = frequency[modal_index + 1] if modal_index < len(frequency) - 1 else 0

    return L + ((f1 - f0) / (2 * f1 - f0 - f2)) * h