import datetime
import random

now = datetime.datetime.now()

days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
formatted_date = now.strftime(f"%Y년 %m월 %d일 {days[now.weekday()]}")

random_int = random.randint(1, 10)          
random_float = round(random.uniform(1, 5), 2) 
fruits = ['포도', '사과', '오렌지', '바나나', '딸기']
random_element = random.choice(fruits)

# 4. 리스트 섞기
shuffled_list = fruits.copy()
random.shuffle(shuffled_list)

# --- 출력 부분 ---
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"포맷된 날짜: {formatted_date}")
print(f"임의의 숫자: {random_int}")
print(f"임의의 실수: {random_float}")
print(f"임의의 리스트 요소: {random_element}")
print(f"섞인 리스트: {shuffled_list}")