n = int(input())
names_grades = [[input(), float(input())] for _ in range(n)]

second_lowest = sorted(set([grade for name, grade in names_grades]))[1]

result = [name for name, grade in names_grades if grade == second_lowest]

print(*sorted(result),sep='\n')
