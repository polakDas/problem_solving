def isValid(s: str) -> bool:
    if len(s) % 2:
        return False

    stack = []

    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if not stack:
                return False

            current = stack.pop()
            
            if current == '(':
                if c != ')':
                    return False
            if current == '{':
                if c != '}':
                    return False
            if current == '[':
                if c != ']':
                    return False
    if stack:
        return False
    return True

def main():
    s = "(){}{}[]"
    print(isValid(s))

if __name__ == "__main__":
    main()
 