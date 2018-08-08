"""
You have to print a list of all possible coordinates given by(i,j,k) on a 3D grid where the sum of i+j+k is not equal to N
"""
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    N = int(raw_input())
    
    arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]
    print(arr)
