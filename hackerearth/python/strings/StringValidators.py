"""
Given a string S; find whether S has
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()
    for f in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(getattr(c, f)() for c in s))
