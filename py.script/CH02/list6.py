avg = 0.0; total =0
student =[]
grades = []
for i in range(3):
    student.append(input("전공, 학번, 이름 순서로 입력 >> "))

for i in range(4):
    grades.append(float(input("과목%s 점수 입력 >> "%str(i+1))))
    total += grades[i]
avg = total/len(grades) 
print('*'*60)
for i in student:
    print(f'{i}', end ='\t')
print()
for grade in grades:
    print(f'{grade}', end ='\t')
print("평균 점수는 %.2f"%avg)