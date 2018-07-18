"""
Given a String S with width W
Your task is to wrap the string into a paragraph of width W.
"""
import textwrap

def wrap(string, max_width):
  return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
