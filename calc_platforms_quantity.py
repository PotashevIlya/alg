# ID успешной посылки - 110571149.
from typing import Union


def calc_platforms_quantity(robots: Union[
        str, list, tuple, map], limit: int) -> int:

    weight_of_robots = sorted(robots)
    platforms_quantity = 0
    min_element_pointer = 0
    max_element_pointer = len(weight_of_robots) - 1

    while min_element_pointer < max_element_pointer:

        if weight_of_robots[min_element_pointer] + weight_of_robots[
                max_element_pointer] <= limit:
            min_element_pointer += 1

        platforms_quantity += 1
        max_element_pointer -= 1

    if min_element_pointer == max_element_pointer:
        platforms_quantity += 1

    return platforms_quantity


if __name__ == '__main__':
    print(calc_platforms_quantity(map(int, input().split()), int(input())))
