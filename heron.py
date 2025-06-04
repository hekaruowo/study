def heron(a, b, c):
    s = (a + b + c) / 2
    import math
    return math.sqrt(s * (s - a) * (s - b) * (s - c))