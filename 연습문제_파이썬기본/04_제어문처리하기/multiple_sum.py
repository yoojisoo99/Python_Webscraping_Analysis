sum = 0
list = []
for i in range(1, 101):
    if i % 3 == 0:
        list.append(i)
        sum += i
print(f"1부터 100까지 3의 배수: {list}")
print(f"3의 배수의 합: {sum}")
print(f"3의 배수의 개수: {len(list)}개")