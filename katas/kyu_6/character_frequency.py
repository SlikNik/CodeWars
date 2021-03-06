from collections import Counter, defaultdict


def letter_frequency(text):
    by_value = defaultdict(list)
    for k, v in Counter(a.lower() for a in text if a.isalpha()).items():
        by_value[v].append((k, v))
    result = []
    for key in sorted(by_value, reverse=True):
        result.extend(sorted(by_value[key]))
    return result
