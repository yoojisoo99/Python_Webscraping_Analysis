def greet(name="손님", message="안녕하세요", suffix="님", extra=""):
    return f"{message}, {name}{suffix}!{extra}"

print(greet(name="김철수"))
print(greet(name="John", message="Hello", suffix=""))
print(greet(name="이영희", extra=" 좋은 하루 되세요"))