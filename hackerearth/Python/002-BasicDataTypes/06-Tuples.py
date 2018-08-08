"""
Compute hash(): 
I/p : 1st Line - Tuple size
      2nd Line - Tuple members.
O/p : Hash()
"""
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print hash(integer_list)
