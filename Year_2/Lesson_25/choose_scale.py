def choose_scale(kind):
    if kind == 'country':
        return 1
    if kind == 'province':
        return 3
    if kind == 'area':
        return 4
    if kind == 'locality':
        return 5
    if kind == 'district':
        return 6
    if kind == 'street':
        return 7
    if kind == 'house':
        return 8
