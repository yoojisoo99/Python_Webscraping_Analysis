student = ["김철수","이영희","박민수","최수진"]
score = [85,92,78,95]
dic = dict(zip(student,score))
print(f"학생과 점수 매칭: ")
for name, s in dic.items():
    print(f"{name}: {s}점")
print(f"점수별 학생 딕셔너리: {dic}")