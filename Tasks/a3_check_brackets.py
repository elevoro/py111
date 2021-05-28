def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    stack = []
    for symb in brackets_row:
        if symb == '(':
            stack.append(")")
        elif symb == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


