def quarter_of(month):
    if month / 3 <= 1:
        return 1
    elif month / 3 <= 2:
        return 2
    elif month / 3 <= 3:
        return 3
    else:
        return 4
print(quarter_of(3))