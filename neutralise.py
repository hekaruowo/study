def neutralise(s1, s2):
    p = ""
    for i in range(len(s1)):
        k = s1[i] + s2[i]
        if k == "+-" or  k == "-+":
            p = p + "0"
        elif k == "++":
            p = p +  "+"
        else:
            p = p + "-"
    return p




print(neutralise("+++", "-+-"))