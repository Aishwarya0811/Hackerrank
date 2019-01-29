n = int(input())
names_grades = [[input(), float(input())] for _ in range(n)]

second_lowest = sorted(set([grade for name, grade in names_grades]))[1]

result = [name for name, grade in names_grades if grade == second_lowest]

print(*sorted(result),sep='\n')



marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
