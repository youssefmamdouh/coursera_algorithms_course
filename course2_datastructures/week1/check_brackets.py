# python3

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = input()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i+1))

        elif next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0 \
                    or not opening_brackets_stack.pop(len(opening_brackets_stack)-1).Match(next):
                print(i+1)
                exit()

    if len(opening_brackets_stack) > 0:
        print(opening_brackets_stack[len(opening_brackets_stack)-1].position)
    else:
        print("Success")
