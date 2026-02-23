score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "미성년자" if age < 19 else "성인"
print(f"나이: {age}, 상태: {status}")

a, b = 15, 42
max_val = a if a > b else b
print(f"숫자들의 최댓값: {max_val}")

numbers = [5, -3, 12, 8, -1, 23, 0]
positives = [n for n in numbers if n > 0]
print(f"양수들: {positives}")