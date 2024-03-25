# ID успешной посылки - 110555659.
from typing import Union


def get_platforms_quantity(robots: Union[str, list, tuple], limit: int) -> int:

    sequence_of_robots = sorted(robots)
    platforms_quantity = 0
    min_element_pointer = 0
    max_element_pointer = len(robots) - 1

    while min_element_pointer < max_element_pointer:

        if int(sequence_of_robots[min_element_pointer]) + int(
                sequence_of_robots[max_element_pointer]) <= limit:
            min_element_pointer += 1

        platforms_quantity += 1
        max_element_pointer -= 1

    if min_element_pointer == max_element_pointer:
        platforms_quantity += 1

    return platforms_quantity


if __name__ == '__main__':
    result = get_platforms_quantity(input().split(), int(input()))
    print(result)
