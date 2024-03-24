# ID успешной посылки - 110520852.
array = input().split()
weight_of_robots = [int(item) for item in array]
platform_limit = int(input())


def get_platforms_quantity(robots: list, limit: int) -> int:

    robots.sort()
    platforms_quantity = 0
    left_pointer = 0
    right_pointer = len(robots) - 1

    while left_pointer <= right_pointer:
        result = robots[left_pointer] + robots[right_pointer]
        if result > limit:
            platforms_quantity += 1
            right_pointer -= 1
        else:
            platforms_quantity += 1
            right_pointer -= 1
            left_pointer += 1
        if left_pointer == right_pointer:
            platforms_quantity += 1
            break

    return platforms_quantity


if __name__ == '__main__':
    print(get_platforms_quantity(weight_of_robots, platform_limit))
