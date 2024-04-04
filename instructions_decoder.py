# ID успешной посылки - 111346648.

def decode_instructions(instructions: str) -> str:
    stack: list = []
    actions_quantity: str = ''
    result: str = ''
    for element in instructions:
        if element.isdigit():
            actions_quantity += element
        elif element == '[':
            stack.append(int(actions_quantity))
            stack.append(result)
            actions_quantity = ''
            result = ''
        elif element == ']':
            result_in_stack = stack.pop()
            multiplier = stack.pop()
            result = result_in_stack + multiplier * result
        else:
            result += element
    return result


if __name__ == '__main__':
    print(decode_instructions(input()))
