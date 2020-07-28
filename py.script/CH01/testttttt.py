def solution(num):
    new = 0
    for i in str(num):
        new = new + int(i)
    return new

print(solution(456))
