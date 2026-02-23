import math 

r = int(input("원의 반지름을 입력하세요: "))
area = r**2 * math.pi
circumference = 2 * r * math.pi  

print(f"반지름이 {r}인 원의 넓이: {area:.2f}")
print(f"반지름이 {r}인 원의 둘레: {circumference:.2f}")