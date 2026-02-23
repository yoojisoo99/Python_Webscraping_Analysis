score = int(input("점수를 입력하세요: "))
if score >= 90:
    print(f"점수 {score}점의 학점은 A입니다.")
elif score >= 80 and score < 90:
    print(f"점수 {score}점의 학점은 B입니다.")
elif score >= 70 and score < 80:
    print(f"점수 {score}점의 학점은 C입니다.")
elif score >= 60 and score < 70:
    print(f"점수 {score}점의 학점은 D입니다.")
else:
    print(f"점수 {score}점의 학점은 F입니다.")