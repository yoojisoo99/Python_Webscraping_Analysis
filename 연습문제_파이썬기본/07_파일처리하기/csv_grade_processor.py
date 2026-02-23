import csv

data = [
    ['이름', '점수'],
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]

file_name = 'grades.csv'

with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"학생 성적이 {file_name}에 저장되었습니다.\n")

print("성적 분석 결과:")
scores = []

with open(file_name, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader) 
    
    for row in reader:
        name = row[0]
        score = int(row[1])
        scores.append(score)
        print(f"{name}: {score}점")

# 4. 평균 계산 및 출력
if scores:
    average = sum(scores) / len(scores)
    print(f"\n전체 평균: {average}점")