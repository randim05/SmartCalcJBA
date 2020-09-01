def startswith_capital_counter(names):
    counnt = 0
    if len(names) == 0:
        return 0
    for name in names:
        if name[0].isupper():
            counnt += 1
    return counnt