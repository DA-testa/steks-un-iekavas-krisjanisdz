# python3

from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    d = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, d+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return d+1
            opening_brackets_stack.pop()
            
        d = d + 1
        
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
