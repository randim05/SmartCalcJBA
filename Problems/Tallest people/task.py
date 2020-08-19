def tallest_people(**arg):
    c = sorted(dict(arg))
    max = []
    for i in c:
        if not max:
            max.append(i)
        else:
            if arg[i] > arg[max[0]]:
                max = []
                max.append(i)
            elif arg[i] == arg[max[0]]:
                max.append(i)

    for u in max:
        print(f'{u} : {arg[u]}')
