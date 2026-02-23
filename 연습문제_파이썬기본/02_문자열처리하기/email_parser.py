email = input("이메일 주소를 입력하세요: ")
split = email.split("@")
username = split[0]
domain = split[1]
print(f"사용자명: {username}")
print(f"도메인: {domain}")