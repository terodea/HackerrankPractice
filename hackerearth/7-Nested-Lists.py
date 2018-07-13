"""
"""
#Read input and append the list to main records list using List Compression
records = [[input(),float(input())] for i in range(int(input()))]

#sort the list using list compression set will avoid duplicates
mk_lst  = sorted(set(x[1] for x in records))

#loop through records and if marks matches with second highest sort and display 
the names
for name in sorted(x[0] for x in records if x[1] == mk_lst[1]):
        print(name)
