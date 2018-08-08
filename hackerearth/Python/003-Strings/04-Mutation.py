"""
You are given an immutable string, and you want to make changes to it.
Read a given string, change the character at a given index and then print the modified string
"""
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
