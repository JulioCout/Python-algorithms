# An algorithm that check if all "(", "[" and "{" are been opened and close correctly.

# Time: O(n)
# Memory: O(n)

string_to_check = "[a{b()(c)d}e2]"

def valid_parentheses(string_to_check):
    close_map = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    open_map = ["(", "{", "["]

    stack = []
    for c in string_to_check:
        if c in close_map:
            if stack and stack[-1] == close_map[c]:
                stack.pop()
            else:
                return False
        elif c in open_map:
            stack.append(c)
    return True if not stack else False

result = valid_parentheses(string_to_check)
print(result)