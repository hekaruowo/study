# def distance_between_points(a, b):
#     if a == b:
#         k = 0;
#     elif a < b:
#         k = b - a;
#     else:
#         k = a - b;
#     return k;
# print(distance_between_points(1, 1))
# print(distance_between_points(-12, 12))
# print(distance_between_points(23, -32))

def distance_between_points(a1, a2):
    import math
    d = a.x - b.x
    c = a.y - b.y
    return math.sqrt(d ** 2 + c ** 2)