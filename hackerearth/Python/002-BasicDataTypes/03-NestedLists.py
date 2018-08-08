"""
Given the names and grades for each student in a Physics class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""
#Read input and append the list to main records list using List Compression
records = [[input(),float(input())] for i in range(int(input()))]

#sort the list using list compression set will avoid duplicates
mk_lst  = sorted(set(x[1] for x in records))

#loop through records and if marks matches with second highest sort and display 
the names
for name in sorted(x[0] for x in records if x[1] == mk_lst[1]):
        print(name)
