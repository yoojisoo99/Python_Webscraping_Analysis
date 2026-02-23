total = 0

while True:
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
    if num == 0:
        break  # 0을 입력하면 반복문 종료
    total += num  # 입력받은 숫자를 합계에 더함

print(f"입력한 숫자들의 합: {total}")