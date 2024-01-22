def brackets(s):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or stack.pop() != brackets_map[char]:
                return "not valid"
    return "valid" if not stack else "not valid"
str_input = input()
if not (1 <= len(str_input) <= 100):
    print("out of bounds")
hasil = brackets(str_input)
print(hasil)
