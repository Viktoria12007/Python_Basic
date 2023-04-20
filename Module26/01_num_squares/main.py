from collections.abc import Iterable


class SquaresNumbers:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__counter = 0

    def __iter__(self) -> 'SquaresNumbers':
        self.__counter = 0
        return self

    def __next__(self) -> int | Exception:
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration


def squares_numbers(limit: int) -> Iterable[int]:
    for cur_val in range(1, limit + 1):
        yield cur_val ** 2


limit = int(input('Введите число N: '))

for square_number in SquaresNumbers(limit):
    print(square_number, end=" ")
print()

for square_number in squares_numbers(limit):
    print(square_number, end=" ")
print()

squares_numbers_2 = (number ** 2 for number in range(1, limit + 1))

for square_number in squares_numbers_2:
    print(square_number, end=" ")
