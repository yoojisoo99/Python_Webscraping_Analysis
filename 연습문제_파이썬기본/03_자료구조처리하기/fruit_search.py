fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"과일 목록: {fruits}")
fruit = input("찾을 과일를 입력하세요: ")
if fruit in fruits:
    print(f"'{fruit}'가 목록에 있습니다!")
else:
    print(f"'{fruit}'가 목록에 없습니다!")