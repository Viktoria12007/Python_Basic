import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: int | float) -> int | float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int | float) -> int | float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, edge_len: int | float) -> int | float:
        return edge_len ** 3

    @classmethod
    def sphere_area(cls, radius: int | float) -> int | float:
        return math.pi * 4 * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(edge_len=5)
res_4 = MyMath.sphere_area(radius=6)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
