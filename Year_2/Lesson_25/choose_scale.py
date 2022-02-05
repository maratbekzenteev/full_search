def choose_scale(kind):
    if kind == 'country':
        return 2
    if kind == 'province':
        return 4
    if kind == 'area':
        return 6
    if kind == 'locality':
        return 8
    if kind == 'district':
        return 10
    if kind == 'street':
        return 14
    if kind == 'house':
        return 16
