def brackets(s):
    if not (1 <= len(s) <= 100):
        return "not valid"
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for char in s:
        if char in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[stack.pop()] != char:
            return "not valid"
    return "valid" if not stack else "not valid"

str_input = input()
hasil= brackets(str_input)
print(hasil)
