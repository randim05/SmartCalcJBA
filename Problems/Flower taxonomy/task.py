iris = {}


def add_iris(id_n, species, petal_length, petal_width, **ph):
    if id_n in iris:
        iris[id_n]['species'] = species
        iris[id_n]['petal_length'] = petal_length
        iris[id_n]['petal_width'] = petal_width
        for i in ph.keys():
            iris[id_n][i] = ph[i]
    else:
        iris[id_n] = {}
        iris[id_n]['species'] = species
        iris[id_n]['petal_length'] = petal_length
        iris[id_n]['petal_width'] = petal_width
        for i in ph.keys():
            iris[id_n][i] = ph[i]