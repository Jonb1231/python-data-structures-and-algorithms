
from structures.dynamic_array import DynamicArray

MODULUS = 10**16 + 61


def missing_odds(inputs: list[int]) -> int:
    maximum = None
    minimum = None
    odd_sum_present = 0
    for number in inputs:
        if number % 2 != 0:
            odd_sum_present += number
        maximum = number if maximum is None or number > maximum else maximum
        minimum = number if minimum is None or number < minimum else minimum

    first_odd = minimum if minimum % 2 != 0 else minimum + 1
    last_odd = maximum if maximum % 2 != 0 else maximum - 1
    total_odd_sum = sum(range(first_odd, last_odd + 1, 2)) if first_odd <= last_odd else 0
    return total_odd_sum - odd_sum_present


def k_cool(k: int, n: int) -> int:
    value = 0
    power = 0
    while n > 0:
        if n & 1:
            value = (value + pow(k, power, MODULUS)) % MODULUS
        n >>= 1
        power += 1
    return value


def number_game(numbers: list[int]) -> tuple[str, int]:
    array = DynamicArray()
    for number in numbers:
        array.append(number)
    array.sort()
    array.reverse()

    alice = 0
    bob = 0
    for i in range(array.get_size()):
        value = array.get_at(i)
        if i % 2 == 0:
            if value % 2 == 0:
                alice += value
        else:
            if value % 2 != 0:
                bob += value
    if alice > bob:
        return 'Alice', alice
    if bob > alice:
        return 'Bob', bob
    return 'Tie', alice


def road_illumination(road_length: int, poles: list[int]) -> float:
    array = DynamicArray()
    for pole in poles:
        array.append(pole)
    array.sort()
    size = array.get_size()
    end_gap = max(array[0], road_length - array[size - 1])
    between_gap = 0
    for i in range(size - 1):
        gap = array[i + 1] - array[i]
        if gap > between_gap:
            between_gap = gap
    return max(end_gap, between_gap / 2)
